# 1. Load PDF code
# from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader('ML-Course-Syllabus.pdf')

# docs = loader.load()

# print(len(docs))

# print(docs[0].page_content)
# print(docs[1].metadata)

# 2. Summarize code

from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Load PDF
loader = PyPDFLoader("ML-Course-Syllabus.pdf")
docs = loader.load()

# Gemini Model
llm = GoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Prompt
prompt = PromptTemplate(
    template="Write a summary of the following text:\n\n{text}",
    input_variables=["text"]
)

# Parser
parser = StrOutputParser()

# Chain
chain = prompt | llm | parser

# Summarize first page
result = chain.invoke({
    "text": docs[0].page_content
})

print(result)