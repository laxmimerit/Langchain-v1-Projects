## What is the history and evolution of MCP?

### Focused Query 1: MCP protocol history
The Model Context Protocol (MCP) emerged from a need to standardize how AI systems, particularly Large Language Models (LLMs), interact with external tools and data sources. Before MCP, integrating AI models with external functionalities was a fragmented and inefficient process, often requiring custom-built connectors for each unique integration. This led to a "M×N integration problem" where M AI agents and N tools required M×N bespoke integrations.

The precursor to MCP was the **Model Object Protocol (MOP)**, a foundational concept that allowed AI models to interact with structured "objects" in their environment. MOP aimed to standardize AI access to external data, simplify tool usage with predictable schemas, and enable consistent communication. However, MOP's rigid design proved insufficient for the evolving needs of AI models, which required more flexibility and real-time context.

The limitations of MOP directly led to the birth of the **Model Context Protocol (MCP)**. Anthropic formally introduced MCP as an open standard for model-to-tool communication in **late 2024 (specifically November 2024)**. The goal was to create a universal, open, and model-agnostic protocol that any AI model, regardless of vendor, could understand and use, building a "smart layer above APIs" to help models use tools intelligently.

### Focused Query 2: When was MCP developed?
The Model Context Protocol (MCP) was formally introduced and open-sourced by **Anthropic in November 2024**. The protocol was developed at Anthropic by David Soria Parra and Justin Spahr-Summers. Its development was a direct response to the challenges faced in connecting AI systems to diverse data sources and legacy systems, aiming to replace fragmented, custom integrations with a single, unified standard.

Following its initial release by Anthropic, major AI providers quickly adopted MCP. OpenAI officially integrated MCP support into its products, including the ChatGPT desktop app and its Agents SDK, in **March 2025**. Google DeepMind, led by CEO Demis Hassabis, confirmed MCP support for upcoming Gemini models and related infrastructure in **April 2025**. Microsoft also introduced MCP support in its Copilot Studio platform in **May 2025**, and AWS integrated MCP support into its AI offerings in the same month.

### Focused Query 3: MCP major versions evolution
The Model Context Protocol has undergone several significant revisions since its initial release, reflecting continuous efforts to enhance its capabilities, security, and interoperability. As of mid-2025, three major versions are notable:

*   **2024-11-05 (Initial Release):**
    *   This was the foundational version, establishing the core architecture and message format.
    *   It introduced key concepts like tools, resources, and prompts.
    *   Features included `ProgressNotification` and sampling.
    *   For streaming transport, it utilized HTTP with Server-Sent Events (SSE).

*   **2025-03-26:**
    *   Introduced a structured OAuth 2.1-style authorization framework, significantly improving security and standardization of access control.
    *   Replaced SSE with a more robust and proxy-friendly **Streamable HTTP** transport, enabling full-duplex communication over a single connection.
    *   Temporarily added JSON-RPC batching, allowing multiple requests in a single payload (though this was later removed).
    *   Introduced tool annotations (e.g., `read-only`, `destructive`) to better describe tool behavior.
    *   Added support for audio content, more descriptive progress messages, and completions capability.

*   **2025-06-18:**
    *   A significant refinement that **removed JSON-RPC batching**, simplifying protocol implementation.
    *   Introduced **structured tool output**, allowing tools to return predictable data formats.
    *   Classified MCP servers as OAuth Resource Servers and mandated Resource Indicators for enhanced security.
    *   Added **elicitation** for server-initiated user requests, enabling servers to ask users for additional information during interactions.
    *   Introduced resource links within tool results for better integration between tool outputs and data sources.
    *   Required the `MCP-Protocol-Version` header for HTTP requests to facilitate version negotiation.
    *   Added `title` fields to tools, resources, and prompts for improved user experience in client interfaces.

### Focused Query 4: MCP historical context
MCP emerged in a landscape where AI models were rapidly advancing in reasoning but were isolated from real-world data and tools. Prior attempts to bridge this gap included:

*   **OpenAI's 2023 "function-calling" API and ChatGPT plugin framework:** These allowed models to call external APIs defined by OpenAPI schemas. While a step forward, they were often platform-specific, limited to one-off calls, and tightly controlled by OpenAI. MCP aimed for a more open, unified, and platform-agnostic framework.
*   **LangChain and other agent frameworks (2022–2023):** These libraries allowed developers to define "Tools" in code for LLM agents. While effective within their frameworks, MCP is a broader protocol standard for live network services. LangChain now provides adapters to integrate MCP servers as LangChain tools.
*   **Retrieval-Augmented Generation (RAG):** RAG enhances LLMs by injecting retrieved documents into prompts. MCP complements RAG by providing an explicit mechanism for models to decide when to call a `search_documents` tool and retrieve specific information on demand, rather than relying solely on preloaded context.
*   **Agent2Agent (A2A) protocol (Google, April 2025):** While MCP focuses on agent-to-tool interaction, A2A is designed for agent-to-agent communication. Google explicitly positions A2A as complementary to MCP, endorsing MCP for agent-to-tool interactions.

The historical context highlights that MCP's development was a natural evolution driven by the growing need for robust, scalable, and standardized interoperability between increasingly capable AI models and the vast ecosystem of external data and services. Its open-source nature and rapid adoption by key industry players underscore its significance in addressing a critical bottleneck in AI development.

### Summary
The Model Context Protocol (MCP) originated from the limitations of earlier, fragmented approaches to connecting AI models with external systems, notably the Model Object Protocol (MOP). Developed and open-sourced by Anthropic in November 2024, MCP was designed as a universal, open standard to enable AI agents to interact with tools, data, and prompts in a consistent, flexible, and context-aware manner. It addresses the "M×N integration problem" by providing a standardized client-server architecture, simplifying how AI models access external functionalities.

Since its inception, MCP has seen rapid adoption across the AI industry, with major players like OpenAI, Google DeepMind, Microsoft, and AWS integrating it into their platforms by early to mid-2025. The protocol has evolved through several key versions (2024-11-05, 2025-03-26, and 2025-06-18), introducing advancements such as structured OAuth 2.1 authorization, the transition from SSE to Streamable HTTP for more robust communication, structured tool outputs, and mechanisms for server-initiated user requests (elicitation).

Historically, MCP builds upon and improves upon prior art like OpenAI's function-calling and ChatGPT plugins, as well as frameworks like LangChain, by offering a more open, platform-agnostic, and bidirectional communication standard. It complements other emerging protocols like Google's Agent2Agent (A2A) by focusing specifically on the crucial agent-to-tool interaction layer. MCP's evolution demonstrates a clear industry trend towards establishing foundational, open standards to foster interoperability, scalability, and security in the rapidly expanding AI ecosystem.