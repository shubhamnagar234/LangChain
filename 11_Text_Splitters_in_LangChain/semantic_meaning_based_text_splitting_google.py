from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-004"
)

text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)

sample = """
Generative AI is transforming the way people create content. It can generate text, images, code, audio, and videos with remarkable quality. Large language models learn patterns from massive datasets and use that knowledge to produce human-like responses. Businesses use Generative AI for chatbots, content creation, software development, and customer support.

Cricket is one of the most popular sports in the world. It is played between two teams of eleven players and has formats such as Test matches, One Day Internationals, and T20s. Major tournaments like the ICC Cricket World Cup and the Indian Premier League attract millions of fans globally. Cricket is known for its rich history, strategy, and passionate fan base.
"""

docs = text_splitter.create_documents([sample])

print("Number of Chunks:", len(docs))

for i, doc in enumerate(docs, start=1):
    print(f"\nChunk {i}")
    print("-" * 50)
    print(doc.page_content)