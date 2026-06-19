# 1. Load Directory code
# from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# loader = DirectoryLoader(
#     path='books',
#     glob='*.pdf',
#     loader_cls=PyPDFLoader
# )

# docs = loader.lazy_load()

# for document in docs:
#     print(document.metadata)

# 2. Summarize code

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Load PDFs from folder
loader = DirectoryLoader(path="books", glob="*.pdf", loader_cls=PyPDFLoader)

docs = loader.load()

# Gemini Model
llm = GoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    template="""
    Summarize the following document:

    {text}
    """,
    input_variables=["text"],
)

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"text": docs[0].page_content})

print(result)
