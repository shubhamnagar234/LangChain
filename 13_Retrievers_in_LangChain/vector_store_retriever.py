# If using OpenAIEmbeddings
# from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(
        page_content="Chroma is a vector database optimized for LLM-based search."
    ),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="Google provides powerful embedding models through Gemini."),
]

# If using OpenAIEmbeddings
# Step 2: Initialize OpenAI Embedding Model
# embedding_model = OpenAIEmbeddings()

# If using GoogleGenerativeAIEmbeddings
# Step 2: Initialize Gemini Embedding Model
embedding_model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# Step 3: Create Chroma Vector Store
vectorstore = Chroma.from_documents(
    documents=documents, embedding=embedding_model, collection_name="my_collection"
)

# Step 4: Convert Vector Store into a Retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

query = "What is Chroma used for?"

# Retriever Search
results = retriever.invoke(query)

print("Retriever Results:")
for i, doc in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print(doc.page_content)

# Similarity Search
results = vectorstore.similarity_search(query, k=2)

print("\n\nSimilarity Search Results:")
for i, doc in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print(doc.page_content)
