# If using OpenAIEmbeddings
# # from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(
        page_content="MMR helps you get diverse results when doing similarity search."
    ),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

# If using OpenAIEmbeddings
# Initialize embedding model
# embedding_model = OpenAIEmbeddings()

# If using GoogleGenerativeAIEmbeddings
# Initialize Gemini Embeddings
embedding_model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# Create FAISS Vector Store
vectorstore = FAISS.from_documents(documents=docs, embedding=embedding_model)

# Enable MMR Retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 3,
        "lambda_mult": 0.5,
    },
)

query = "What is LangChain?"

results = retriever.invoke(query)

for i, doc in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print(doc.page_content)
