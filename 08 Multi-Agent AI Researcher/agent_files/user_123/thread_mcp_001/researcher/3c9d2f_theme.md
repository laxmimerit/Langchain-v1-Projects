## What is the history, origin, and development timeline of MCP? Who are the key creators?

### Focused Query 1: Who are the key creators of MCP?
The Model Context Protocol (MCP) was created by **David Soria Parra** and **Justin Spahr-Summers** at **Anthropic**.
- **Context:** The two developers were working on internal developer tooling at Anthropic around **July 2024**.
- **Motivation:** They were frustrated by the "M × N" integration problem—specifically the inability to easily move context between tools like Claude Desktop and IDEs (like Zed) without constant copy-pasting or building custom connectors for every single tool.
- **Inspiration:** The project was heavily inspired by the **Language Server Protocol (LSP)**, which solved a similar problem for programming language support in IDEs. They adopted similar design principles (like JSON-RPC) but adapted them for AI-specific needs (Tools, Resources, Prompts).

### Focused Query 2: What is the history and development timeline of MCP?
The development of MCP progressed rapidly from internal prototyping to an industry standard.

**Timeline:**
*   **July 2024 (Inception):** David Soria Parra and Justin Spahr-Summers begin working on the protocol at Anthropic.
*   **Mid-2024 (Development):** The protocol was built over a few months. The first external implementation was integrated into the **Zed** editor (approx. 1.5 months before the official release) to test it in the open.
*   **November 25, 2024 (Official Launch):** Anthropic officially released and open-sourced the Model Context Protocol (MCP). It was positioned as the "USB-C for AI applications."
    *   *Launch Features:* Included local MCP server support in Claude Desktop and an open-source repository of pre-built servers (Google Drive, Slack, GitHub, etc.).
*   **March 2025 (Major Adoption):** **OpenAI** officially adopted MCP, integrating it into ChatGPT Desktop, the Agents SDK, and the Responses API. This was a pivotal moment, signaling MCP's victory as the "de facto" standard over competitors (like OpenAI's earlier plugin systems).
*   **April 2025:** **Google DeepMind** (via Demis Hassabis) confirmed MCP support for Gemini models and infrastructure.
*   **December 2025 (Governance Shift):** Anthropic donated MCP to the **Agentic AI Foundation (AAIF)**, a directed fund under the Linux Foundation, co-founded by Anthropic, Block, and OpenAI. This move solidified its status as a neutral open standard.

### Focused Query 3: How has the protocol evolved?
*   **Version 1.0 (Nov 2024):** Focused on core primitives: Resources, Tools, and Prompts. Transport via Stdio and SSE.
*   **2025 Updates:**
    *   **Stateless/Streamable HTTP:** Introduced to allow easier horizontal scaling of MCP servers (moving away from purely stateful connections).
    *   **Async Operations:** Added support for long-running tasks (tasks that take minutes/hours).
    *   **Official Registry:** Launch of a centralized (but open) MCP Registry for discovering servers.
    *   **Agentic Capabilities:** Enhanced support for "sampling" (allowing servers to call back to the LLM) and nested MCP servers (servers that act as clients to other servers).

### Summary
The Model Context Protocol (MCP) was born in **July 2024** from the collaboration of **David Soria Parra** and **Justin Spahr-Summers** at **Anthropic**, who sought to solve the fragmentation of AI tool integrations. Heavily inspired by the Language Server Protocol (LSP), it was open-sourced on **November 25, 2024**. The protocol saw rapid industry consolidation in early 2025, with major adoption by **OpenAI** (March 2025) and **Google** (April 2025), effectively becoming the standard "USB-C" interface for the AI industry. By the end of 2025, governance was transferred to the Linux Foundation's **Agentic AI Foundation**, ensuring its long-term neutrality and growth.
