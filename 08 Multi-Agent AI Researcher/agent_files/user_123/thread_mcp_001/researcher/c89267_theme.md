## What are the key architectural components, protocols, and technical standards of MCP?

### Focused Query 1: Model Context Protocol (MCP) architectural components overview
The Model Context Protocol (MCP) follows a **Client-Host-Server** architecture designed to decouple AI applications from the data sources they use.

*   **MCP Host:** The main application (e.g., Claude Desktop, IDEs like Cursor) that orchestrates the AI experience. It manages multiple clients, handles security/consent, and integrates LLM outputs with server-provided context.
*   **MCP Client:** A connector within the Host that maintains a **1:1 stateful session** with a specific server. It handles the low-level communication and protocol negotiation.
*   **MCP Server:** A lightweight service (local or remote) that exposes specific data or functionality. Servers are highly composable and isolated, meaning they cannot see other servers' data or the full chat history unless explicitly shared.

### Focused Query 2: MCP technical specification protocol standards
MCP is built on **JSON-RPC 2.0**, a stateless, light-weight remote procedure call (RPC) protocol.

*   **Message Types:**
    *   **Requests:** Bidirectional messages requiring a response (must include a unique ID).
    *   **Responses:** The result or error matching a Request ID.
    *   **Notifications:** One-way messages for status updates or events (no ID, no response required).
*   **Stateful Sessions:** Unlike standard REST APIs, MCP maintains a stateful connection where capabilities are negotiated at the start of the session.
*   **Capability Negotiation:** During the `initialize` phase, the client and server exchange "capabilities" (e.g., `resources`, `tools`, `prompts`, `sampling`). This ensures that both sides know exactly what features are available for that specific session.

### Focused Query 3: MCP client-server architecture communication protocols
The protocol is transport-agnostic but defines two primary standard transport mechanisms:

*   **Standard Input/Output (stdio):** Primarily for **local** resources. The Host launches the MCP Server as a child process. Communication happens via `stdin` (input) and `stdout` (output). This is preferred for security and speed when dealing with local file systems or databases.
*   **Server-Sent Events (SSE) / HTTP:** Primarily for **remote** or cloud-hosted resources. The server uses SSE to stream updates to the client and a standard HTTP POST endpoint for the client to send messages back.
*   **Emerging Standards:** Recent developments include a "Streamable HTTP" specification intended for serverless environments (e.g., Vercel, AWS Lambda) where long-lived connections aren't feasible.

### Focused Query 4: MCP data formats and integration standards
MCP provides three fundamental "primitives" for context integration:

*   **Resources (URI-based):** Standardized way to provide raw data (files, database rows, API responses) to the AI.
*   **Tools (Function Calling):** Standardized schema for the AI to trigger actions (running code, posting to Slack).
*   **Prompts (Templates):** Standardized way for servers to provide "system instructions" or pre-defined message templates to the Host.
*   **Advanced Capabilities:**
    *   **Sampling:** Allows a Server to request the Host to get a completion from the LLM.
    *   **Roots:** Allows a Host to define the filesystem boundaries the Server is allowed to access.

### Summary
The Model Context Protocol architecture is a modular, stateful system based on **JSON-RPC 2.0**. It uses a **Host-Client-Server** model to solve the integration bottleneck in AI development. By standardizing communication through **stdio** and **SSE** transports and defining core primitives (**Resources, Tools, Prompts**), MCP acts as a "USB-C" interface for the AI ecosystem, allowing any model to connect to any data source through a unified technical standard.
