# 1. Load CSV code
# from langchain_community.document_loaders import CSVLoader

# loader = CSVLoader(file_path='Social_Network_Ads.csv')

# docs = loader.load()

# print(len(docs))
# print(docs[1])

# 2. Summarize code

from langchain_community.document_loaders import CSVLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Load CSV
loader = CSVLoader(
    file_path="Social_Network_Ads.csv"
)

docs = loader.load()

# Gemini Model
llm = GoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt = PromptTemplate(
    template="""
    Analyze and summarize the following CSV record:

    {text}
    """,
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({
    "text": docs[0].page_content
})

print(result)