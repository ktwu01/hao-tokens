# 薅 tokens · hao-tokens

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/ktwu01/hao-tokens?style=flat&logo=github)](https://github.com/ktwu01/hao-tokens/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ktwu01/hao-tokens?style=flat&logo=github)](https://github.com/ktwu01/hao-tokens/fork)
![Last Verified](https://img.shields.io/badge/last%20verified-April%202026-brightgreen)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-blue)](CONTRIBUTING.md)
![License: CC0](https://img.shields.io/badge/license-CC0-lightgrey)
![Providers](https://img.shields.io/badge/providers-12-orange)

---

## 官方学生 / 教育入口（请在厂商站点再次确认）

| 产品 | 官方核对入口 | 备注（概括；**使用前请自行确认最新条款**） |
|------|----------------|------------------------------------------|
| **GitHub Copilot（学生）** | [GitHub Education – Students](https://education.github.com/students)、[学生 Copilot 说明](https://docs.github.com/copilot/how-tos/manage-your-account/free-access-with-copilot-student)、[教育权益设置](https://github.com/settings/education/benefits) | 核验通过的学生/教师可获得 **Copilot**；可与 **GitHub Models**、IDE 工作流搭配。 |
| **GitHub Student Developer Pack** | [Student Developer Pack](https://education.github.com/pack/) | 合作方权益合集；含 AI 相关项（如 **Notion Education + AI**、**Camber** LLM 条数等——请逐条阅读）。 |
| **Google Gemini（学生页）** | [Gemini for Students](https://gemini.google/students/) | 活动**随地区/时间变化**；多地曾推 **12 个月**学生方案，现页面可能侧重**试用**——请看站内 FAQ。 |
| **Perplexity – Education** | [Perplexity for Education](https://www.perplexity.com/education)、[Education Pro 帮助](https://www.perplexity.ai/help-center/en/articles/12590157-what-is-education-pro) | 价格在演变；学历核验（如 **SheerID**）常见；以官方为准。 |
| **OpenAI – ChatGPT / Edu / Codex** | [学生落地页示例](https://chat.openai.com/college-students/)、[ChatGPT Education](https://openai.com/chatgpt/education)、[Codex for Students](https://developers.openai.com/community/students) | 促销多**限时、分地区**；**Edu** 多为学校采购；**Codex** 美加学生约 **$100** 额度（以官方为准）。 |
| **Microsoft – Azure for Students** | [Azure for Students](https://azure.microsoft.com/free/students/) | 云额度；在允许范围内可用于**托管**与 **Azure OpenAI** 实验。 |

**Otter.ai：** 转写向。**Basic** 免费（有额度）；**Pro** [师生优惠](https://help.otter.ai/hc/en-us/articles/4402467517847-Student-Teacher-discount-program-for-the-Pro-plan)（常见 `.edu`）。价目 [otter.ai/pricing](https://otter.ai/pricing)。

---

**精选索引：**学生/教育 AI 权益与合规免费 API · 手册非破解 · [English](README.md)

---

## 为什么需要它

学生和自学者常常希望在**聊天 / 研究 / 写代码**场景里用 AI，又尽量不花钱。这里的「薅 token」指**合法叠加额度**：教育身份验证、开发者免费层，以及社区维护的、**仅引用厂商文档**的额度说明——而不是绕开计费或传播付费 Key。

---

## 方法：索引如何建立

我们在 GitHub 与开放网络上进行了**多轮**检索（2026-04），查询示例包括：

- `site:github.com student free LLM`、`free LLM API`、`awesome free inference`、`no-cost-ai`、Perplexity / Gemini / OpenAI 学生相关、`GitHub Education Copilot`

由此**抽样整理了 56+ 个仓库**（见下表）：**awesome 列表**、大列表的 **fork**、**学生优惠**说明、与免费 `base_url` API 配套的**客户端/UI**，以及**已粗筛**的相邻 SDK/工具链。Star 数会变化，请以仓库最新 README 为准。

仅靠网页搜索**无法在一次检索中可靠穷尽 50 个互不重复且已核验的 GitHub 仓库**（结果有上限且重复多）。下文列出调研中**较重要的来源**、可自行扩展的 **GitHub 搜索式**、分层仓库表、官方入口，以及**合规红线**。

---

## 全景：方法论与分层资源

### 如何自己快速找到 50+ 个相关仓库

登录 GitHub 后搜索上限通常更友好：

1. **免费 / API 列表**  
   `free llm api stars:>100`  
   `awesome free inference`  
   `permanent free tier LLM API`  
   `openrouter groq gemini free tier`

2. **学生 / 教育**  
   `student perks developer`  
   `awesome student resources`  
   `github education pack`  
   `student discount AI`

3. **网关 / 池化（基础设施）**  
   `litellm proxy`  
   `one-api LLM`  
   `new-api gateway`  
   `AI gateway OpenAI compatible`

列表成熟后可投稿元列表 **[sindresorhus/awesome](https://github.com/sindresorhus/awesome)**（审核较严）。

### 重要来源（分层）

#### A. 「基准级」免费 LLM / API 精选列表（信噪比较高）

认真做列表的人常会引用或合并这些：

| 仓库 | 作用 |
|------|------|
| [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | Star 很多；厂商覆盖面广 + 试用额度；社区强调「勿滥用」 |
| [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | 强调**长期**免费层；表格化，CC0 |
| [bradAGI/awesome-free-inference](https://github.com/bradAGI/awesome-free-inference) | 分层（免绑卡 / 赠额 / 自建）；含 LiteLLM 思路 |
| [nejib1/Free-LLM](https://github.com/nejib1/Free-LLM) | 目录式；有配套站点；厂商多 |

**同系 fork / 衍生（维护度可能较低）：**  
[KI-IAN/free-llm-api-resources-forked](https://github.com/KI-IAN/free-llm-api-resources-forked)、[nherx/free-llm-api-resources](https://github.com/nherx/free-llm-api-resources)

#### B. 学生与「全栈」福利（不止 LLM API）

| 仓库 / 页面 | 作用 |
|-------------|------|
| [jhaxce/student-perks](https://github.com/jhaxce/student-perks) | 学生福利整理（含云与 AI 等条目） |
| [Shashwat-19/awesome-student-resources](https://github.com/Shashwat-19/awesome-student-resources) | 面向学生的经典 awesome-list |
| [education/students](https://github.com/education/students) | GitHub Education 学生入口相关 |
| [GitHub Student Developer Pack](https://education.github.com/pack) | **Copilot**、Azure 额度、DO 等众多合作权益 |
| [Codex for Students](https://developers.openai.com/community/students) | 面向 Codex 的 **$100 ChatGPT 额度（美加，需核验）** — 官方 |

#### C. 基础设施：多把 Key 统一成 OpenAI 形态端点

| 项目 | 作用 |
|------|------|
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 主流方案：SDK + **AI 网关**，100+ 厂商，预算与路由 |
| [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | Key 管理与转发；OpenAI 兼容；Docker |
| [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | 新一代 fork：计费、鉴权、更多格式（AGPL） |
| [shenald-dev/one-api](https://github.com/shenald-dev/one-api) | 另一类统一网关（使用前请自行看协议与活跃度） |

较旧：[BerriAI/liteLLM-proxy](https://github.com/BerriAI/liteLLM-proxy) 已**弃用**，请以主仓库 `litellm` 为准。

#### D. 学习与上手（适合做学生向仓库的友链）

| 仓库 | 作用 |
|------|------|
| [microsoft/Mastering-GitHub-Copilot-for-Paired-Programming](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming) | 免费 Copilot 配套课程 |

### 红线（要长期可做、就别碰这些）

1. **不要推广公开贴第三方 API Key、或「复制这段 `sk-…`」类仓库。** 常见问题：**违反 ToS**、账号共享或近似欺诈，平台可能下架。把 [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) 这类当作**反面教材**。

2. 与 `cheahjs/free-llm-api-resources` 等「全集表」**差异化**要靠**细分定位**，而不是再抄一张大表：

   - **只收**正规学生/教职工验证路径（SheerID、GitHub Education、`.edu`、各地区项目）。
   - **区分** API 向 vs 纯聊天产品。
   - **区域矩阵**（美/加/欧/印…）+ **最后核查日期** + **一手链接**。
   - **「组合打法」**：如 GitHub Pack → Copilot + Azure → LiteLLM 配置骨架。

3. **法律声明**：链接仅供信息参考；资格与条款以各厂商为准；本站无商业隶属关系；请遵守 ToS。

### 本项目小结

- **发现层**：定位为**学生核验 + AI/API 免费层**，来源要严——不是「全网免费送 Key」。  
- **基础设施层**：统一路由用 **[LiteLLM](https://github.com/BerriAI/litellm)**；可选 **[one-api](https://github.com/songquanpeng/one-api)** / **[new-api](https://github.com/QuantumNous/new-api)** 做 Key 池管理——**池化仍须遵守各厂商条款**。

---

## 免费 / 按额度的 LLM **API**（合规厂商层）

这些**不是**「仅学生」，但与教育场景的聊天权益叠加后，是**零成本开发**的主力：

- **Google AI Studio（Gemini API）** — [`ai.google.dev`](https://ai.google.dev)
- **Groq** — [`console.groq.com`](https://console.groq.com)
- **OpenRouter（含免费模型路由）** — [`openrouter.ai`](https://openrouter.ai)
- **Cloudflare Workers AI** — 见 Cloudflare 控制台文档
- **GitHub Models** — 与 GitHub 账号/Copilot 等绑定；见 GitHub 文档
- **Mistral / Cohere / NVIDIA NIM / Together 等** — 常有**小额长期免费层**或**试用金**；注意脚注（手机号验证、是否参与训练等）

**惯用法：**多数 OpenAI 兼容厂商可用：

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://YOUR_PROVIDER_OPENAI_COMPAT_ENDPOINT/v1",
    api_key="YOUR_KEY",
)
```

进阶路由：[**LiteLLM**](https://github.com/BerriAI/litellm)（单入口对接多后端）。  
社区有 **GitHub Copilot → OpenAI 兼容本地代理**（如 LiteLLM + Copilot）等写法；请视为**个人开发**，并遵守 Copilot **限流**与政策。

---

## 56+ 个已调研 GitHub 仓库（书签表）

> **图例：** ⭐ = 大型「awesome/目录」式列表；🎓 = 学生优惠/教育角度说明；🛠 = 客户端、网关或可接免费后端的本地运行时；⚠ = 第三方转发/灰区风险—请自行阅读许可证与 ToS。

| # | 仓库 | 说明 |
|---|------|------|
| 1 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | ⭐ 免费/试用 API 厂商大全 |
| 2 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | ⭐ 偏「长期免费层」的 API 列表 |
| 3 | [bradAGI/awesome-free-inference](https://github.com/bradAGI/awesome-free-inference) | ⭐ 分层指南（免绑卡 / 试用 / 自建） |
| 4 | [amardeeplakshkar/awesome-free-llm-apis](https://github.com/amardeeplakshkar/awesome-free-llm-apis) | ⭐ fork 风格整理 + 对比表 |
| 5 | [nejib1/Free-LLM](https://github.com/nejib1/Free-LLM) | ⭐ 目录 + 配套站点 |
| 6 | [zebbern/no-cost-ai](https://github.com/zebbern/no-cost-ai) | ⭐ 很广的「零成本」服务索引（聊天+媒体） |
| 7 | [steven2358/awesome-generative-ai](https://github.com/steven2358/awesome-generative-ai) | ⭐ 超大列表（GenAI 工具、API、UI） |
| 8 | [nherx/free-llm-api-resources](https://github.com/nherx/free-llm-api-resources) | ⭐ 围绕免费 API 列表的社区打包 |
| 9 | [KI-IAN/free-llm-api-resources-forked](https://github.com/KI-IAN/free-llm-api-resources-forked) | ⭐ 跟踪上游免费 API 列表的 fork |
| 10 | [mto67200/perplexity-student-pro](https://github.com/mto67200/perplexity-student-pro) | 🎓 Perplexity 学生 Pro 说明（以 Perplexity 现行政策为准） |
| 11 | [popjane/free_chatgpt_api](https://github.com/popjane/free_chatgpt_api) | ⚠ 社区 OpenAI 形态端点；**非官方** |
| 12 | [Kourva/AwesomeChatGPTBot](https://github.com/Kourva/AwesomeChatGPTBot) | ⚠ Telegram 机器人聚合「免费源」 |
| 13 | [ChatTeach/FreeGPT](https://github.com/ChatTeach/FreeGPT) | ⚠ Web UI 堆叠非付费访问路径 |
| 14 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 🛠 多后端统一代理/路由器 |
| 15 | [ollama/ollama](https://github.com/ollama/ollama) | 🛠 本地推理（硬件即「免费层」） |
| 16 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 🛠 自托管多模型 UI |
| 17 | [lobehub/lobe-chat](https://github.com/lobehub/lobe-chat) | 🛠 开源聊天客户端；自备官方 Key |
| 18 | [ChatGPTNextWeb/ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web) | 🛠 Next.js 客户端接 OpenAI 兼容端点 |
| 19 | [continuedev/continue](https://github.com/continuedev/continue) | 🛠 IDE 助手；自带模型/端点 |
| 20 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | 🛠 API 网关 / Key 池（自建；合规自负） |
| 21 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | 🛠 new-api 系网关（计费、鉴权；AGPL） |
| 22 | [Calcium-Ion/new-api](https://github.com/Calcium-Ion/new-api) | 🛠 同系不同 fork（部署前请比对） |
| 23 | [shenald-dev/one-api](https://github.com/shenald-dev/one-api) | 🛠 另一类统一网关（请看协议/活跃度） |
| 24 | [mudler/LocalAI](https://github.com/mudler/LocalAI) | 🛠 OpenAI 兼容本地服务端 |
| 25 | [ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) | 🛠 本地权重的高效 CPU/GPU 推理 |
| 26 | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 🛠 多厂商聊天 UI |
| 27 | [mckaywrigley/chatbot-ui](https://github.com/mckaywrigley/chatbot-ui) | 🛠 简易开源聊天 UI |
| 28 | [Bin-Huang/chatbox](https://github.com/Bin-Huang/chatbox) | 🛠 跨平台桌面客户端 |
| 29 | [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | 📚 提示词模式（质量 > 单纯抠 token） |
| 30 | [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | 📚 官方示例与范式 |
| 31 | [google-gemini/cookbook](https://github.com/google-gemini/cookbook) | 📚 Gemini API 示例 |
| 32 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 📚 生成式 AI 入门课（含 Azure 笔记） |
| 33 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 🛠 应用框架；易切换免费后端 |
| 34 | [run-llama/llama_index](https://github.com/run-llama/llama_index) | 🛠 RAG / Agent；可接免费嵌入模型 |
| 35 | [huggingface/transformers](https://github.com/huggingface/transformers) | 🛠 模型库 + 推理基础组件 |
| 36 | [huggingface/chat-ui](https://github.com/huggingface/chat-ui) | 🛠 HF 生态聊天 UI |
| 37 | [vercel/ai](https://github.com/vercel/ai) | 🛠 流式 UI 用 TS SDK（可配免费 API） |
| 38 | [AntonOsika/gpt-engineer](https://github.com/AntonOsika/gpt-engineer) | 🛠 代码生成 CLI（自备 API Key） |
| 39 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 🛠 Agent 实验（自备 Key；注意费用） |
| 40 | [TransformerOptimus/SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | 🛠 Agent 平台（自备端点） |
| 41 | [KillianLucas/open-interpreter](https://github.com/KillianLucas/open-interpreter) | 🛠 本地/远端代码执行助手 |
| 42 | [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) | 🛠 🇨🇳 本地知识库 + 模型 |
| 43 | [binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic) | 🛠 偏研究与论文向聊天/工具 |
| 44 | [Giskard-AI/giskard](https://github.com/Giskard-AI/giskard) | 🛠 ML / LLM 评测（open core） |
| 45 | [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) | 🛠 本地权重 Web UI |
| 46 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 🛠 高性能推理服务（自建 GPU） |
| 47 | [skypilot-org/skypilot](https://github.com/skypilot-org/skypilot) | 🛠 多云训练/部署—配合**学生云额度** |
| 48 | [huggingface/agents-course](https://github.com/huggingface/agents-course) | 📚 HF Agent 课程（免费材料） |
| 49 | [anthropics/courses](https://github.com/anthropics/courses) | 📚 Anthropic 教学 notebooks |
| 50 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 📚 入门 AI 课（含低成本路径） |
| 51 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | 📚 LLM 动手课仓库 |
| 52 | [datawhalechina/hugging-llm](https://github.com/datawhalechina/hugging-llm) | 📚 🇨🇳 Datawhale《拥抱大模型》开源书/代码 |
| 53 | [jhaxce/student-perks](https://github.com/jhaxce/student-perks) | 🎓 学生福利整理（云 + AI 等） |
| 54 | [Shashwat-19/awesome-student-resources](https://github.com/Shashwat-19/awesome-student-resources) | 🎓 学生向 awesome：课程、云、AI |
| 55 | [education/students](https://github.com/education/students) | 🎓 GitHub Education「学生」枢纽仓 |
| 56 | [microsoft/Mastering-GitHub-Copilot-for-Paired-Programming](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming) | 📚 免费多模块 Copilot / 结对编程课 |
| — | [Gist: sudhxnva – Copilot + LiteLLM OpenAI 兼容代理](https://gist.github.com/sudhxnva/78172d7a46bf4a1e5663fc487c136121) | 🎓 搭建示例（个人使用；遵守 Copilot 限额） |

---

## 延伸阅读

- [Vibe Coding IDE 简评](https://koutian.is-a.dev/posts/2025/12/vibe-coding-ides-brief-comparison/) — 与免费额度、学生向工具链配套的 AI 辅助编辑器与工作流随笔。

---

## 贡献

欢迎 PR：

- **新增官方**学生/教育工作者链接（须为厂商页面，拒接引流/联盟垃圾）
- **更正**已结束的活动（尽量带日期 + 存档链接）
- **补充**仍在**积极维护**的高质量 GitHub 列表

请勿提交：共享的付费 API Key、盗窃凭证，或**主要目的**为逃避 ToS 的说明。

---

## 免责声明

内容仅供**信息参考**，可能在发布次日即**过期**。**你**需自行遵守法律、学校 AI 政策与厂商条款。不确定时，请优先使用**官方**教育项目与**文档记载**的免费额度。

---

## 许可证

本仓库以 [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) 释至公有领域。详见仓库根目录 [`LICENSE`](LICENSE)。外链网站与第三方仓库仍适用其各自许可证。
