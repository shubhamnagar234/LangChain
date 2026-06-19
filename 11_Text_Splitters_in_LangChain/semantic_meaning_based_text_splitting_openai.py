from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)

sample = """
Generative AI is transforming the way people create content. It can generate text, images, code, audio, and videos with remarkable quality. Large language models learn patterns from massive datasets and use that knowledge to produce human-like responses. Businesses use Generative AI for chatbots, content creation, software development, and customer support.

Cricket is one of the most popular sports in the world. It is played between two teams of eleven players and has formats such as Test matches, One Day Internationals, and T20s. Major tournaments like the ICC Cricket World Cup and the Indian Premier League attract millions of fans globally. Cricket is known for its rich history, strategy, and passionate fan base.
"""

docs = text_splitter.create_documents([sample])
print(len(docs))
print(docs)


