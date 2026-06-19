from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Gemini Model
model = GoogleGenerativeAI(model="gemini-2.5-flash")

# Prompt
prompt = PromptTemplate(
    template="Write a summary for the following poem:\n{poem}", input_variables=["poem"]
)

parser = StrOutputParser()

# Load Text File
loader = TextLoader("cricket.txt", encoding="utf-8")

docs = loader.load()

print(type(docs))
print(len(docs))

print("\nPage Content:\n")
print(docs[0].page_content)

print("\nMetadata:\n")
print(docs[0].metadata)

# LCEL Chain
chain = prompt | model | parser

result = chain.invoke({"poem": docs[0].page_content})

print("\nSummary:\n")
print(result)
