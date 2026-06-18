# Runnables in LangChain

## What are Runnables in LangChain

- Runnables in LangChain provide a structured and modular way to define, execute, and manage tasks within a pipeline. They encapsulate various components such as models, tools, chains, and custom logic, making them reusable and composable. This feature is particularly useful for building complex workflows, as it allows developers to break down tasks into smaller, manageable units.

## Basics of Runnable

- A runnable in LangChain is like a common plug that lets different parts of our AI system work together easily. Whether it’s a prompt, a language model, a retriever, or something else — if it’s runnable, it can connect and talk to other parts smoothly and predictably.

- This setup is helpful because it saves time and effort. Instead of writing new code every time you want components to work together, you can just link them like building blocks. The main idea is to make it easier for developers to build and manage AI workflows without needing to worry about the details of how each part runs.

- So in conclusion, we can say that runnable provides methods that help in easy interaction between different LangChain components. But this is exactly what Chains do. Then what is the need for Runnable?

## Need of Runnable

- **Integration of Components**: LangChain allows us to seamlessly integrate various components required for building applications using language models, such as prompt templates, parsers, and retrievers.
- **Standardization**: It standardizes the way different components interact with one another. With the introduction of runnable, it ensures that all components follow the same set of rules and can easily connect, which simplifies the development process.
- **Flexibility**: We can create complex workflows with ease by connecting different runnable components. This enables the building of complex applications while keeping the underlying codebase manageable.
- **Support for Different Workflows**: It supports various workflows such as sequential, parallel, and conditional executions, which cater to diverse application requirements.

## Different Types of Chains

| Chain Name                                       | Description                                                          |
| ------------------------------------------------ | -------------------------------------------------------------------- |
| **LLMChain**                                     | Basic chain that calls an LLM with a prompt template.                |
| **SequentialChain**                              | Chains multiple LLM calls in a specific sequence.                    |
| **SimpleSequentialChain**                        | A simplified version of SequentialChain for easier use.              |
| **ConversationalRetrievalChain**                 | Handles conversational Q&A with memory and retrieval.                |
| **RetrievalQA**                                  | Fetches relevant documents and uses an LLM for question-answering.   |
| **RouterChain**                                  | Directs user queries to different chains based on intent.            |
| **MultiPromptChain**                             | Uses different prompts for different user intents dynamically.       |
| **HydeChain (Hypothetical Document Embeddings)** | Generates hypothetical answers to improve document retrieval.        |
| **AgentExecutorChain**                           | Orchestrates different tools and actions dynamically using an agent. |
| **SQLDatabaseChain**                             | Connects to SQL databases and answers natural language queries.      |
