# Engineering Assistant Agent

A multi-capability AI assistant built using **Retrieval-Augmented Generation (RAG)** to interact with engineering documents through a conversational interface.

The system extends a basic RAG-based question-answering pipeline into an **Engineering Assistant Agent** capable of performing **Question Answering, Document Summarization, Document Comparison, and Note Generation**.

A conversational **Streamlit** interface allows users to interact with the assistant through a chat-style experience.

---

## 📌 Overview

The project was developed as an extension of a basic **Retrieval-Augmented Generation (RAG)** pipeline.

The initial RAG system was designed primarily for document-based question answering. The project was then extended into a multi-capability **Engineering Assistant** by adding multiple knowledge-based capabilities and a conversational user interface.

The assistant can work with engineering documents and provide different types of document-related assistance depending on the user's requirement.

The main capabilities implemented in the system are:

- **Question Answering**
- **Document Summarization**
- **Document Comparison**
- **Note Generation**

During development, several practical issues were encountered related to retrieval, LLM responses, vector database handling, package compatibility, and the Streamlit interface. These issues were debugged and resolved through iterative testing and improvements to the system architecture.

---

## 🚀 Key Features

- Retrieval-Augmented Generation (RAG)
- Engineering document question answering
- Document summarization
- Document comparison
- Automatic note generation
- Conversational AI assistant
- Streamlit chat interface
- Vector database-based document retrieval
- Prompt engineering
- Retrieval debugging and optimization
- Vector database recreation and recovery logic
- Modular project architecture
- Multi-capability document interaction

---

## 🧠 System Capabilities

### 1. Question Answering

The assistant retrieves relevant information from the available engineering documents and uses the retrieved context to generate an answer to the user's question.

###2. Document Summarization

The assistant can generate concise summaries of engineering topics, chapters, or retrieved document content.

This feature enables users to understand key concepts more quickly by condensing lengthy document content into structured summaries.

###3. Document Comparison

The assistant can compare two engineering concepts, technologies, methods, or topics using information retrieved from the document collection.

The generated comparison highlights similarities, differences, advantages, and important distinctions between concepts.

###4. Note Generation

The assistant can automatically generate study notes from the retrieved document content.

The notes are designed to provide a concise and organized overview of important concepts, making revision and learning easier.

##⚙️ Technology Stack
Programming Language
Python
Frameworks and Libraries
LangChain
Streamlit
ChromaDB
Ollama
HuggingFace Embeddings
AI Components
Phi-4 Mini
Retrieval-Augmented Generation (RAG)
Vector Database
ChromaDB

##🔧 Challenges Encountered and Solutions
1. LangChain Import Issues

Challenge: Frequent package updates caused import errors and compatibility issues.

Solution: Updated imports according to the latest LangChain package structure and installed compatible package versions.

2. Duplicate Retrieval Results

Challenge: The retriever often returned repetitive document chunks, reducing answer quality.

Solution: Optimized retrieval logic and document chunking strategy to improve retrieval diversity.

3. Hallucinated Responses

Challenge: The language model occasionally produced responses not supported by retrieved documents.

Solution: Implemented stronger prompt instructions to ensure responses remain grounded in retrieved context.

4. Empty Context Generation

Challenge:

No documents were being retrieved for certain queries.

Solution: Debugged the retrieval pipeline and rebuilt the vector database whenever retrieval returned zero documents.

5. ChromaDB Loading Problems

Challenge: Persisted vector stores occasionally failed to load correctly.

Solution: Validated vector database paths and recreated embeddings when required.

6. Streamlit Import Errors

Challenge: Application startup failures caused by environment and dependency issues.

Solution: Resolved package conflicts and verified project dependencies.

7. Project Scalability

Challenge: The original implementation consisted of a single-purpose RAG pipeline.

Solution: Refactored the project into modular components and introduced routing logic to support multiple capabilities.

##✅ Results

The project successfully evolved from a basic RAG-based question-answering system into a more advanced Engineering Assistant Agent capable of supporting multiple document-oriented tasks.

Key achievements include:

Multi-capability engineering document assistant
Conversational Streamlit interface
Improved retrieval quality
Reduced hallucinations through prompt engineering
ChromaDB-based vector search
Modular and maintainable architecture
Support for Question Answering, Summarization, Comparison, and Note Generation
Enhanced user experience through chat-based interaction
