from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

llm = GoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Explain the following joke:\n{text}", input_variables=["text"]
)

chain = RunnableSequence(prompt1, llm, parser, prompt2, llm, parser)

result = chain.invoke({"topic": "AI"})
print(result)

chain.get_graph().print_ascii()
