from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# Create LangChain documents for IPL players
doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
    metadata={"team": "Royal Challengers Bangalore"},
)

doc2 = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
    metadata={"team": "Mumbai Indians"},
)

doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
    metadata={"team": "Chennai Super Kings"},
)

doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
    metadata={"team": "Mumbai Indians"},
)

doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
    metadata={"team": "Chennai Super Kings"},
)

docs = [doc1, doc2, doc3, doc4, doc5]

# Gemini Embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# Chroma Vector Store
vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory="my_chroma_db",
    collection_name="sample",
)

# Add Documents
vector_store.add_documents(docs)

# View Documents
print(vector_store.get(include=["documents", "metadatas"]))

# Similarity Search
results = vector_store.similarity_search(query="Who among these are a bowler?", k=2)

print("\nSimilarity Search:")
for doc in results:
    print(doc.page_content)

# Similarity Search With Score
results = vector_store.similarity_search_with_score(
    query="Who among these are a bowler?", k=2
)

print("\nSimilarity Search With Score:")
for doc, score in results:
    print(score, doc.page_content)

# Metadata Filtering
results = vector_store.similarity_search_with_score(
    query="", filter={"team": "Chennai Super Kings"}
)

print("\nMetadata Filter:")
for doc, score in results:
    print(score, doc.page_content)

# Update Document
updated_doc1 = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history.",
    metadata={"team": "Royal Challengers Bangalore"},
)

# Replace with actual ID from vector_store.get()
vector_store.update_document(document_id="YOUR_DOCUMENT_ID", document=updated_doc1)

# View Updated Documents
print(vector_store.get(include=["documents", "metadatas"]))

# Delete Document
vector_store.delete(ids=["YOUR_DOCUMENT_ID"])

# View Remaining Documents
print(vector_store.get(include=["documents", "metadatas"]))
