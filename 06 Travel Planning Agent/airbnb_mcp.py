"""Simple Airbnb MCP module."""
######## MCP SETUP ###############
# MCP GITHUB
# https://github.com/laxmimerit/MCP-Mastery-with-Claude-and-Langchain
# https://github.com/langchain-ai/langchain-mcp-adapters

from langchain_ollama import ChatOllama

from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio


# Config
LLM_MODEL = "qwen3"
BASE_URL = "http://localhost:11434"

llm = ChatOllama(model=LLM_MODEL, base_url=BASE_URL, temperature=0)


async def get_tools():

    client = MultiServerMCPClient(
        {
            "airbnb": {
                "command": "npx",
                "args": ["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"],
                "transport": "stdio"
            }
        }
    )


    tools = await client.get_tools()

    print(f"Loaded {len(tools)} Tools")
    print(f"Tools Available: {tools}")

    return tools

async def search(query):
    tools = await get_tools()
    agent = create_agent(model=llm, tools=tools)
    result = await agent.ainvoke({'messages': [HumanMessage(query)]})

    response = result['messages'][-1].content

    print(response)

    return response


if __name__=="__main__":
    query = "Show me premium hotels for party in Mumbai"
    asyncio.run(search(query))