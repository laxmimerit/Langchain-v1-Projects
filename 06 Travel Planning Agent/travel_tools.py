import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    client = MultiServerMCPClient(
        {
            "airbnb": {
                "command": "C:\\Program Files\\nodejs\\npx.cmd",  # Update this path to your npx location
                "args": ["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"],
                "transport": "stdio"
            }
        }
    )

    tools = await client.get_tools()

    print(f"Loaded {len(tools)} Tools")
    print(f"Tools Available: {tools}")


if __name__ == "__main__":
    asyncio.run(main())


