# 🦜🔗 LangChain & Generative AI: From Zero to Autonomous AI Agents & Production RAG

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-v0.3+-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini%201.5%2F2.0-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Anthropic](https://img.shields.io/badge/Anthropic-Claude%203.5-D97706?style=for-the-badge&logo=anthropic&logoColor=white)](https://www.anthropic.com/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![ChromaDB](https://img.shields.io/badge/Vector%20DB-Chroma-orange?style=for-the-badge)](https://www.trychroma.com/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

An end-to-end, enterprise-ready masterclass repository covering modern **Generative AI Engineering**, **LangChain (v0.3+)**, **LangChain Expression Language (LCEL)**, **Retrieval-Augmented Generation (RAG)**, **Vector Databases**, and **Autonomous AI Agents (ReAct)** across all major foundation model providers (**OpenAI**, **Google Gemini**, **Anthropic Claude**, and **Hugging Face**).

Progressing from the mathematical and conceptual foundations of GenAI to building production-grade full-stack applications—including a **YouTube Video Transcript RAG Chatbot**, **Autonomous Tool-Calling Agents**, and **Interactive Prompt Engineering Playgrounds**.

---

## 📌 Table of Contents

- [Architectural Overview](#-architectural-overview)
- [Repository Structure](#-repository-structure)
- [19-Module Comprehensive Deep Dive](#-19-module-comprehensive-deep-dive)
  - [00. Introduction to GenAI](#00-introduction-to-genai)
  - [01. Introduction to LangChain](#01-introduction-to-langchain)
  - [02. LangChain Components](#02-langchain-components)
  - [03. LangChain Models: LLMs, Chat & Embeddings](#03-langchain-models-llms-chat--embeddings)
  - [04. Prompts in LangChain](#04-prompts-in-langchain)
  - [05. Structured Output in LangChain](#05-structured-output-in-langchain)
  - [06. Output Parsers in LangChain](#06-output-parsers-in-langchain)
  - [07. Chains in LangChain & LCEL](#07-chains-in-langchain--lcel)
  - [08. Runnables in LangChain: Part 1](#08-runnables-in-langchain-part-1)
  - [09. Runnables in LangChain: Part 2 (LCEL Primitives)](#09-runnables-in-langchain-part-2-lcel-primitives)
  - [10. Document Loaders in LangChain](#10-document-loaders-in-langchain)
  - [11. Text Splitters & Chunking Strategies](#11-text-splitters--chunking-strategies)
  - [12. Vector Stores & Chroma DB](#12-vector-stores--chroma-db)
  - [13. Retrievers & Intelligent Search](#13-retrievers--intelligent-search)
  - [14. Retrieval-Augmented Generation (RAG) Foundations](#14-retrieval-augmented-generation-rag-foundations)
  - [15. Building a Production RAG System: YouTube Chatbot](#15-building-a-production-rag-system-youtube-chatbot)
  - [16. Tools & Toolkits in LangChain](#16-tools--toolkits-in-langchain)
  - [17. Tool Calling & Function Execution](#17-tool-calling--function-execution)
  - [18. Building Autonomous AI Agents (ReAct)](#18-building-autonomous-ai-agents-react)
- [Featured Showcase Projects](#-featured-showcase-projects)
- [Technology & Integration Matrix](#-technology--integration-matrix)
- [Getting Started Locally](#-getting-started-locally)
- [Environment Configuration (.env)](#-environment-configuration-env)
- [Production Best Practices for GenAI & Agents](#-production-best-practices-for-genai--agents)
- [Contributing & License](#-contributing--license)

---

## 🏛 Architectural Overview

```
                                  ┌──────────────────────────────────────────────┐
                                  │           User & Client Application         │
                                  │   (Streamlit Web UI / CLI / REST API Client)  │
                                  └──────────────────────┬───────────────────────┘
                                                         │
                                                         ▼
                                  ┌──────────────────────────────────────────────┐
                                  │     LangChain Orchestration Engine (LCEL)     │
                                  │  - RunnableSequence (|)   - RunnableParallel │
                                  │  - RunnablePassthrough    - RunnableLambda   │
                                  │  - RunnableBranch         - Async Streaming  │
                                  └──────────┬────────────────────────┬──────────┘
                                             │                        │
                    ┌────────────────────────┴────────┐      ┌────────┴────────────────────────┐
                    ▼                                 ▼      ▼                                 ▼
      ┌──────────────────────────┐      ┌──────────────────────────┐      ┌──────────────────────────┐
      │   Prompt Engineering     │      │   RAG & Vector Engine    │      │  Agent & Tool Execution  │
      │ - ChatPromptTemplate     │      │ - Multi-source Ingestion │      │ - ReAct Reasoning Loop   │
      │ - System / Human / AI    │      │ - Semantic Chunking      │      │ - Tool Binding & Schema  │
      │ - Few-Shot Examples      │      │ - Vector Embeddings      │      │ - DuckDuckGo / Calc / API│
      │ - MessagesPlaceholder    │      │ - Chroma DB & Retrievers │      │ - Autonomous Execution   │
      └─────────────┬────────────┘      └─────────────┬────────────┘      └─────────────┬────────────┘
                    │                                 │                                 │
                    └────────────────────────┬────────┴─────────────────────────────────┘
                                             ▼
                      ┌──────────────────────────────────────────────┐
                      │          Unified Model Provider Layer        │
                      │  ┌────────────┬─────────────┬─────────────┐  │
                      │  │   OpenAI   │ Google PaLM │  Anthropic  │  │
                      │  │  (GPT-4o)  │ / Gemini 1.5│ (Claude 3.5)│  │
                      │  ├────────────┼─────────────┼─────────────┤  │
                      │  │Hugging Face│  Llama 3    │ Local Models│  │
                      │  │(Inference) │  (Groq/Oll) │ (Pipelines) │  │
                      │  └────────────┴─────────────┴─────────────┘  │
                      └──────────────────────┬───────────────────────┘
                                             ▼
                      ┌──────────────────────────────────────────────┐
                      │          Structured Output & Parsing         │
                      │   - Pydantic BaseModel Validation            │
                      │   - JsonOutputParser & StrOutputParser       │
                      │   - Type-safe, production-ready responses    │
                      └──────────────────────────────────────────────┘
```

---

## 📂 Repository Structure

```
LangChain/
├── 00_Introduction_to_GenAI/                 # GenAI principles, foundation models & engineering landscape
├── 01_Introduction_to_LangChain/             # Framework motivations, ecosystem & problem space
├── 02_LangChain_Components/                  # Core pillars: Models, Prompts, Indexes, Chains, Memory
├── 03_ LangChain_Models/                     # LLMs, ChatModels & Embeddings (OpenAI, Gemini, Claude, HF)
│   ├── 01_LLMs/                              # Text completion models
│   ├── 02_ChatModels/                        # Message-based conversational models
│   └── 03_EmbeddingModels/                   # Vector representations & document similarity
├── 04_Prompts_in_LangChain/                  # Templates, message placeholders, temperature & Streamlit UI
├── 05_Structured_Output_in_LangChain/        # with_structured_output via Pydantic, TypedDict & JSON schema
├── 06_Output_Parsers_in_LangChain/           # StrOutputParser, JsonOutputParser, PydanticOutputParser
├── 07_Chains_in_LangChain/                   # Simple, Sequential, Parallel & Conditional chains
├── 08_Runnables_in_LangChain_Part_01/        # LCEL Runnable protocol: invoke, batch, stream & notebook demos
├── 09_Runnables_in_LangChain_Part_02/        # Runnable primitives: Sequence, Parallel, Passthrough, Lambda, Branch
├── 10_Document_Loaders_in_LangChain/         # Ingesting Text, CSV, PDF, Web pages & entire directories
├── 11_Text_Splitters_in_LangChain/           # Character, Recursive, Markdown, Code & Semantic text splitting
├── 12_Vector_Stores_in_LangChain/            # Vector store theory, Chroma DB indexing & similarity search
├── 13_Retrievers_in_LangChain/               # VectorStore, Wikipedia, MultiQuery, ContextualCompression, MMR
├── 14_Retrieval_Augmented_Generation(RAG)/   # RAG architecture: Ingestion, Chunking, Embedding, Generation
├── 15_Building_a_RAG_System_in_LangChain/    # Full-Stack YouTube Transcript RAG Chatbot (Streamlit + Chroma)
│   ├── app.py                                # Streamlit frontend
│   └── src/                                  # RAG pipeline & YouTube transcript extraction
├── 16_Tools_in_LangChain/                    # Built-in tools, @tool decorator, StructuredTool & Toolkits
├── 17_Tool_Calling_in_LangChain/             # bind_tools, schema binding, tool execution & Currency Converter
├── 18_AI_Agent_in_LangChain/                 # Autonomous ReAct Agent & AgentExecutor workflows
├── .gitignore                                # Exclusions for venv, env files, checkpoints, chroma DB
├── LICENSE                                   # MIT License
├── README.md                                 # Master Documentation
└── requirements.txt                          # Comprehensive repository dependencies
```

---

## 🔍 19-Module Comprehensive Deep Dive

### [00. Introduction to GenAI](00_Introduction_to_GenAI/)

- **Core Technology**: Generative AI, Foundation Models, Deep Learning Architectures.
- **Description**: Establishes the foundational paradigms of Generative AI, contrasting discriminative versus generative systems across text, code, imagery, and audio.
- **Key Concepts Covered**:
  - The evolution of Foundation Models (GPT, Claude, Gemini, LLaMA).
  - The AI Engineer vs. ML Engineer perspective: Moving from model training from scratch to fine-tuning, in-context learning, and application composition.
  - Generative AI impact areas: Enterprise automation, customer support, data synthesis, and code intelligence.

---

### [01. Introduction to LangChain](01_Introduction_to_LangChain/)

- **Core Technology**: LangChain Ecosystem, API Abstractions, Multi-Provider Architecture.
- **Description**: Examines the core motivations behind LangChain and why raw API calls to LLM providers fail to scale in complex enterprise software.
- **Key Concepts Covered**:
  - The fragmented landscape of proprietary LLM APIs and vendor lock-in.
  - The "AI-Powered Book Reader" case study: How simple Q&A breaks without chunking, retrieval, and contextual prompting.
  - LangChain's value proposition: Modular primitives, unified interfaces, active community ecosystem, and production tooling.

---

### [02. LangChain Components](02_LangChain_Components/)

- **Core Technology**: LangChain Core, Architectural Abstractions.
- **Description**: Comprehensive overview of the 6 core pillars that constitute the LangChain framework.
- **Key Concepts Covered**:
  - **Models**: Standardized interfaces for LLMs, Chat Models, and Text Embeddings.
  - **Prompts**: Parameterized, dynamic, and role-based prompt templates.
  - **Chains & LCEL**: Declarative composition of multi-step processing pipelines.
  - **Indexes**: Connecting LLMs to private enterprise data via Document Loaders, Splitters, and Vector Stores.
  - **Memory**: State management and conversational history retention across invocations.
  - **Agents**: Autonomous decision-making engines using LLMs as reasoning controllers.

---

### [03. LangChain Models: LLMs, Chat & Embeddings](03_%20LangChain_Models/)

- **Core Technology**: `langchain-openai`, `langchain-google-genai`, `langchain-anthropic`, `langchain-huggingface`, Hugging Face Transformers.
- **Description**: In-depth implementation of all three primary model categories across four industry-leading providers.
- **Sub-Modules & Code**:
  - `01_LLMs/`: Text completion models (`OpenAI`, `Anthropic`, `GoogleGenerativeAI`, `HuggingFaceEndpoint`, and local Transformers pipelines).
  - `02_ChatModels/`: Message-oriented chat models (`ChatOpenAI`, `ChatAnthropic`, `ChatGoogleGenerativeAI`, and Hugging Face chat models) utilizing structured message arrays.
  - `03_EmbeddingModels/`: Generating dense vector representations (`OpenAIEmbeddings`, `GoogleGenerativeAIEmbeddings`, and local SentenceTransformers) and measuring cosine document similarity.

---

### [04. Prompts in LangChain](04_Prompts_in_LangChain/)

- **Core Technology**: `PromptTemplate`, `ChatPromptTemplate`, `MessagesPlaceholder`, Streamlit.
- **Description**: Advanced prompt engineering techniques, stateful chat prompt composition, temperature calibration, and interactive UI creation.
- **Key Concepts Covered**:
  - Dynamic & reusable prompt templates with variable injection.
  - Role-based prompting using `SystemMessage`, `HumanMessage`, and `AIMessage`.
  - Managing chat history in prompts using `MessagesPlaceholder`.
  - Temperature effects on determinism vs. creativity (`temperature.py`).
  - **Interactive Streamlit App (`prompt_ui.py`, `chatbot.py`)**: Web playground for testing dynamic prompt templates in real time.

---

### [05. Structured Output in LangChain](05_Structured_Output_in_LangChain/)

- **Core Technology**: `.with_structured_output()`, Pydantic v2, Python `TypedDict`, JSON Schema.
- **Description**: Guaranteeing type-safe, deterministic, machine-readable structured responses from LLMs instead of raw unstructured strings.
- **Key Concepts Covered**:
  - Forcing models to adhere strictly to schemas using function calling / JSON mode under the hood.
  - Output schema definitions via **Pydantic `BaseModel`**, **TypedDict**, and **JSON Schema**.
  - Comparison across OpenAI and open-source models (Llama via Ollama/Groq).
  - Extracting structured records from raw student dataset information (`students_dataset.csv`).

---

### [06. Output Parsers in LangChain](06_Output_Parsers_in_LangChain/)

- **Core Technology**: `StrOutputParser`, `JsonOutputParser`, `PydanticOutputParser`, `StructuredOutputParser`.
- **Description**: Parsing, cleaning, and converting raw model output streams into typed Python primitives and data structures.
- **Key Concepts Covered**:
  - `StrOutputParser`: Extracting pure text content from `AIMessage` objects for clean downstream chaining.
  - `JsonOutputParser`: Enforcing and streaming valid JSON objects.
  - `PydanticOutputParser`: Injecting format instructions into prompts and validating outputs against schema models.
  - Multi-provider implementations comparing OpenAI and Hugging Face pipelines.

---

### [07. Chains in LangChain & LCEL](07_Chains_in_LangChain/)

- **Core Technology**: LangChain Expression Language (LCEL), Declarative Pipelines, Pipe (`|`) Operator.
- **Description**: Composing linear and branching LLM workflows using the modern pipe syntax.
- **Key Patterns Implemented**:
  - **Simple Chains**: `prompt | model | parser`.
  - **Sequential Chains**: Cascading multiple steps where the output of Chain A becomes input to Chain B.
  - **Parallel Chains**: Running simultaneous independent queries (e.g., pros/cons analysis) concurrently.
  - **Conditional Chains**: Dynamically routing prompts to specialized branches based on intent classification.

---

### [08. Runnables in LangChain: Part 1](08_Runnables_in_LangChain_Part_01/)

- **Core Technology**: Runnable Protocol, Asynchronous Streaming, Batching, Fake LLMs.
- **Description**: The architectural underpinnings of the LangChain Expression Language (LCEL) and why it replaced legacy chains like `LLMChain`.
- **Key Concepts Covered**:
  - The unified Runnable interface: `invoke()`, `batch()`, `stream()`, `ainvoke()`, `abatch()`, `astream()`.
  - Unit testing LLM applications deterministically with fake LLMs (`langchain_fake_llm.ipynb`).
  - Document Q&A chains and legacy `RetrievalQA` analysis.

---

### [09. Runnables in LangChain: Part 2 (LCEL Primitives)](09_Runnables_in_LangChain_Part_02/)

- **Core Technology**: `RunnableSequence`, `RunnableParallel`, `RunnablePassthrough`, `RunnableLambda`, `RunnableBranch`.
- **Description**: Mastering advanced LCEL primitives to build production-grade, fault-tolerant execution graphs.
- **Primitives Implemented**:
  - `RunnableSequence`: Piping components sequentially with the `|` syntax.
  - `RunnableParallel`: Executing multiple branches concurrently and merging dict outputs.
  - `RunnablePassthrough`: Forwarding raw user input untouched alongside transformed values.
  - `RunnableLambda`: Wrapping arbitrary Python functions into seamless pipeline steps.
  - `RunnableBranch`: Conditional branching based on boolean evaluation predicates.

---

### [10. Document Loaders in LangChain](10_Document_Loaders_in_LangChain/)

- **Core Technology**: `TextLoader`, `CSVLoader`, `PyPDFLoader`, `DirectoryLoader`, `WebBaseLoader`, `BeautifulSoup`.
- **Description**: Ingesting structured and unstructured private enterprise documents into standard LangChain `Document` objects.
- **Data Sources Explored**:
  - Plain text files (`.txt`).
  - Tabular CSV datasets (`Social_Network_Ads.csv`).
  - PDF technical documents and books using `pypdf`.
  - Batch folder loading with glob pattern matching (`DirectoryLoader`).
  - Live web scraping using `WebBaseLoader` with HTML sanitization.

---

### [11. Text Splitters & Chunking Strategies](11_Text_Splitters_in_LangChain/)

- **Core Technology**: `CharacterTextSplitter`, `RecursiveCharacterTextSplitter`, `MarkdownHeaderTextSplitter`, `PythonCodeTextSplitter`, Semantic Meaning-based Splitting.
- **Description**: Solving context window limits and optimizing retrieval precision through smart document chunking.
- **Strategies Covered**:
  - **Length-Based Splitting**: Splitting on character thresholds and chunk overlap.
  - **Recursive Character Splitting**: Splitting by paragraphs, sentences, and words to maintain semantic coherence.
  - **Document Structure-Aware**: Splitting Markdown by `#` headers and Python files by function/class AST boundaries.
  - **Semantic Meaning-Based**: Using embedding cosine similarity shifts to split text where semantic topics change.

---

### [12. Vector Stores & Chroma DB](12_Vector_Stores_in_LangChain/)

- **Core Technology**: Vector Stores, Vector Databases, `langchain-chroma`, ChromaDB, Vector Similarity.
- **Description**: Indexing vector embeddings into high-performance vector databases for lightning-fast semantic retrieval.
- **Key Concepts Covered**:
  - Vector Store vs. Vector Database comparison (ephemeral search vs. scalable persistent index).
  - Integrating **Chroma DB** with LangChain.
  - Indexing chunked documents, assigning metadata tags, and running K-Nearest Neighbors (KNN) similarity search.

---

### [13. Retrievers & Intelligent Search](13_Retrievers_in_LangChain/)

- **Core Technology**: `VectorStoreRetriever`, `WikipediaRetriever`, `MultiQueryRetriever`, `ContextualCompressionRetriever`, Maximum Marginal Relevance (MMR).
- **Description**: Advanced search and reranking algorithms that go beyond simple semantic similarity.
- **Retriever Architectures**:
  - `VectorStoreRetriever`: Standard KNN vector querying.
  - `WikipediaRetriever`: Live external knowledge base querying.
  - `MultiQueryRetriever`: Using an LLM to generate multiple prompt perspectives to improve recall.
  - `MaximumMarginalRelevance (MMR)`: Balancing relevance with result diversity to eliminate duplicate chunks.
  - `ContextualCompressionRetriever`: Using an LLM to extract and compress only relevant sentences from retrieved chunks.

---

### [14. Retrieval-Augmented Generation (RAG) Foundations](<14_Retrieval_Augmented_Generation(RAG)/>)

- **Core Technology**: In-Context Learning, Vector Search, Knowledge Augmentation.
- **Description**: The comprehensive theoretical and architectural blueprint of modern RAG systems.
- **Core Dimensions Explored**:
  - **The Problem RAG Solves**: Overcoming LLM knowledge cutoffs, hallucination, and lack of private enterprise context.
  - **RAG vs. Fine-Tuning**: When to retrieve context (dynamic knowledge) vs. when to fine-tune (formatting/tone/specialized vocabulary).
  - **The 4-Stage Indexing Lifecycle**: Ingestion → Chunking → Embedding → Vector Indexing.
  - **The Generation Lifecycle**: User Query → Retrieval → Prompt Augmentation → LLM Synthesis.

---

### [15. Building a Production RAG System: YouTube Chatbot](15_Building_a_RAG_System_in_LangChain/)

- **Core Technology**: `youtube-transcript-api`, Chroma DB, Streamlit, LCEL, RAG Pipeline.
- **Description**: **Full-stack flagship showcase project**: An interactive YouTube video transcript question-answering assistant.
- **Application Architecture**:
  - `src/transcript.py`: Extracts and formats full video transcripts from YouTube video URLs.
  - `src/rag_pipeline.py`: Chunks transcripts with recursive splitters, generates embeddings, persists them into Chroma vector DB, and creates an augmented LCEL QA chain.
  - `app.py`: Clean Streamlit web dashboard where users paste any YouTube link and converse with the video content with source timestamps.

---

### [16. Tools & Toolkits in LangChain](16_Tools_in_LangChain/)

- **Core Technology**: `DuckDuckGoSearchRun`, `ShellTool`, `@tool` decorator, `StructuredTool`, `BaseTool`.
- **Description**: Empowering language models to interact with the external world by executing actions and fetching live data.
- **Tool Creation Approaches**:
  - Using pre-built tools (DuckDuckGo Web Search, Shell execution).
  - Creating custom tools via Python's `@tool` decorator with automated schema extraction from docstrings.
  - Using `StructuredTool.from_function()` with multi-argument Pydantic validation schemas.
  - Subclassing `BaseTool` for enterprise-level stateful tool development.

---

### [17. Tool Calling & Function Execution](17_Tool_Calling_in_LangChain/)

- **Core Technology**: `bind_tools`, Tool Calls, Arguments Serialization, Currency Conversion Engine.
- **Description**: The mechanics of modern LLM tool calling: binding tools to models, generating function call payloads, and executing tools deterministically.
- **Key Concepts Covered**:
  - Binding tools to chat models with `.bind_tools()`.
  - Extracting tool calls, tool IDs, and JSON arguments from `AIMessage.tool_calls`.
  - Executing tool functions and returning `ToolMessage` results back to the model.
  - **Project**: Building an end-to-end real-time **Currency Conversion Tool**.

---

### [18. Building Autonomous AI Agents (ReAct)](18_AI_Agent_in_LangChain/)

- **Core Technology**: ReAct Framework (Reasoning + Acting), `create_react_agent`, `AgentExecutor`, Autonomous Planning.
- **Description**: Capstone module: Constructing autonomous AI agents capable of multi-step reasoning, external search, computation, and iterative problem solving.
- **Key Concepts Covered**:
  - **The ReAct Loop**: Thought → Action → Action Input → Observation → Thought → Final Answer.
  - Configuring agent prompts and scratchpad memory.
  - Orchestrating complex reasoning chains with `AgentExecutor`.
  - Combining search tools, mathematical evaluators, and custom Python utilities into a unified autonomous agent.

---

## 💡 Featured Showcase Projects

### 1. 🎥 YouTube Transcript RAG Chatbot (`15_Building_a_RAG_System_in_LangChain`)

- **Overview**: Ingests any YouTube video URL, extracts full transcripts, stores embeddings in Chroma, and lets users converse with the video content.
- **Tech Stack**: Streamlit, `youtube-transcript-api`, ChromaDB, Google Gemini / OpenAI, LCEL.
- **How to Run**:
  ```bash
  cd 15_Building_a_RAG_System_in_LangChain
  streamlit run app.py
  ```

### 2. 🤖 Autonomous ReAct AI Agent (`18_AI_Agent_in_LangChain`)

- **Overview**: An autonomous agent combining live web search and mathematical reasoning to answer multi-step questions that require both real-time data and computation.
- **Tech Stack**: LangChain Core, `AgentExecutor`, `create_react_agent`, DuckDuckGo Search, Custom Math Tools.
- **How to Run**:
  ```bash
  cd 18_AI_Agent_in_LangChain
  python agents_in_langchain.py
  ```

### 3. 💬 Interactive Prompt Engineering Playground (`04_Prompts_in_LangChain`)

- **Overview**: Interactive Streamlit web interface for dynamically formatting prompt templates, adjusting system roles, and observing temperature effects.
- **Tech Stack**: Streamlit, LangChain Prompts, OpenAI / Gemini.
- **How to Run**:
  ```bash
  cd 04_Prompts_in_LangChain
  streamlit run prompt_ui.py
  ```

### 4. 💱 Real-Time Currency Conversion Tool (`17_Tool_Calling_in_LangChain`)

- **Overview**: Real-time tool-calling workflow demonstrating how LLMs parse human financial inquiries, extract currency symbols and quantities, and invoke conversion functions.
- **Tech Stack**: LangChain Tool Calling, Pydantic, Exchange APIs.

---

## 🛠 Technology & Integration Matrix

| Category                   | Supported Technologies & Libraries                                                                                                                                                                                   |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Frameworks**             | [LangChain](https://www.langchain.com/), [LangChain Core](https://python.langchain.com/docs/concepts/lcel/), [LangChain Community](https://python.langchain.com/)                                                    |
| **Foundation Models**      | [OpenAI](https://openai.com/) (GPT-4o, GPT-3.5), [Google Gemini](https://ai.google.dev/) (1.5 Pro/Flash, PaLM), [Anthropic](https://www.anthropic.com/) (Claude 3.5 Sonnet), [Hugging Face](https://huggingface.co/) |
| **Vector Databases**       | [Chroma DB](https://www.trychroma.com/), In-Memory Vector Stores                                                                                                                                                     |
| **Document Loaders**       | PyPDF, BeautifulSoup4, CSVLoader, DirectoryLoader, YouTube Transcript API                                                                                                                                            |
| **Chunking & Splitting**   | RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter, PythonCodeTextSplitter, Semantic Splitters                                                                                                               |
| **Retrieval Strategies**   | VectorStoreRetriever, MultiQueryRetriever, ContextualCompressionRetriever, Maximum Marginal Relevance (MMR)                                                                                                          |
| **Data Schemas & Parsing** | [Pydantic v2](https://docs.pydantic.dev/), TypedDict, JsonOutputParser, StrOutputParser                                                                                                                              |
| **External Tools**         | DuckDuckGo Search API, Shell Tool, Custom Tools via `@tool`                                                                                                                                                          |
| **Agent Architectures**    | ReAct (Reasoning + Acting), `AgentExecutor`                                                                                                                                                                          |
| **Frontend & UI**          | [Streamlit](https://streamlit.io/), Python-Dotenv                                                                                                                                                                    |

---

## 🚀 Getting Started Locally

### 1. Clone the Repository

```bash
git clone https://github.com/shubhamnagar234/LangChain.git
cd LangChain
```

### 2. Set Up a Python Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Activate on macOS / Linux:
source .venv/bin/activate
```

### 3. Install All Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔑 Environment Configuration (.env)

Create a `.env` file in the root directory (and inside specific project folders like `15_Building_a_RAG_System_in_LangChain`) with your API keys:

```ini
# OpenAI
OPENAI_API_KEY="your-openai-api-key"

# Google Gemini
GOOGLE_API_KEY="your-google-gemini-api-key"

# Anthropic Claude
ANTHROPIC_API_KEY="your-anthropic-api-key"

# Hugging Face
HUGGINGFACEHUB_API_TOKEN="your-huggingface-token"

# Optional: LangSmith Tracing & Observability
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_API_KEY="your-langchain-api-key"
LANGCHAIN_PROJECT="LangChain-Masterclass"
```

> [!NOTE]
> You only need the API key for the specific model provider you are running. For instance, to run Google Gemini scripts, only `GOOGLE_API_KEY` is required.

---

## 🛡 Production Best Practices for GenAI & Agents

1. **Keep Secrets Safe**: Never commit `.env` files or API keys. Ensure `**/.env` is strictly maintained in [.gitignore](.gitignore).
2. **Prefer LCEL Over Legacy Chains**: Use the declarative pipe operator (`|`) instead of legacy classes (`LLMChain`, `SimpleSequentialChain`) for built-in streaming, batching, and async execution.
3. **Always Validate LLM Outputs**: Never rely on raw string responses when integrating with downstream databases or APIs. Use `.with_structured_output(PydanticModel)` to enforce deterministic schemas.
4. **Tune Chunk Sizes to the Embedding Model**: Match chunk sizes (e.g., 500–1000 characters with 10–20% overlap) to your embedding model's optimal input length to avoid semantic dilution.
5. **Implement Agent Safety Guardrails**: Always configure maximum iterations (`max_iterations=5`) in `AgentExecutor` to prevent infinite tool-calling loops and unexpected API billing.

---

## 🤝 Contributing & License

Contributions, feedback, and improvements are warmly welcomed! Feel free to fork the repository, open an issue, or submit a pull request.

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for complete details.

---

<p align="center">
  Crafted with ❤️ by <b>Shubham Nagar</b>
</p>
