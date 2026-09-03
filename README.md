# InterDoc-RAG

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![RAG Framework](https://img.shields.io/badge/Framework-RAG-orange.svg)](#)

**InterDoc-RAG** is an advanced Retrieval-Augmented Generation (RAG) framework tailored for inter-document analysis and cross-reference reasoning. It enables Large Language Models (LLMs) to retrieve, synthesize, and answer queries by analyzing context across multiple interconnected documents simultaneously.

---

##  Key Features

- **Multi-Document Contextual Retrieval**: Dynamically fetches relevant sections from across broad collections of documents rather than isolated single files.
- **Cross-Document Synthesis**: Generates cohesive, grounded answers that draw connections and highlight dependencies across multiple sources.
- **Hierarchical Chunking & Ingestion**: Preserves structural metadata (headings, sections, page numbers) during ingestion for precise attribution and retrieval.
- **Hybrid Search**: Combines dense semantic vector search with sparse keyword search (BM25) for high retrieval accuracy.
- **Citation & Source Attribution**: Provides precise cross-references linking synthesized insights back to source files and section locations.
## Architecture Overview
---
  ┌────────────────┐      ┌─────────────────┐      ┌──────────────────┐
│ Source Docs    │ ───► │ Ingestion &     │ ───► │ Vector & Sparse  │
│ (PDF, MD, TXT) │      │ Chunking Engine │      │ Indexing         │
└────────────────┘      └─────────────────┘      └─────────┬────────┘
│
┌────────────────┐      ┌─────────────────┐                ▼
│ Final Answer + │ ◄─── │ Context-Aware   │ ◄─── ┌──────────────────┐
│ Source Links   │      │ Generation LLM  │      │ Cross-Doc Search │
└────────────────┘      └─────────────────┘      └──────────────────┘

---

##  Quick Start

### Prerequisites

- **Python 3.10+** installed
- API Keys for your preferred LLM/Embedding provider (e.g., OpenAI, Cohere, Anthropic)

### 1. Installation

Clone the repository and install dependencies:

```
git clone [https://github.com/Damaa-C/interdoc-RAG-.git](https://github.com/Damaa-C/interdoc-RAG-.git)
cd interdoc-RAG-

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```
### 2. Environment Configuration

Create a `.env` file in the root directory and add your credentials:

```env
OPENAI_API_KEY=your_openai_api_key_here
VECTOR_DB_PATH=./data/vector_store
DOCUMENTS_DIR=./data/documents
```
### 3. Ingest Documents

Place your target files (`.pdf`, `.md`, `.txt`, `.docx`) in the `./data/documents` folder, then run the indexing pipeline:

```bash
python ingest.py
```
### 4. Query the System

Run an interactive cross-document search:

```bash
python main.py --query "Compare the safety protocols in Document A with the guidelines in Document B."
```
Or start the interactive CLI/API:
```python cli.py```
## Usage & Examples
Python API
```Python
from interdoc_rag import InterDocRAG

# Initialize pipeline
rag = InterDocRAG(
    embedding_model="text-embedding-3-small",
    llm_model="gpt-4o",
    vector_store_path="./data/vector_store"
)

# Run an inter-document query
response = rag.query(
    "Summarize all conflict points between contract_v1.pdf and specification_v2.pdf."
)

print("Answer:\n", response.answer)
print("\nSources Cited:")
for source in response.sources:
    print(f"- {source.doc_name} (Page {source.page})")```
##  Repository Structure
```interdoc-RAG-/
├── data/
│   ├── documents/          # Input documents directory
│   └── vector_store/       # Local vector index persistence
├── src/
│   ├── chunking/           # Document loader & cross-doc chunking logic
│   ├── embeddings/         # Vector embedding generation & managers
│   ├── retrieval/          # Hybrid search & re-ranking modules
│   └── generation/         # Prompt engineering & LLM synthesis pipelines
├── config.py               # Central configuration file
├── ingest.py               # Document parsing & indexing script
├── main.py                 # Query execution script
├── requirements.txt        # Python dependencies
└── README.md               # Repository documentation
```
## Tech Stack & Dependencies
- Frameworks: LangChain / LlamaIndex

- Vector Database: FAISS / Qdrant / ChromaDB

- LLM Integrations: OpenAI / HuggingFace Transformers

- Text Processing: PyPDF / Unstructured / Tiktoken

##  Contributing
Contributions are welcome! Follow these steps to contribute:

- Fork the repository.

- Create your feature branch (git checkout -b feature/AmazingFeature).

- Commit your changes (git commit -m 'Add some AmazingFeature').

- Push to the branch (git push origin feature/AmazingFeature).

- Open a Pull Request.

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact
Project Maintainer: Damaa-C

Project Link: https://github.com/Damaa-C/interdoc-RAG-

---

