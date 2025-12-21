## Technical Architecture of the Model Context Protocol (MCP)

The Model Context Protocol (MCP) employs a modular, client-server architecture designed to standardize the connection between AI applications (Hosts) and external data sources or tools (Servers). This architecture decouples the AI model from the specific implementations of external integrations, allowing for a "plug-and-play" ecosystem.

### 1. Core Architectural Components

The MCP architecture is built around three primary participants that interact in a strict hierarchy:

*   **MCP Host**:
    *   **Definition**: The user-facing application that integrates and runs the MCP system (e.g., Claude Desktop, Cursor, VS Code, or an AI IDE).
    *   **Role**: It provides the runtime environment for the LLM and the user interface. It is responsible for discovery and lifecycle management of the servers.
    *   **Function**: The Host orchestrates the connection. When a user prompts the application, the Host determines if an external tool is needed and routes the request through the Client to the appropriate Server.

*   **MCP Client**:
    *   **Definition**: The protocol client implementation embedded within the Host application.
    *   **Role**: It maintains a **1:1 connection** with a specific MCP Server.
    *   **Function**: It acts as the bridge/translator. It converts the Host's/LLM's high-level requests into the JSON-RPC 2.0 format required by the protocol and manages the state of the connection (handshakes, timeouts). A single Host application often instantiates multiple Clients to connect to multiple Servers simultaneously.

*   **MCP Server**:
    *   **Definition**: A standalone process or service that exposes specific capabilities (Tools, Resources, Prompts) to the Client.
    *   **Role**: It acts as the gateway to external systems (e.g., a database, a local filesystem, a Slack API, or a GitHub repository).
    *   **Function**: It listens for requests from the Client, executes the requested action (like querying a database), and returns the result. Servers are designed to be "model-agnostic"—they don't know which specific LLM is calling them.

### 2. Transport Layers

MCP defines the "Transport Layer" as the mechanism responsible for moving messages between the Client and Server. The protocol is designed to be transport-agnostic, but currently defines two standard transport mechanisms:

*   **Stdio Transport (Standard Input/Output)**:
    *   **Use Case**: Best for **local** integrations where the Server runs as a subprocess of the Host application (e.g., accessing local files).
    *   **Mechanism**: The Client spawns the Server process and communicates via `stdin` and `stdout`.
    *   **Characteristics**: High performance, low latency, secure (no network exposure), but limited to the same machine.

*   **SSE Transport (Server-Sent Events over HTTP)**:
    *   **Use Case**: Designed for **remote** or distributed integrations (e.g., connecting to a server running on a cloud platform or a different container).
    *   **Mechanism**:
        *   **Client-to-Server**: Uses standard **HTTP POST** requests for sending JSON-RPC messages (requests/notifications).
        *   **Server-to-Client**: Uses **Server-Sent Events (SSE)** to push responses and asynchronous notifications back to the Client.
    *   **Characteristics**: Scalable, standard firewall-friendly HTTP traffic, supports authentication/authorization headers, enables distributed architectures.

### 3. Protocol and Data Layer

On top of the transport layer, MCP uses **JSON-RPC 2.0** as the wire protocol for the "Data Layer." This ensures a consistent message structure regardless of the underlying transport.

*   **Message Types**:
    *   **Request**: A message expecting a response (e.g., `tools/call` or `tools/list`). Contains a unique `id`.
    *   **Response**: The reply to a specific request, containing the `result` or an `error`. Matches the request's `id`.
    *   **Notification**: A one-way message requiring no response (e.g., `notifications/tools/list_changed` or logging events).

### 4. Interaction Lifecycle

The interaction between a Client and Server follows a strict lifecycle to ensure compatibility and stability:

#### Phase 1: Initialization (Handshake)
1.  **Client sends `initialize` Request**: The Client proposes a protocol version and declares its capabilities (e.g., "I support sampling and progress notifications").
2.  **Server sends `initialize` Response**: The Server selects the protocol version and declares its own capabilities (e.g., "I have Tools and Resources, and I support list-changed notifications").
3.  **Client sends `notifications/initialized`**: A final acknowledgement that the connection is established and ready for traffic.

#### Phase 2: Discovery
Once initialized, the Client inspects the Server to learn what it can do:
*   **`tools/list`**: The Client requests the list of available executable functions (Tools) and their JSON schemas.
*   **`resources/list`**: The Client requests available data sources (Resources) that can be read.
*   **`prompts/list`**: The Client requests standard prompt templates.

#### Phase 3: Operation (Execution)
When the LLM determines it needs to take an action:
1.  **Host** identifies the correct tool.
2.  **Client** sends a **`tools/call` Request** with the arguments generated by the LLM (e.g., `{"name": "weather", "args": {"city": "Paris"}}`).
3.  **Server** executes the logic (calls the weather API) and sends a **Response** with the result (e.g., "15°C").
4.  **Host** feeds this result back to the LLM as context.

#### Phase 4: Real-time Updates
If the state of the Server changes (e.g., a file is added to a directory):
1.  **Server** sends a **Notification** (e.g., `notifications/resources/list_changed`).
2.  **Client** receives this and automatically re-fetches the list to keep the LLM's context up-to-date.

#### Phase 5: Termination
Connections can be closed gracefully (via a `close` method) or abruptly (transport failure). Both sides are expected to handle cleanup of resources upon disconnection.
