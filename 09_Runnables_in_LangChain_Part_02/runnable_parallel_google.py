from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

# Gemini Model
model = GoogleGenerativeAI(model="gemini-2.5-flash")

# Prompt 1: Tweet
prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}", input_variables=["topic"]
)

# Prompt 2: LinkedIn Post
prompt2 = PromptTemplate(
    template="Generate a LinkedIn post about {topic}", input_variables=["topic"]
)

parser = StrOutputParser()

# Individual Chains
tweet_chain = RunnableSequence(prompt1, model, parser)

linkedin_chain = RunnableSequence(prompt2, model, parser)

# Parallel Chain
parallel_chain = RunnableParallel(
    {
        "tweet": tweet_chain,
        "linkedin": linkedin_chain,
    }
)

# Execute
result = parallel_chain.invoke({"topic": "AI"})

print("Tweet:\n")
print(result["tweet"])

print("\nLinkedIn Post:\n")
print(result["linkedin"])

parallel_chain.get_graph().print_ascii()
