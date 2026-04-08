# 薅 tokens · hao-tokens

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/ktwu01/hao-tokens?style=flat&logo=github)](https://github.com/ktwu01/hao-tokens/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ktwu01/hao-tokens?style=flat&logo=github)](https://github.com/ktwu01/hao-tokens/fork)
![Last Verified](https://img.shields.io/badge/last%20verified-March%202026-brightgreen)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-blue)](CONTRIBUTING.md)
![License: CC0](https://img.shields.io/badge/license-CC0-lightgrey)
![Providers](https://img.shields.io/badge/providers-12-orange)

---

## Official student / education entry points (verify on the provider site)

| Product | Official links | Notes (high level; **confirm latest terms yourself**) |
|---------|----------------|--------------------------------------------------------|
| **GitHub Copilot (Student)** | [GitHub Education – Students](https://education.github.com/students), [Copilot for students](https://docs.github.com/copilot/how-tos/manage-your-account/free-access-with-copilot-student), [Education benefits](https://github.com/settings/education/benefits) | Verified students/teachers may get **Copilot**; pairs with **GitHub Models** and IDE flows. |
| **GitHub Student Developer Pack** | [Student Developer Pack](https://education.github.com/pack/) | Partner bundle; includes AI‑adjacent perks (**Notion Education + AI**, **Camber** LLM quotas, etc.—read each offer). |
| **Google Gemini (students)** | [Gemini for Students](https://gemini.google/students/) | Promos **vary by region/time**; some regions ran a **12‑month** student deal; pages may emphasize **trials**—see live FAQ. |
| **Perplexity – Education** | [Perplexity for Education](https://www.perplexity.com/education), [Education Pro](https://www.perplexity.ai/help-center/en/articles/12590157-what-is-education-pro) | Pricing **evolves**; edu verification (e.g. **SheerID**) is common; trust **official** copy only. |
| **OpenAI – ChatGPT / Edu / Codex** | [Students landing](https://chat.openai.com/college-students/), [ChatGPT Education](https://openai.com/chatgpt/education), [Codex for Students](https://developers.openai.com/community/students) | Promos often **time‑boxed / region‑specific**; **Edu** is usually **institution‑purchased**; **Codex** ~**$100** credits for verified **US/CA** students (per official page). |
| **Microsoft – Azure for Students** | [Azure for Students](https://azure.microsoft.com/free/students/) | Cloud credits; **hosting** and **Azure OpenAI** experiments where allowed. |

**Otter.ai:** Transcription‑focused. **Basic** is free (limits); **Pro** has a [student & teacher discount](https://help.otter.ai/hc/en-us/articles/4402467517847-Student-Teacher-discount-program-for-the-Pro-plan) (often `.edu`). See [otter.ai/pricing](https://otter.ai/pricing).

---

**Handbook + link hub** — student/educator AI benefits & legit free API refs; not key sharing · [简体中文](README.zh-CN.md)

---

## Why this exists

Students and self‑learners often need **Chat / Research / Code** AI without burning money. “薅 token” here means **stacking legitimate allowances**: education verification, free developer tiers, and community‑maintained directories of **provider‑documented** limits—not bypassing billing or sharing paid keys.

---

## Method: how we built the index

We ran **multiple rounds** of discovery (2026‑04) across GitHub and the open web, including queries like:

- `site:github.com student free LLM`, `free LLM API`, `awesome free inference`, `no-cost-ai`, `perplexity student`, `Gemini student`, `OpenAI student`, `GitHub Education Copilot`

From that we **sampled 56+ repositories** (see table below): **awesome lists**, **forks of major lists**, **student‑offer write‑ups**, **client/UI projects** that pair well with free `base_url` APIs, plus **vetted adjacent SDK/tooling**. Star counts drift; always open the repo for the latest README.

We could not reliably **enumerate 50 distinct GitHub repositories with verification in one pass** from web search alone (results are capped and repetitive). The subsection below lists **substantive sources** the survey surfaced, **GitHub searches** to find dozens more, tiered repo tables, official vendor pages, and **red flags** for staying legitimate.

---

## Landscape report: methodology & tiered sources

### How to get 50+ repos yourself (fast)

Use GitHub’s search (logged in yields better caps):

1. **Free / API lists**  
   `free llm api stars:>100`  
   `awesome free inference`  
   `permanent free tier LLM API`  
   `openrouter groq gemini free tier`

2. **Student / education**  
   `student perks developer`  
   `awesome student resources`  
   `github education pack`  
   `student discount AI`

3. **Gateways / pooling (infra)**  
   `litellm proxy`  
   `one-api LLM`  
   `new-api gateway`  
   `AI gateway OpenAI compatible`

Bookmark the **Awesome** meta-list once your list is mature: [sindresorhus/awesome](https://github.com/sindresorhus/awesome) (submission process is strict).

### Important sources (tiered)

#### A. “Canonical” free-LLM / API curated lists (high signal)

These are references serious list-makers cite or merge from:

| Repo | Role |
|------|------|
| [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | Very starred; broad provider list + trials; “don’t abuse” culture |
| [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | Focus: **permanent** free tiers; table-style, CC0 |
| [bradAGI/awesome-free-inference](https://github.com/bradAGI/awesome-free-inference) | Tiers (no card / credits / self-hosted); LiteLLM angle |
| [nejib1/Free-LLM](https://github.com/nejib1/Free-LLM) | Directory style; companion site; many providers |

**Forks / derivatives (same lineage, lower maintenance):**  
[KI-IAN/free-llm-api-resources-forked](https://github.com/KI-IAN/free-llm-api-resources-forked), [nherx/free-llm-api-resources](https://github.com/nherx/free-llm-api-resources)

#### B. Student & “whole stack” perks (not only LLM API)

| Repo / page | Role |
|-------------|------|
| [jhaxce/student-perks](https://github.com/jhaxce/student-perks) | Curated student benefits DB (includes AI rows) |
| [Shashwat-19/awesome-student-resources](https://github.com/Shashwat-19/awesome-student-resources) | Classic awesome-list for students |
| [education/students](https://github.com/education/students) | GitHub Education entry |
| [GitHub Student Developer Pack](https://education.github.com/pack) | **Copilot**, Azure credits, DO, many partners |
| [Codex for Students](https://developers.openai.com/community/students) | **$100 ChatGPT credits (US/CA, verified)** for Codex — official |

#### C. Infrastructure: unify many keys behind one OpenAI-shaped endpoint

| Project | Role |
|---------|------|
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Standard choice: SDK + **AI Gateway**, 100+ providers, budgets, routing |
| [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | Key management / redistribution; OpenAI-shaped; Docker |
| [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | Next-gen fork: billing, auth, more formats (AGPL) |
| [shenald-dev/one-api](https://github.com/shenald-dev/one-api) | Another unified-gateway variant (verify activity/license for your use) |

Older: [BerriAI/liteLLM-proxy](https://github.com/BerriAI/liteLLM-proxy) is **deprecated** in favor of main `litellm`.

#### D. Learning / adoption (good cross-links for a student-facing repo)

| Repo | Role |
|------|------|
| [microsoft/Mastering-GitHub-Copilot-for-Paired-Programming](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming) | Free courseware for Copilot |

### Red flags (stay legitimate and durable)

1. **Avoid promoting repos that publish live third-party API keys** or “paste this `sk-…`” lists. That is often **TOS abuse**, **account sharing**, or **fraud-adjacent**, and platforms may remove it. Treat [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys)-style projects as **anti-patterns** for a serious list.

2. **Differentiate** from `cheahjs/free-llm-api-resources` et al. by **niche**, not by duplicating tables:

   - **Only** accredited student / educator verification paths (SheerID, GitHub Education, `.edu`, regional programs).
   - **Only** API-oriented offers vs chat-only.
   - **Regional matrix** (US/CA/EU/IN…) with **last-checked date** and **primary source link**.
   - **“Stack recipes”**: e.g. GitHub Pack → Copilot + Azure → LiteLLM config skeleton.

3. **Legal copy:** links are informational; eligibility and terms are set by each vendor; no affiliation; comply with ToS.

### Bottom line for this project

- **Discovery layer:** niche is **student-verified AI & API access + free tiers**, with strict sourcing—not a generic free-key dump.  
- **Infra layer:** **[LiteLLM](https://github.com/BerriAI/litellm)** for unified routing; optionally **[one-api](https://github.com/songquanpeng/one-api)** / **[new-api](https://github.com/QuantumNous/new-api)** for key pool management—**pooling must respect each provider’s terms**.

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

## 56+ GitHub repositories surveyed (bookmark list)

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
| 20 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | 🛠 API gateway / key pool (self‑host; compliance is on you) |
| 21 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | 🛠 LLM gateway fork ecosystem (billing, auth; AGPL) |
| 22 | [Calcium-Ion/new-api](https://github.com/Calcium-Ion/new-api) | 🛠 Related new-api lineage (verify which fork you deploy) |
| 23 | [shenald-dev/one-api](https://github.com/shenald-dev/one-api) | 🛠 Unified-gateway variant (check license/activity) |
| 24 | [mudler/LocalAI](https://github.com/mudler/LocalAI) | 🛠 OpenAI‑compatible local server |
| 25 | [ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) | 🛠 Efficient CPU/GPU inference for local weights |
| 26 | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 🛠 Multi‑provider chat UI |
| 27 | [mckaywrigley/chatbot-ui](https://github.com/mckaywrigley/chatbot-ui) | 🛠 Simple OSS chat UI |
| 28 | [Bin-Huang/chatbox](https://github.com/Bin-Huang/chatbox) | 🛠 Cross‑platform desktop client |
| 29 | [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | 📚 Prompt patterns (quality over raw tokens) |
| 30 | [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | 📚 Official patterns & examples |
| 31 | [google-gemini/cookbook](https://github.com/google-gemini/cookbook) | 📚 Gemini API examples |
| 32 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 📚 Beginner GenAI course (incl. Azure notes) |
| 33 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 🛠 App framework; swap free backends easily |
| 34 | [run-llama/llama_index](https://github.com/run-llama/llama_index) | 🛠 RAG / agents; plug in free embeddings models |
| 35 | [huggingface/transformers](https://github.com/huggingface/transformers) | 🛠 Model zoo + inference building blocks |
| 36 | [huggingface/chat-ui](https://github.com/huggingface/chat-ui) | 🛠 OSS chat UI from HF ecosystem |
| 37 | [vercel/ai](https://github.com/vercel/ai) | 🛠 TS SDK for streaming UIs (pair with free APIs) |
| 38 | [AntonOsika/gpt-engineer](https://github.com/AntonOsika/gpt-engineer) | 🛠 Codegen CLI (BYO API key) |
| 39 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 🛠 Agent experiments (BYO keys; mind cost) |
| 40 | [TransformerOptimus/SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | 🛠 Agent platform (BYO endpoints) |
| 41 | [KillianLucas/open-interpreter](https://github.com/KillianLucas/open-interpreter) | 🛠 Local/remote code exec assistant |
| 42 | [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) | 🛠 🇨🇳 Local knowledge‑base + models |
| 43 | [binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic) | 🛠 Research oriented chat/tooling |
| 44 | [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) | 🛠 ML testing / LLM eval (open core) |
| 45 | [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) | 🛠 Web UI for local LLM weights |
| 46 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 🛠 Fast inference server (self‑host GPUs) |
| 47 | [skypilot-org/skypilot](https://github.com/skypilot-org/skypilot) | 🛠 Train/serve across clouds—use **student credits** smartly |
| 48 | [huggingface/agents-course](https://github.com/huggingface/agents-course) | 📚 HF agents course (free materials) |
| 49 | [anthropics/courses](https://github.com/anthropics/courses) | 📚 Anthropic educational course notebooks |
| 50 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 📚 Intro AI curriculum (incl. low‑cost options) |
| 51 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 📚 Hands‑on LLM course repo |
| 52 | [datawhalechina/hugging-llm](https://github.com/datawhalechina/hugging-llm) | 📚 🇨🇳 Datawhale “Hugging LLM” open book / code |
| 53 | [jhaxce/student-perks](https://github.com/jhaxce/student-perks) | 🎓 Curated student benefits DB (cloud + AI rows) |
| 54 | [Shashwat-19/awesome-student-resources](https://github.com/Shashwat-19/awesome-student-resources) | 🎓 Awesome-list: courses, cloud, AI tools for students |
| 55 | [education/students](https://github.com/education/students) | 🎓 GitHub Education “students” hub repository |
| 56 | [microsoft/Mastering-GitHub-Copilot-for-Paired-Programming](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming) | 📚 Free multi-module Copilot / peer-programming course |
| — | [Gist: sudhxnva – Copilot + LiteLLM OpenAI‑compatible proxy](https://gist.github.com/sudhxnva/78172d7a46bf4a1e5663fc487c136121) | 🎓 Setup recipe (personal use; obey Copilot caps) |

---

## Related reading

- [Vibe coding IDEs: a brief comparison](https://koutian.is-a.dev/posts/2025/12/vibe-coding-ides-brief-comparison-en/) — companion note on AI‑assisted editors and workflows alongside free tokens and student tooling.

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
