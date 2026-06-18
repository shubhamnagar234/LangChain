from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
)
from dotenv import load_dotenv

load_dotenv()

# Gemini Model
model = GoogleGenerativeAI(model="gemini-2.5-flash")

# Prompt 1: Joke Generation
prompt1 = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

# Prompt 2: Joke Explanation
prompt2 = PromptTemplate(
    template="Explain the following joke:\n{text}", input_variables=["text"]
)

parser = StrOutputParser()

# Chain 1: Generate Joke
joke_gen_chain = RunnableSequence(prompt1, model, parser)

# Chain 2: Run in Parallel
parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explanation": RunnableSequence(prompt2, model, parser),
    }
)

# Final Chain
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# Execute
result = final_chain.invoke({"topic": "cricket"})

print("Joke:")
print(result["joke"])

print("\nExplanation:")
print(result["explanation"])

final_chain.get_graph().print_ascii()

