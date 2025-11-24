"""Simple Airbnb MCP module."""
######## MCP SETUP ###############
# MCP GITHUB
# https://github.com/laxmimerit/MCP-Mastery-with-Claude-and-Langchain
# https://github.com/laxmimerit/Agentic-RAG-with-LangGraph-and-Ollama

# https://github.com/langchain-ai/langchain-mcp-adapters
from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_google_genai import ChatGoogleGenerativeAI

import asyncio
import os
import sys

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

system_prompt = """
                You are a travel assistant helping users find Airbnb accommodations.

                Available Tools:
                - airbnb_search: Search for Airbnb listings (location required, optional: checkin, checkout, adults, children, infants, pets, minPrice, maxPrice)
                - airbnb_listing_details: Get detailed information about a specific listing (id required)

                Instructions:
                - ALWAYS call airbnb_search immediately when user asks for accommodations
                - Extract location from query (required), use defaults for missing info: adults=2, no dates if not mentioned
                - After getting results, present top 5 listings with: all details and direct link https://www.airbnb.com/rooms/{listing_id}
                - Be proactive - search first, don't ask for additional details unless search fails
                """

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

async def hotel_search(query):
    tools = await get_tools()
    agent = create_agent(model=llm, tools=tools, system_prompt=system_prompt)
    result = await agent.ainvoke({'messages': [HumanMessage(query)]})
    
    response = result['messages'][-1].content[0]['text']
    print(response)

    return response

if __name__=="__main__":
    query = "Show me hotels for party in Mumbai"
    asyncio.run(hotel_search(query))