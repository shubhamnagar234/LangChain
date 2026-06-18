from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

from dotenv import load_dotenv
load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

# Prompt 1: Facts
fact_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Give five interesting short facts about: {topic}"
)

# Prompt 2: Definition
definition_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Give a concise definition of: {topic}"
)

# Prompt 3: Use Case
usecase_prompt = PromptTemplate(
    input_variables=["topic"],
    template="What is a real-world use case of: {topic}?"
)

# Run all chains in parallel
parallel_chain = RunnableParallel({
    "facts": fact_prompt | llm | parser,
    "definition": definition_prompt | llm | parser,
    "use_case": usecase_prompt | llm | parser
})

# Invoke parallel chain
result = parallel_chain.invoke({"topic": "Artificial Intelligence"})

# print(type(result))
# print(result)
# print("\n📌 Facts:\n", result["facts"])
# print("\n📘 Definition:\n", result["definition"])
# print("\n🛠️ Use Case:\n", result["use_case"])
parallel_chain.get_graph().print_ascii()