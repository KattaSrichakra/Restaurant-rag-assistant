# 🍽️ Sree Restaurant — AI-Powered RAG Chatbot

An AI-powered restaurant assistant that answers customer questions using restaurant-specific information. Built with **Streamlit, LangChain, Hugging Face embeddings, FAISS, and the Groq API**, the application retrieves relevant information from a local knowledge source and generates context-grounded responses.

## ✨ Features

- **Conversational interface:** Ask restaurant-related questions through a Streamlit chat interface.
- **Retrieval-Augmented Generation (RAG):** Retrieves relevant information before generating an answer.
- **Semantic search:** Uses Hugging Face sentence embeddings and FAISS for similarity-based retrieval.
- **Context-grounded responses:** Instructs the language model to answer using the retrieved restaurant information.
- **Groq LLM integration:** Uses the `openai/gpt-oss-20b` model through the Groq API.
- **Local knowledge base:** Uses `myresto.txt` as the restaurant information source.
- **Docker support:** Includes a Dockerfile to containerize the application.

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| User interface | Streamlit |
| LLM integration | Groq API |
| Language model | `openai/gpt-oss-20b` |
| RAG framework | LangChain |
| Embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| Vector database | FAISS |
| Containerization | Docker |
| Version control | Git and GitHub |

## 🏗️ Architecture

```text
             User Question
                   |
                   v
          Streamlit Chat UI
                   |
                   v
          LangChain RAG Chain
                   |
                   v
          Hugging Face Embeddings
                   |
                   v
          FAISS Similarity Search
                   |
                   v
          Retrieve Top 4 Chunks
                   |
                   v
        Restaurant Context + Query
                   |
                   v
             Groq LLM API
                   |
                   v
          Context-Grounded Answer
                   |
                   v
             Streamlit UI
```

## 📂 Project Structure

```text
Sree-Restaurant/
│
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
│
├── main.py
├── myresto.txt
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .env                  # Local only; never commit
└── README.md
```

- `main.py` — Streamlit interface and RAG pipeline.
- `myresto.txt` — Restaurant knowledge source.
- `faiss_index/` — Saved FAISS vector index and associated metadata.
- `requirements.txt` — Python dependencies.
- `Dockerfile` — Instructions for building the Docker image.
- `.env` — Stores the local Groq API key and must remain private.

## ⚙️ Prerequisites

Install the following before running the project:

- Python 3.11 recommended for the Docker configuration.
- Git.
- A valid Groq API key.
- Docker Desktop, if running the containerized application.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/KattaSrichakra/Restaurant-rag-assistant.git
cd Restaurant-rag-assistant
```

### 2. Create a virtual environment

**Windows Command Prompt:**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
groq_api_key=YOUR_GROQ_API_KEY
```

Replace the placeholder with your actual API key.

**Security:** Never commit `.env` or expose your API key in source code, screenshots, logs, or GitHub Actions files.

### 5. Run the application

```bash
python -m streamlit run main.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

Ask a question about the restaurant to test the chatbot.

## 🐳 Run with Docker

Ensure Docker Desktop is running.

### 1. Build the image

```bash
docker build -t sree-restaurant:latest .
```

### 2. Start the container

```bash
docker run --rm -p 8501:8501 --env-file .env sree-restaurant:latest
```

Open `http://localhost:8501` in your browser.

The `.env` file is supplied at runtime rather than copied into the Docker image.

**Note:** The application expects the saved FAISS index to be present in `faiss_index/`. The first run may also download the embedding model if it is not already cached.

## 🔐 Security

- Keep API keys in environment variables.
- Exclude `.env` and virtual environments using `.gitignore`.
- Do not hardcode API keys in Python files.
- Do not commit secrets to GitHub.
- Load only trusted FAISS index files because the saved index metadata may use Python pickle deserialization.

## 🔄 CI/CD Roadmap

GitHub Actions will be used to automate selected development and delivery tasks.

Planned workflow:

1. Trigger the workflow when code is pushed to GitHub or a pull request is opened.
2. Set up the required Python version.
3. Install project dependencies.
4. Run automated validation and tests.
5. Build the Docker image if the validation stage succeeds.

These are planned improvements; they should be marked as completed only after the workflow has been implemented and tested.

## 🎯 Learning Outcomes

This project provides practical experience with:

- Retrieval-Augmented Generation (RAG).
- Semantic embeddings and vector similarity search.
- LangChain retrieval chains.
- LLM API integration.
- Streamlit application development.
- Environment variable and API-key management.
- Docker image creation and container execution.
- Git and GitHub version control.

## 👩‍💻 Author

**Srichakra**

GitHub: [@KattaSrichakra](https://github.com/KattaSrichakra)

## 📄 License

No license has been specified yet. Add a license if you intend to define how others may use, modify, or distribute this project.
