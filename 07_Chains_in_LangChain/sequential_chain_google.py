from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.5-flash")

# Prompt 1 : Explanation
explaination_prompt = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

# Prompt 2 : Summary
summary_prompt = PromptTemplate(
   template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = explaination_prompt | llm | parser | summary_prompt | llm | parser

result = chain.invoke({"topic": "Generative AI"})
# print(result)

chain.get_graph().print_ascii()