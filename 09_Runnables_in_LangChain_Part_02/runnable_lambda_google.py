from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableSequence,
    RunnableLambda,
    RunnablePassthrough,
    RunnableParallel,
)
from dotenv import load_dotenv

load_dotenv()


def word_count(text):
    return len(text.split())


# Prompt
prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

# Gemini Model
model = GoogleGenerativeAI(
    model="gemini-2.5-flash"
)

parser = StrOutputParser()

# Joke Generation Chain
joke_gen_chain = RunnableSequence(
    prompt,
    model,
    parser
)

# Parallel Processing
parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "word_count": RunnableLambda(word_count)
    }
)

# Final Chain
final_chain = RunnableSequence(
    joke_gen_chain,
    parallel_chain
)

# Execute
result = final_chain.invoke({"topic": "AI"})

final_result = "{}\n\nWord Count - {}".format(
    result["joke"],
    result["word_count"]
)

print(final_result)
final_chain.get_graph().print_ascii()