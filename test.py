
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OpenRouter API key not found!")

llm = ChatOpenRouter(
    model=os.getenv("MODEL_NAME", "openai/gpt-4o-mini"),
    api_key=api_key,
    temperature=0
)

response = llm.invoke(
    "Explain LangChain in one sentence."
)

print("\nOpenRouter API connected successfully!")
print(response.content)
