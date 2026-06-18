from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

# Load the LLM (GPT 4o-mini)
llm = OpenAI(model_name="gpt-4o-mini", temperature=0.7)

# Create a Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about  {topic}.",
)

# Create a Chain
chain = LLMChain(llm=llm, prompt=prompt)

# Define the input
topic = input("Enter the topic: ")

# Run the Chain with a specific topic
output = chain.run(topic)

# Print the output
print("Generated Blog Title: ", output)
