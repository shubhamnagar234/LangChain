from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableSequence,
    RunnablePassthrough,
    RunnableBranch,
)
from dotenv import load_dotenv

load_dotenv()

# Prompt 1: Report Generation
prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# Prompt 2: Summarization
prompt2 = PromptTemplate(
    template="Summarize the following text:\n{text}",
    input_variables=["text"]
)

# Gemini Model
model = GoogleGenerativeAI(
    model="gemini-2.5-flash"
)

parser = StrOutputParser()

# Report Generation Chain
report_gen_chain = prompt1 | model | parser

# Conditional Branch
branch_chain = RunnableBranch(
    (
        lambda x: len(x.split()) > 300,
        prompt2 | model | parser
    ),
    RunnablePassthrough()
)

# Final Chain
final_chain = report_gen_chain | branch_chain

# Execute
result = final_chain.invoke(
    {"topic": "Generative AI"}
)

print(result)
final_chain.get_graph().print_ascii()
