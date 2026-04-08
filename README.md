# 薅 tokens · hao-tokens

**Curated index: student / educator AI benefits, official free tiers, and legit “zero‑cost API” references.**  
This repo is a **handbook + link hub**, not a crack or credential sharing project. Prefer **official** education offers and **published** free quotas; respect each provider’s Terms of Service.

---

## Why this exists

Students and self‑learners often need **Chat / Research / Code** AI without burning money. “薅 token” here means **stacking legitimate allowances**: education verification, free developer tiers, and community‑maintained directories of **provider‑documented** limits—not bypassing billing or sharing paid keys.

---

## Method: how we built the index

We ran **multiple rounds** of discovery (2026‑04) across GitHub and the open web, including queries like:

- `site:github.com student free LLM`, `free LLM API`, `awesome free inference`, `no-cost-ai`, `perplexity student`, `Gemini student`, `OpenAI student`, `GitHub Education Copilot`

From that we **sampled 50+ repositories** (see table below): **awesome lists**, **forks of major lists**, **student‑offer write‑ups**, **client/UI projects** that pair well with free `base_url` APIs, plus **vetted adjacent SDK/tooling**. Star counts drift; always open the repo for the latest README.

---

## Official student / education entry points (verify on the provider site)

| Product | What to check (official) | Notes (high level; **confirm before relying**) |
|--------|---------------------------|--------------------------------------------------|
| **GitHub Copilot (Student)** | [GitHub Education – Students](https://education.github.com/students), [Copilot for students](https://docs.github.com/copilot/how-tos/manage-your-account/free-access-with-copilot-student), [Education benefits settings](https://github.com/settings/education/benefits) | Verified students/teachers may get **Copilot** access; pairs with **GitHub Models** and IDE flows. |
| **GitHub Student Developer Pack** | [Student Developer Pack](https://education.github.com/pack/) | Bundle of partner offers; includes AI‑adjacent perks (e.g. items that mention **Notion Education + AI**, **Camber** LLM message quotas, etc.—read each offer). |
| **Google Gemini (students page)** | [Gemini for Students](https://gemini.google/students/) | Promotions **change by region/time**. Many regions previously ran a **12‑month student promo**; pages may now emphasize **trials** or alternate wording—read the FAQ on the live site. |
| **Perplexity – Education** | [Perplexity for Education](https://www.perplexity.com/education), [Education Pro help](https://www.perplexity.ai/help-center/en/articles/12590157-what-is-education-pro) | Programs and pricing **evolve**; edu verification (e.g. **SheerID**) is common. |
| **OpenAI – ChatGPT / Edu** | [ChatGPT for students landing](https://chat.openai.com/college-students/), [ChatGPT Education (Edu)](https://openai.com/chatgpt/education) | **Time‑boxed** student promos have appeared in the past (region‑specific); **ChatGPT Edu** is typically **institution‑purchased**, not a personal toggle. |
| **Microsoft – Azure for Students** | [Azure for Students](https://azure.microsoft.com/free/students/) | Cloud credits; useful for **hosting** and **Azure OpenAI** experiments where allowed. |

**Otter (Otter.ai):** If you meant **[Otter.ai](https://otter.ai)** voice notes: look for **Education / student** pages and eligibility in your country—they change often and are **not** GitHub‑centric. This repo focuses on **LLM tokens / AI plans**; Otter is listed so the name isn’t a dead end.

---

## Free / quota‑based LLM **APIs** (legit provider tiers)

These are **not** “student only,” but they are the backbone of **zero‑cost dev** when combined with education chat offers:

- **Google AI Studio (Gemini API)** — [`ai.google.dev`](https://ai.google.dev)
- **Groq** — [`console.groq.com`](https://console.groq.com)
- **OpenRouter (free model routes)** — [`openrouter.ai`](https://openrouter.ai)
- **Cloudflare Workers AI** — docs via Cloudflare dashboard
- **GitHub Models** — tied to GitHub account / Copilot plan; see GitHub docs
- **Mistral / Cohere / NVIDIA NIM / Together / etc.** — often have **small perpetual free tiers** or **trial credits**; read the pricing footnotes (phone verify, training opt‑in, etc.)

**Pattern:** most OpenAI‑compatible providers accept:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://YOUR_PROVIDER_OPENAI_COMPAT_ENDPOINT/v1",
    api_key="YOUR_KEY",
)
```

Advanced routing: [**LiteLLM**](https://github.com/BerriAI/litellm) (single entrypoint to many backends).  
**GitHub Copilot → OpenAI‑compatible local proxy** is described in community writeups (e.g. LiteLLM + Copilot); treat as **personal dev only**, subject to Copilot **rate limits** and policy.

---

## 50+ GitHub repositories surveyed (bookmark list)

> **Legend:** ⭐ = large “awesome / directory” style list; 🎓 = student offer write‑up / education angle; 🛠 = client, gateway, or local runtime that **uses** free backends; ⚠ = third‑party relay / grey‑area risk—read licenses & ToS yourself.

| # | Repository | Role |
|---|------------|------|
| 1 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | ⭐ Broad directory of free / trial API providers |
| 2 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | ⭐ Curated “permanent free tier” API list |
| 3 | [bradAGI/awesome-free-inference](https://github.com/bradAGI/awesome-free-inference) | ⭐ Tiered guide (no card / trials / self‑host) |
| 4 | [amardeeplakshkar/awesome-free-llm-apis](https://github.com/amardeeplakshkar/awesome-free-llm-apis) | ⭐ Fork‑style curated list + comparison tables |
| 5 | [nejib1/Free-LLM](https://github.com/nejib1/Free-LLM) | ⭐ Directory + site companion |
| 6 | [zebbern/no-cost-ai](https://github.com/zebbern/no-cost-ai) | ⭐ Very wide “no‑cost” services index (chat + media) |
| 7 | [steven2358/awesome-generative-ai](https://github.com/steven2358/awesome-generative-ai) | ⭐ Mega‑list (GenAI tools, APIs, UIs) |
| 8 | [nherx/free-llm-api-resources](https://github.com/nherx/free-llm-api-resources) | ⭐ Community packaging around free‑API list |
| 9 | [KI-IAN/free-llm-api-resources-forked](https://github.com/KI-IAN/free-llm-api-resources-forked) | ⭐ Fork tracking upstream free‑API list |
| 10 | [mto67200/perplexity-student-pro](https://github.com/mto67200/perplexity-student-pro) | 🎓 Student Perplexity Pro guide (verify against live Perplexity policies) |
| 11 | [popjane/free_chatgpt_api](https://github.com/popjane/free_chatgpt_api) | ⚠ Community OpenAI‑shape endpoint; **non‑official** |
| 12 | [Kourva/AwesomeChatGPTBot](https://github.com/Kourva/AwesomeChatGPTBot) | ⚠ Telegram bot multiplexing “free providers” |
| 13 | [ChatTeach/FreeGPT](https://github.com/ChatTeach/FreeGPT) | ⚠ Web UI stacking unpaid access paths |
| 14 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 🛠 Unified proxy / router for many LLM backends |
| 15 | [ollama/ollama](https://github.com/ollama/ollama) | 🛠 Local inference runner (hardware = “free tier”) |
| 16 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 🛠 Self‑hosted UI for many model backends |
| 17 | [lobehub/lobe-chat](https://github.com/lobehub/lobe-chat) | 🛠 Open chat client; plug in official keys |
| 18 | [ChatGPTNextWeb/ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web) | 🛠 Next.js client for OpenAI‑compatible endpoints |
| 19 | [continuedev/continue](https://github.com/continuedev/continue) | 🛠 IDE assistant; bring your own model / endpoint |
| 20 | [Songquanpeng/one-api](https://github.com/Songquanpeng/one-api) | 🛠 API gateway / key pool (self‑host; compliance is on you) |
| 21 | [Calcium-Ion/new-api](https://github.com/Calcium-Ion/new-api) | 🛠 Open‑source API gateway (successor‑style ecosystem) |
| 22 | [mudler/LocalAI](https://github.com/mudler/LocalAI) | 🛠 OpenAI‑compatible local server |
| 23 | [ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) | 🛠 Efficient CPU/GPU inference for local weights |
| 24 | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 🛠 Multi‑provider chat UI |
| 25 | [mckaywrigley/chatbot-ui](https://github.com/mckaywrigley/chatbot-ui) | 🛠 Simple OSS chat UI |
| 26 | [Bin-Huang/chatbox](https://github.com/Bin-Huang/chatbox) | 🛠 Cross‑platform desktop client |
| 27 | [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | 📚 Prompt patterns (quality over raw tokens) |
| 28 | [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | 📚 Official patterns & examples |
| 29 | [google-gemini/cookbook](https://github.com/google-gemini/cookbook) | 📚 Gemini API examples |
| 30 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 📚 Beginner GenAI course (incl. Azure notes) |
| 31 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 🛠 App framework; swap free backends easily |
| 32 | [run-llama/llama_index](https://github.com/run-llama/llama_index) | 🛠 RAG / agents; plug in free embeddings models |
| 33 | [huggingface/transformers](https://github.com/huggingface/transformers) | 🛠 Model zoo + inference building blocks |
| 34 | [huggingface/chat-ui](https://github.com/huggingface/chat-ui) | 🛠 OSS chat UI from HF ecosystem |
| 35 | [vercel/ai](https://github.com/vercel/ai) | 🛠 TS SDK for streaming UIs (pair with free APIs) |
| 36 | [AntonOsika/gpt-engineer](https://github.com/AntonOsika/gpt-engineer) | 🛠 Codegen CLI (BYO API key) |
| 37 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 🛠 Agent experiments (BYO keys; mind cost) |
| 38 | [TransformerOptimus/SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | 🛠 Agent platform (BYO endpoints) |
| 39 | [KillianLucas/open-interpreter](https://github.com/KillianLucas/open-interpreter) | 🛠 Local/remote code exec assistant |
| 40 | [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) | 🛠 🇨🇳 Local knowledge‑base + models |
| 41 | [binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic) | 🛠 Research oriented chat/tooling |
| 42 | [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) | 🛠 ML testing / LLM eval (open core) |
| 43 | [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) | 🛠 Web UI for local LLM weights |
| 44 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 🛠 Fast inference server (self‑host GPUs) |
| 45 | [skypilot-org/skypilot](https://github.com/skypilot-org/skypilot) | 🛠 Train/serve across clouds—use **student credits** smartly |
| 46 | [huggingface/agents-course](https://github.com/huggingface/agents-course) | 📚 HF agents course (free materials) |
| 47 | [anthropics/courses](https://github.com/anthropics/courses) | 📚 Anthropic educational course notebooks |
| 48 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 📚 Intro AI curriculum (incl. low‑cost options) |
| 49 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 📚 Hands‑on LLM course repo |
| 50 | [datawhalechina/hugging-llm](https://github.com/datawhalechina/hugging-llm) | 📚 🇨🇳 Datawhale “Hugging LLM” open book / code |
| — | [Gist: sudhxnva – Copilot + LiteLLM OpenAI‑compatible proxy](https://gist.github.com/sudhxnva/78172d7a46bf4a1e5663fc487c136121) | 🎓 Setup recipe (personal use; obey Copilot caps) |

---

## Contributing

PRs welcome for:

- **New official** student / educator URLs (must be vendor pages, not affiliate spam)
- **Corrections** when an offer expires (date + archive link if possible)
- **Extra** high‑quality GitHub lists that are **actively maintained**

Please **do not** submit: shared paid API keys, stolen credentials, or instructions whose **primary** purpose is ToS evasion.

---

## Disclaimer

Information is **informational** and may be **out of date** the day after we write it. **You** are responsible for compliance with laws, school AI policies, and provider Terms. When in doubt, use **official** education programs and **documented** free quotas.

---

## License

This repository is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). See the [`LICENSE`](LICENSE) file in the repo root. External sites and third‑party repositories linked here keep their own licenses.
