#!/usr/bin/env python3
"""Call NVIDIA NIM using NVIDIA_API_KEY from the environment or .env.

No external Python packages are required.
"""

import os
import sys

from openai import OpenAI

DEFAULT_PROMPT = "我要去洗车店洗车，但是开车很麻烦，我是最好应该开车还是走路过去？"


def load_dotenv(path=".env"):
  if not os.path.exists(path):
    return

  with open(path, encoding="utf-8") as env_file:
    for line in env_file:
      line = line.strip()
      if not line or line.startswith("#") or "=" not in line:
        continue

      key, value = line.split("=", 1)
      key = key.strip()
      value = value.strip().strip("'\"")
      os.environ.setdefault(key, value)


load_dotenv()

client = OpenAI(
  base_url = os.environ.get("NVIDIA_API_BASE", "https://integrate.api.nvidia.com/v1"),
  api_key = os.environ["NVIDIA_API_KEY"],
  timeout = float(os.environ.get("NVIDIA_TIMEOUT_SECONDS", "600"))
)

completion = client.chat.completions.create(
  model=os.environ.get("NVIDIA_NIM_MODEL") or os.environ.get("NVIDIA_MODEL", "meta/llama-3.3-70b-instruct"),
  messages=[{"role":"user","content":" ".join(sys.argv[1:]) or DEFAULT_PROMPT}],
  temperature=1,
  top_p=0.95,
  max_tokens=512,
  stream=False
)

print(completion.choices[0].message.content)
