from langchain_huggingface import HuggingFacePipeline
import os

os.environ["HF_HOME"] = "F:/huggingface_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"temperature": 0.5, "max_new_tokens": 100},
)

result = llm.invoke("What is the capital of India?")

print(result)
