## What are the key architectural components and technical specifications of MCP?

### Focused Query 1: MCP Architecture Components (Client, Server, Host)
The Model Context Protocol (MCP) follows a clear **Client-Host-Server** architecture designed to standardize how AI models interact with external data and tools.

*   **MCP Server**: A lightweight service that exposes specific capabilities to the AI. It does not contain the AI model itself. Instead, it provides:
    *   **Resources**: Read-only data that the AI can access (e.g., files, database rows, API responses). These are often likened to "GET" requests.
    *   **Prompts**: Pre-defined templates or instructions that help the AI use the server effectively.
    *   **Tools**: Executable functions that the AI can invoke to perform actions (e.g., "search_web", "query_database"). These are like "POST" requests.
*   **MCP Client**: The AI application (e.g., Claude Desktop, cursor, or a custom agent) that maintains the connection to the server. The client is responsible for:
    *   Discovering available capabilities (handshake).
    *   Routing the AI's "intent" to the appropriate server tool.
    *   Managing the sampling loop (asking the LLM to generate completions based on server data).
*   **MCP Host**: The runtime environment where the client operates. It manages the lifecycle of the connection and security boundaries.

### Focused Query 2: Technical Specifications (JSON-RPC 2.0)
At its core, MCP is a wire protocol built on top of **JSON-RPC 2.0**. This ensures a stateless, language-agnostic message format.

*   **Message Types**:
    *   **Requests**: Client-to-Server (or Server-to-Client) messages expecting a response. Must include a unique `id`. Example: `tools/call`.
    *   **Responses**: The reply to a request, containing either a `result` object or an `error` object. Must match the request `id`.
    *   **Notifications**: One-way messages that do not expect a response (no `id`). Used for logging, progress updates, or resource change alerts.
*   **Schema**: The protocol is strictly typed using TypeScript schemas, ensuring reliable contract enforcement between clients and servers.

### Focused Query 3: Transport Mechanisms (Stdio, SSE, Streamable HTTP)
MCP defines specific transport layers to handle communication in different environments:

*   **Stdio (Standard Input/Output)**:
    *   **Use Case**: Local integrations where the client spawns the server as a subprocess (e.g., Claude Desktop running a local git tool).
    *   **Mechanism**: Messages are sent via `stdin` and `stdout`.
    *   **Pros**: Secure by default (local process isolation), low latency, zero network configuration.
*   **Server-Sent Events (SSE) - Legacy/Compatible**:
    *   **Use Case**: Remote connections over HTTP.
    *   **Mechanism**: Uses an HTTP GET connection for server-to-client streams (events) and a separate HTTP POST endpoint for client-to-server messages.
*   **Streamable HTTP (Modern Standard)**:
    *   **Use Case**: The recommended standard for new remote servers.
    *   **Mechanism**: Uses a single HTTP endpoint. Supports standard POST requests for interactions, simplifying deployment behind load balancers and proxies compared to the dual-channel SSE approach.

### Summary
The Model Context Protocol (MCP) is a **JSON-RPC 2.0** based standard that decouples AI models from their integrations. Its architecture consists of **Clients** (AI apps), **Servers** (Capability providers), and **Hosts**. It supports flexible transport layers: **Stdio** for secure local connections and **Streamable HTTP** for scalable remote deployments. Key primitives include **Resources** (data), **Prompts** (context), and **Tools** (actions), enabling a standardized "USB-C for AI" ecosystem where any model can plug into any tool without custom glue code. Recently, **OAuth 2.0** support was added to standardize authentication for remote servers.
