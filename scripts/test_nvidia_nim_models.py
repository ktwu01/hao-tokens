#!/usr/bin/env python3
"""Test NVIDIA NIM LLM models from the public LLM API docs.

The script loads .env, scrapes model IDs from NVIDIA's LLM API reference, and
tests each model one by one against /v1/chat/completions.
"""

import argparse
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request


DOCS_URL = "https://docs.api.nvidia.com/nim/reference/llm-apis"
DEFAULT_BASE_URL = "https://integrate.api.nvidia.com/v1"
TIMEOUT_BUCKETS = (10, 60, 600)
PROMPT = "用一句话回答：洗车应该开车去还是走路去？"


def load_dotenv(path=".env"):
  if not os.path.exists(path):
    return

  with open(path, encoding="utf-8") as env_file:
    for line in env_file:
      line = line.strip()
      if not line or line.startswith("#") or "=" not in line:
        continue

      key, value = line.split("=", 1)
      os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def fetch_text(url, timeout=30):
  request = urllib.request.Request(
    url,
    headers={
      "User-Agent": "Mozilla/5.0 nvidia-nim-model-tester",
      "Accept": "text/html,application/json",
    },
  )
  with urllib.request.urlopen(request, timeout=timeout) as response:
    return response.read().decode("utf-8", "replace")


def docs_models():
  text = fetch_text(DOCS_URL)
  models = []
  for raw in re.findall(r">([^<>]+ / [^<>]+)</a>", text):
    model = html.unescape(raw).strip().replace(" / ", "/")
    if model not in models:
      models.append(model)
  return models


def chat_completion(model, timeout):
  base_url = os.environ.get("NVIDIA_API_BASE", DEFAULT_BASE_URL).rstrip("/")
  api_key = os.environ["NVIDIA_API_KEY"]
  body = {
    "model": model,
    "messages": [{"role": "user", "content": PROMPT}],
    "temperature": 0.1,
    "top_p": 1,
    "max_tokens": 32,
    "stream": False,
  }
  command = [
    "curl",
    "-sS",
    "--connect-timeout", "10",
    "--max-time", str(timeout),
    f"{base_url}/chat/completions",
    "-H", f"Authorization: Bearer {api_key}",
    "-H", "Content-Type: application/json",
    "-d", json.dumps(body, ensure_ascii=False),
  ]
  completed = subprocess.run(command, capture_output=True, text=True, timeout=timeout + 5)
  if completed.returncode != 0:
    raise TimeoutError(completed.stderr.strip() or f"curl exited {completed.returncode}")
  if not completed.stdout.strip():
    raise RuntimeError("empty response body")
  payload = json.loads(completed.stdout)
  if "error" in payload:
    raise RuntimeError(json.dumps(payload["error"], ensure_ascii=False))
  if "choices" not in payload:
    raise RuntimeError(json.dumps(payload, ensure_ascii=False)[:500])
  content = payload["choices"][0]["message"].get("content")
  if content is None:
    raise RuntimeError("null message content")
  return content


def classify_model(model):
  last_error = None
  last_timeout = None
  last_elapsed = None
  for timeout in TIMEOUT_BUCKETS:
    start = time.monotonic()
    try:
      answer = chat_completion(model, timeout)
      elapsed = time.monotonic() - start
      return {
        "model": model,
        "status": "success",
        "bucket": f"<={timeout}s",
        "elapsed_seconds": round(elapsed, 3),
        "answer": answer.replace("\n", " ")[:240],
      }
    except Exception as exc:
      elapsed = time.monotonic() - start
      last_timeout = timeout
      last_elapsed = elapsed
      if isinstance(exc, urllib.error.HTTPError):
        detail = exc.read().decode("utf-8", "replace")[:500]
        last_error = f"HTTP {exc.code}: {detail}"
        break
      last_error = f"{type(exc).__name__}: {exc}"
      if "Failed to connect" in last_error:
        last_timeout = min(timeout, 10)
        break
      if elapsed < timeout * 0.8:
        break

  return {
    "model": model,
    "status": "fail",
    "bucket": f"fail_<={last_timeout}s" if last_timeout else ">600s/error",
    "elapsed_seconds": round(last_elapsed, 3) if last_elapsed is not None else None,
    "error": last_error,
  }


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--output", default="tmp/nvidia_nim_model_results.jsonl")
  parser.add_argument("--limit", type=int, default=0)
  parser.add_argument("--model", action="append", dest="models")
  args = parser.parse_args()

  load_dotenv()
  if "NVIDIA_API_KEY" not in os.environ:
    raise SystemExit("NVIDIA_API_KEY is missing. Add it to .env or export it.")

  models = args.models or docs_models()
  if args.limit:
    models = models[:args.limit]

  os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
  with open(args.output, "w", encoding="utf-8") as out:
    for index, model in enumerate(models, 1):
      print(f"[{index}/{len(models)}] {model}", flush=True)
      result = classify_model(model)
      print(json.dumps(result, ensure_ascii=False), flush=True)
      out.write(json.dumps(result, ensure_ascii=False) + "\n")
      out.flush()


if __name__ == "__main__":
  main()
