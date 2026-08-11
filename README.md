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

User Question
      ↓
Query Processing
      ↓
Document Retrieval
      ↓
Relevant Context
      ↓
LLM
      ↓
Generated Answer
