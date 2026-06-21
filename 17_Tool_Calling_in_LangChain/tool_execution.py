# If using ChatOpenAI
# # from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

# tool create


@tool
def multiply(a: int, b: int) -> int:
    """Given 2 numbers a and b this tool returns their product"""
    return a * b


print(multiply.invoke({"a": 3, "b": 4}))

# tool binding
# If using ChatOpenAI
# llm = ChatOpenAI()

# If using GoogleGenerativeAIEmbeddings
# Initialize ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI()

# print(llm.invoke("hi"))

llm_with_tools = llm.bind_tools([multiply])

# tool calling
print(llm_with_tools.invoke("Hi how are you").tool_calls[0])

query = HumanMessage("can you multiply 3 with 1000")

messages = [query]
# print(messages)

result = llm_with_tools.invoke(messages)

messages.append(result)
print(messages)

tool_result = multiply.invoke(result.tool_calls[0])
print(tool_result)

messages.append(tool_result)
print(messages)

print(llm_with_tools.invoke(messages).content)
