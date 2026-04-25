import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))
print(os.getenv("LANGCHAIN_API_KEY"))
print(os.getenv("LANGCHAIN_TRACING_V2"))
print(os.getenv("LANGCHAIN_ENDPOINT"))
print(os.getenv("LANGCHAIN_PROJECT"))

async def main():
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    asyncio.run(main())
