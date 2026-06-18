from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

explaination_prompt = PromptTemplate(
    template="Generate a detailed report on {topic}", input_variables=["topic"]
)

summary_prompt = PromptTemplate(
    template="Generate a 5 pointer summary from the following text \n {text}",
    input_variables=["text"],
)


parser = StrOutputParser()

chain = explaination_prompt | llm | parser | summary_prompt | llm | parser

result = chain.invoke({"topic": "Generative AI"})

print(result)

chain.get_graph().print_ascii()
