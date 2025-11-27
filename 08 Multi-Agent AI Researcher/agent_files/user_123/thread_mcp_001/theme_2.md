## What is the history and evolution of MCP?

### Focused Query 1: "Model Context Protocol origin" & "Anthropic MCP announcement"
The Model Context Protocol (MCP) originated from an internal project at Anthropic. The idea was conceived by David Soria Parra, a software engineer at Anthropic, who was motivated by the frustration of constantly switching between Claude Desktop and his code editor for AI-assisted coding. He recognized a need for a standardized way to connect large language models (LLMs) with external tools and data sources.

His inspiration came from the Language Server Protocol (LSP), which standardizes communication between code editors and language-specific servers to provide features like autocomplete and diagnostics. Parra, along with Justin Spahr-Summers, laid the foundation for MCP, aiming to solve the "MxN problem" – where 'M' LLMs and 'N' integrations would traditionally require M*N custom connectors.

Anthropic officially announced and open-sourced the Model Context Protocol on **November 25, 2024**.

### Focused Query 2: "When was MCP protocol released"
The Model Context Protocol (MCP) was first released to the public by Anthropic on **November 25, 2024**.

### Focused Query 3: "MCP protocol evolution timeline"
Since its initial release, MCP has seen rapid adoption and continuous evolution:

*   **Pre-Launch (2024):** Internal hackathons at Anthropic demonstrated rapid, organic adoption of MCP for building tools and integrations with Claude Desktop.
*   **November 25, 2024:** Public launch of MCP by Anthropic as an open standard. This included the initial specification, SDKs, local MCP server support in Claude Desktop apps, and an open-source repository of reference servers (e.g., for Google Drive, Slack, GitHub).
*   **Early 2025 (March-April):** Significant industry adoption began:
    *   **OpenAI** officially adopted MCP, integrating it into ChatGPT desktop app, Agents SDK, and Responses API (March 2025).
    *   **Google DeepMind** confirmed support for MCP in upcoming Gemini models and infrastructure (April 2025).
    *   **Microsoft** integrated MCP with Semantic Kernel and Azure OpenAI services.
    *   Development tools like Zed, Replit, Codeium, and Sourcegraph started working with MCP.
*   **September 2025 (Preview):** The **MCP Registry** was launched in preview as a centralized index for discovering available MCP servers, experiencing rapid growth in listed entries.
*   **November 25, 2025 (First Anniversary Release):** A major update to the MCP specification was released, introducing several key features and enhancements:
    *   **Task-based Workflows:** Experimental support for managing long-running, multi-step operations with defined states (working, input_required, completed, failed, cancelled).
    *   **Simplified Authorization Flows:** Introduction of URL-based client registration using OAuth Client ID Metadata Documents (SEP-991) to streamline authentication, moving away from complex Dynamic Client Registration.
    *   **Extensions Framework:** A mechanism to extend the core protocol with optional, additive, and composable capabilities for specialized use cases (e.g., authorization extensions like OAuth client credentials support and Enterprise IdP policy controls).
    *   **URL Mode Elicitation:** Enables secure, out-of-band interactions for credential acquisition (e.g., OAuth flows in a browser) without exposing sensitive information directly to the MCP client.
    *   **Sampling with Tools (Agentic Servers):** Allows MCP servers to implement their own agentic loops and include tool calling within sampling requests, enabling more sophisticated server-side reasoning and parallel tool execution.
    *   **Developer Experience Improvements:** Minor enhancements for standardized tool names, decoupled request payloads, SSE polling, and improved specification version management.
*   **Ongoing Evolution:** The protocol continues to evolve with a focus on reliability, observability, server composition, and refining the security model to meet enterprise needs. Community participation through Specification Enhancement Proposals (SEPs) and Working/Interest Groups drives its development.

### Summary
MCP was born from Anthropic in late 2024 to standardize LLM-tool integration, inspired by LSP. It quickly gained traction, with major AI players like OpenAI and Google adopting it within months. Its evolution is marked by significant annual updates, introducing features like task-based workflows, simplified authorization, and an extensions framework, all driven by a collaborative open-source community to build a robust and interoperable AI ecosystem.