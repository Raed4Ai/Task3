
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader, TextLoader


BASE_DIR = Path(__file__).resolve().parent
CV_DIR = BASE_DIR / "sources" / "cv"
GITHUB_DIR = BASE_DIR / "sources" / "github"


def load_documents():
    documents = []

    # Load CV file
    for pdf_path in CV_DIR.rglob("*.pdf"):
        pdf_docs = PyPDFLoader(str(pdf_path)).load()

        for doc in pdf_docs:
            doc.metadata.update({
                "source": pdf_path.relative_to(BASE_DIR).as_posix(),
                "source_type": "cv",
                "filename": pdf_path.name,
                "page_number": doc.metadata.get("page", 0) + 1,
            })

        documents.extend(pdf_docs)

    # Load GitHub README files
    for md_path in GITHUB_DIR.rglob("README.md"):
        md_docs = TextLoader(
            str(md_path),
            encoding="utf-8",
        ).load()

        for doc in md_docs:
            doc.metadata.update({
                "source": md_path.relative_to(BASE_DIR).as_posix(),
                "source_type": "github",
                "filename": md_path.name,
                "project": md_path.parent.name,
            })

        documents.extend(md_docs)

    if not documents:
        raise ValueError("No documents found in the sources directory.")

    print(f"Loaded {len(documents)} documents.")

    return documents

