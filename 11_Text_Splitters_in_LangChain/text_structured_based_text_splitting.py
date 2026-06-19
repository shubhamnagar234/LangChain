from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Generative AI is transforming the way people create content.
It can generate text, images, code, audio, and videos with remarkable quality.
Large language models learn patterns from massive datasets and use that knowledge to produce human-like responses.
Businesses use Generative AI for chatbots, content creation, software development, and customer support.
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)
