from langchain_classic.text_splitter import TokenTextSplitter
from ingestion import load_documents

def split_documents(documents):
    splitter = TokenTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        add_start_index=True,
    )

    chunks = splitter.split_documents(documents)

    return chunks


