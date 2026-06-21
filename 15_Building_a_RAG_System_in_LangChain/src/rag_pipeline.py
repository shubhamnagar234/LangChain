from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)
from langchain_core.output_parsers import StrOutputParser

# Import Gemini counterparts
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

# If using OpenAIEmbeddings and ChatOpenAI
# from langchain_openai import OpenAIEmbeddings, ChatOpenAI


def format_docs(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)


def generate_rag_answer(transcript, question):
    # Notebook Step 1b: Text Splitting
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript])

    # Step 1c & 1d: Embedding Generation and Vector Store

    # If using OpenAIEmbeddings and ChatOpenAI
    # embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-001")
    vector_store = FAISS.from_documents(chunks, embeddings)

    # Step 2: Retrieval
    retriever = vector_store.as_retriever(
        search_type="similarity", search_kwargs={"k": 4}
    )

    # Step 3: Augmentation (LLM & Prompt)

    # If using OpenAIEmbeddings and ChatOpenAI
    # llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

    prompt = PromptTemplate(
        template="""
          You are a helpful assistant.
          Answer ONLY from the provided transcript context.
          If the context is insufficient, just say you don't know.

          {context}
          Question: {question}
        """,
        input_variables=["context", "question"],
    )

    # Step 4: Building the Chain
    parallel_chain = RunnableParallel(
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough(),
        }
    )

    parser = StrOutputParser()

    main_chain = parallel_chain | prompt | llm | parser

    # Execute the chain
    return main_chain.invoke(question)
