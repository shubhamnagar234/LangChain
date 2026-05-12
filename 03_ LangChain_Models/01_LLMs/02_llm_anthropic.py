from langchain_anthropic import AnthropicLLM
from dotenv import load_dotenv

load_dotenv()

llm = AnthropicLLM(model="claude-2")

result = llm.invoke("What is the capital of India?")

print(result)
