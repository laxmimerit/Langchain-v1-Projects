## What is the history, origin, and development timeline of MCP? Who are the key creators?

### Focused Query 1: Model Context Protocol MCP history origin timeline
The **Model Context Protocol (MCP)** was officially introduced and open-sourced by **Anthropic** on **November 25, 2024**. Its creation was driven by the need to solve the "N×M" integration problem in the AI industry, where every new AI model required custom connectors to interface with every different data source or tool.

Before MCP, developers relied on brittle, one-off integrations or proprietary "function-calling" APIs (like OpenAI's 2023 approach) that locked them into specific vendors. MCP was designed as a universal, open standard—often described as the "USB-C for AI applications"—to standardize how AI assistants connect to systems like content repositories, business tools, and development environments.

The protocol's development history reflects a rapid transition from a single-company initiative to an industry-wide standard:
*   **Pre-2024:** The concept of **MOP (Model Object Protocol)** existed as a precursor, focusing on making models tool-aware. MCP evolved from this to prioritize broader context and interoperability.
*   **November 25, 2024:** Anthropic launches MCP as an open standard, releasing SDKs and specifications.
*   **Early 2025:** Rapid experimentation and adoption by major tech players like AWS, Red Hat, and IBM.
*   **March 2025:** **OpenAI** officially adopts MCP, integrating it into its Agents SDK and ChatGPT desktop app, marking a critical moment of cross-industry consensus.
*   **April 2025:** **Google DeepMind** confirms MCP support for its Gemini models.
*   **December 2025:** In a move to ensure long-term neutrality and governance, Anthropic donates MCP to the **Agentic AI Foundation (AAIF)**, a fund under the Linux Foundation co-founded by Anthropic, OpenAI, and Block.

### Focused Query 2: Who created Model Context Protocol MCP key creators
The Model Context Protocol was created at **Anthropic**. The key individuals credited with its development are:
*   **David Soria Parra**: Co-creator and developer at Anthropic.
*   **Justin Spahr-Summers**: Co-creator and developer at Anthropic.

These developers designed MCP to resemble the **Language Server Protocol (LSP)**, leveraging similar message-flow concepts and **JSON-RPC 2.0** as the transport mechanism. Their goal was to create a "nervous system" for AI, allowing models to "sense" and "act" on external data without needing to be retrained or heavily customized for each new tool.

### Focused Query 3: Model Context Protocol evolution development
Since its release, MCP has evolved from a basic connection protocol to a comprehensive ecosystem for "agentic" workflows.
*   **November 2024 (v0.1):** Initial release focusing on reading resources, executing tools, and managing prompts.
*   **2025 Evolution:**
    *   **ACP (Agentic Commerce Protocol):** In early 2025, OpenAI and Stripe introduced ACP to handle *transactions* (buying/selling), complementing MCP's focus on *context* (reading/reasoning).
    *   **Security & Governance:** As adoption grew, focus shifted to security. In April 2025, researchers identified vulnerabilities like prompt injection, leading to tighter security specifications.
    *   **November 2025 (1-Year Anniversary Update):** A major spec update (version 2025-11-25) introduced:
        *   **Task-Based Workflows:** Enabling long-running, asynchronous operations.
        *   **Agentic Servers:** allowing servers to run their own loops using client tokens.
        *   **Simplified Authorization:** New flows for OAuth and secure credential handling.

### Summary
The Model Context Protocol (MCP) originated at **Anthropic** in **November 2024**, created by **David Soria Parra** and **Justin Spahr-Summers**. It was designed to solve the fragmentation of AI integrations by providing a universal standard for connecting LLMs to data and tools. Its history is characterized by extremely rapid industry consolidation; within months of its release, competitors like **OpenAI** and **Google** adopted it, effectively ending the "connector wars." By late 2025, governance was transferred to the **Linux Foundation**, cementing its status as a neutral, foundational layer of the AI stack—comparable to HTTP for the web or LSP for coding tools. Its evolution has moved quickly from simple data retrieval to supporting complex, asynchronous agentic workflows and secure commerce.