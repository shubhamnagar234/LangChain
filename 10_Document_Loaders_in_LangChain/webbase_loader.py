from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Gemini Model
model = GoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Prompt
prompt = PromptTemplate(
    template="""
Answer the following question:

Question: {question}

Based on the following text:

{text}
""",
    input_variables=["question", "text"]
)

parser = StrOutputParser()

# URL to load
url = "https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421"

# Load webpage content
loader = WebBaseLoader(url)

docs = loader.load()

print("Number of Documents:", len(docs))
print("\nMetadata:")
print(docs[0].metadata)

# LCEL Chain
chain = prompt | model | parser

result = chain.invoke(
    {
        "question": "What is the product that we are talking about?",
        "text": docs[0].page_content
    }
)

print("\nAnswer:\n")
print(result)