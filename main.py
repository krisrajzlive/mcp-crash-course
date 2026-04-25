import asyncio
from dotenv import load_dotenv
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

load_dotenv()

def build_llm() -> ChatOpenAI:
    provider = os.getenv("LLM_PROVIDER", "llama").lower()

    if provider == "llama":
        # Works with OpenAI-compatible Llama endpoints (e.g., Ollama's /v1 API).
        return ChatOpenAI(
            model=os.getenv("LLAMA_MODEL", "llama3.2:3b"),
            base_url=os.getenv("LLAMA_BASE_URL", "http://localhost:11434/v1"),
            api_key=os.getenv("LLAMA_API_KEY", "ollama"),
        )

    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        api_key=os.getenv("OPENAI_API_KEY"),
    )


llm = build_llm()

stdio_server_params = StdioServerParameters(
    command="python",
    args=[os.path.join(os.path.dirname(__file__), "servers", "math_server.py")],
)

async def main():
    async with stdio_client(stdio_server_params) as (read,write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)
            agent = create_agent(llm, tools)

            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 2 + 2?")]})
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
