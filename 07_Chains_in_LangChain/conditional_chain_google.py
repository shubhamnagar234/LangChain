from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch
from dotenv import load_dotenv
load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

# Prompt 1 : Summary
summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text briefly:\n\n{text}"
)

# Prompt 2 : Extend
extend_prompt = PromptTemplate(
    input_variables=["text"],
    template="Extend the idea in the following long text:\n\n{text}"
)

# Chain 1 : Summary
summary_chain = summary_prompt | llm | parser

# Chain 2 : Extend
extend_chain = extend_prompt | llm | parser

def is_long_text(input: dict) -> bool:
    return len(input["text"].split()) > 50

conditional_chain = RunnableBranch(
    (lambda x: is_long_text(x), summary_chain),
    extend_chain 
)

text_input = {
    "text": "Machine learning is a field of artificial intelligence that uses statistical techniques to give computer systems the ability to learn from data."
}

result = conditional_chain.invoke(text_input)

# print("\nOutput:\n")
# print(result)

conditional_chain.get_graph().print_ascii()