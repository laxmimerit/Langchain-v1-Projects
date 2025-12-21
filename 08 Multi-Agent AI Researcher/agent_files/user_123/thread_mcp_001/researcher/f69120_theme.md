## What is the history of MCP, who created it, and how has it evolved over time?

### Focused Query 1: MCP Creators and Origin Story
**Creators:**
- **David Soria Parra** and **Justin Spahr-Summers** at **Anthropic**.
- The protocol was born out of frustration with the "M × N" integration problem: every AI application (M) needed a unique connector for every data source (N).
- Development began around **July 2024**. The creators were heavily inspired by the **Language Server Protocol (LSP)**, which had successfully standardized how IDEs communicate with programming languages. They applied similar "client-server" and "capability negotiation" principles to AI context.

**Key Motivation:**
- Before MCP, developers at Anthropic (and elsewhere) had to manually copy-paste context between tools (e.g., from a terminal to Claude) or build brittle, one-off integrations.
- An internal hackathon at Anthropic (approx. October 2024) demonstrated the power of the protocol when engineers used it to build novel integrations (like controlling a 3D printer), validating the concept for public release.

### Focused Query 2: Release and Initial Launch
**Official Launch:**
- **Date:** **November 25, 2024**.
- **Scope:** Anthropic open-sourced the specification, SDKs (TypeScript, Python), and a repository of reference servers (Google Drive, Slack, GitHub, Postgres).
- **Positioning:** It was marketed as the "USB-C for AI applications"—a universal standard for connecting models to data.
- **Initial Client:** The **Claude Desktop** app was the first major application to support MCP, allowing users to connect local tools directly to the model.

### Focused Query 3: Evolution and Technical Milestones
**Adoption Wave (Early-Mid 2025):**
- **March 2025:** **OpenAI** announced adoption of MCP for the ChatGPT desktop app and Agents SDK. This effectively ended potential "standard wars" and solidified MCP as the industry choice.
- **April 2025:** **Google DeepMind** committed to supporting MCP in Gemini and related infrastructure.
- **September 2025:** The **MCP Registry** was launched to index thousands of community-built servers.

**Protocol Updates:**
- **March 2025 Spec Update:**
  - Addressed a major limitation of the initial release (which relied heavily on local `stdio` connections) by introducing **Streamable HTTP (SSE)**. This allowed for easier deployment of remote, stateless servers.
  - Introduced robust **Authorization** capabilities based on OAuth 2.1.
- **November 2025 Spec Release:**
  - **Tasks:** Added a new primitive for tracking long-running, asynchronous operations.
  - **Agentic Support:** Enabled "sampling with tools," allowing servers to act as agents themselves.
  - **Extensions:** Created a framework for experimental features without bloating the core spec.

### Focused Query 4: Governance and Standardization
**Shift to the Linux Foundation:**
- **Date:** **December 9, 2025**.
- **Event:** Anthropic donated the MCP project to the **Agentic AI Foundation (AAIF)**, a new body under the **Linux Foundation**.
- **Founding Members:** The AAIF was co-founded by **Anthropic, Block, and OpenAI**, with backing from Google, Microsoft, AWS, Cloudflare, and Bloomberg.
- **Significance:** This move marked the maturity of MCP from a single-company project to a vendor-neutral industry standard, ensuring its long-term viability and open governance.

### Summary
The Model Context Protocol (MCP) originated in **July 2024** as an internal project by **David Soria Parra** and **Justin Spahr-Summers** at **Anthropic** to solve the fragmentation of AI integrations. Officially released on **November 25, 2024**, it was designed as a "USB-C for AI," heavily inspired by the Language Server Protocol (LSP).

Its evolution was rapid:
1.  **2024:** Launch with local `stdio` support and Claude Desktop integration.
2.  **Early 2025:** Critical adoption by competitors **OpenAI** and **Google**, preventing fragmentation.
3.  **Mid-2025:** Technical evolution to support **remote HTTP** connections and better security.
4.  **Late 2025:** Expansion into **agentic workflows** and transfer of stewardship to the **Linux Foundation's Agentic AI Foundation** (Dec 9, 2025), establishing it as a neutral open standard for the entire industry.
