from langchain_text_splitters import CharacterTextSplitter

text = """
Generative AI is transforming the way people create content.
It can generate text, images, code, audio, and videos with remarkable quality.
Large language models learn patterns from massive datasets and use that knowledge to produce human-like responses.
Businesses use Generative AI for chatbots, content creation, software development, and customer support.
"""

splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=0, separator="")

result = splitter.split_text(text)

print(result)
