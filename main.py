import asyncio
from dotenv import load_dotenv
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

load_dotenv()

llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python",
    args=["D:\\workspace\\mcp-servers\\mcp-crash-courseservers\\math_server.py"],
)

async def main():
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    asyncio.run(main())
