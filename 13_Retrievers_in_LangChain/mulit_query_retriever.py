# If using OpenAIEmbeddings and ChatOpenAI
# from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv

load_dotenv()

# Relevant health & wellness documents
all_docs = [
    Document(
        page_content="Regular walking boosts heart health and can reduce symptoms of depression.",
        metadata={"source": "H1"},
    ),
    Document(
        page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.",
        metadata={"source": "H2"},
    ),
    Document(
        page_content="Deep sleep is crucial for cellular repair and emotional regulation.",
        metadata={"source": "H3"},
    ),
    Document(
        page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.",
        metadata={"source": "H4"},
    ),
    Document(
        page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.",
        metadata={"source": "H5"},
    ),
    Document(
        page_content="The solar energy system in modern homes helps balance electricity demand.",
        metadata={"source": "I1"},
    ),
    Document(
        page_content="Python balances readability with power, making it a popular system design language.",
        metadata={"source": "I2"},
    ),
    Document(
        page_content="Photosynthesis enables plants to produce energy by converting sunlight.",
        metadata={"source": "I3"},
    ),
    Document(
        page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.",
        metadata={"source": "I4"},
    ),
    Document(
        page_content="Black holes bend spacetime and store immense gravitational energy.",
        metadata={"source": "I5"},
    ),
]

# If using OpenAIEmbeddings
# Initialize OpenAI Embedding Model
# embedding_model = OpenAIEmbeddings()

# If using GoogleGenerativeAIEmbeddings
# Initialize Gemini Embedding Model
embedding_model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# Create FAISS Vector Store
vectorstore = FAISS.from_documents(documents=all_docs, embedding=embedding_model)

# Similarity Retriever
similarity_retriever = vectorstore.as_retriever(
    search_type="similarity", search_kwargs={"k": 5}
)

# If using ChatOpenAI
# Initialize OpenAI LLM
# llm = ChatOpenAI(model="gpt-4o-mini")


# If using ChatGoogleGenerativeAI
# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Multi Query Retriever
multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    llm=llm,
)

# Query
query = "How to improve energy levels and maintain balance?"

# Retrieve Results
similarity_results = similarity_retriever.invoke(query)
multiquery_results = multiquery_retriever.invoke(query)

print("SIMILARITY RETRIEVER RESULTS")
print("=" * 80)

for i, doc in enumerate(similarity_results, start=1):
    print(f"\n--- Result {i} ---")
    print(doc.page_content)

print("\n" + "*" * 150)

print("\nMULTI QUERY RETRIEVER RESULTS")
print("=" * 80)

for i, doc in enumerate(multiquery_results, start=1):
    print(f"\n--- Result {i} ---")
    print(doc.page_content)
