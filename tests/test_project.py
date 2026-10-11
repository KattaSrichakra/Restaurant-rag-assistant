
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_required_project_files_exist():
    """Check that essential application files are present."""
    required_files = [
        "main.py",
        "myresto.txt",
        "requirements.txt",
        "Dockerfile",
    ]

    for filename in required_files:
        assert (ROOT / filename).is_file(), (
            f"Required file is missing: {filename}"
        )


def test_restaurant_knowledge_base_is_not_empty():
    """Check that the restaurant knowledge source contains data."""
    knowledge_file = ROOT / "myresto.txt"

    assert knowledge_file.is_file()
    assert knowledge_file.stat().st_size > 0


def test_faiss_index_files_exist():
    """Check that the saved vector index files are available."""
    index_files = [
        ROOT / "faiss_index" / "index.faiss",
        ROOT / "faiss_index" / "index.pkl",
    ]

    for file_path in index_files:
        assert file_path.is_file(), (
            f"FAISS index file is missing: {file_path.name}"
        )
        assert file_path.stat().st_size > 0


def test_rag_configuration_is_present():
    """Check important RAG settings in the application source."""
    source = (ROOT / "main.py").read_text(encoding="utf-8")

    assert "HuggingFaceEmbeddings" in source
    assert "FAISS.load_local" in source
    assert 'search_kwargs={"k": 4}' in source
    assert "create_retrieval_chain" in source
    assert "ChatGroq" in source
