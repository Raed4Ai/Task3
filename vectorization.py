from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from ingestion import load_documents
from chunking import split_documents



embeddings = HuggingFaceEmbeddings (
model_name="sentence-transformers/all-MiniLM-L6-v2",
model_kwargs={"device":"cpu"})


documents = load_documents()
chunks = split_documents(documents)

vectorDB = FAISS.from_documents(chunks, embeddings)

print("FAISS vector store created successfully!")
print("Stored chunks:", vectorDB.index.ntotal)

vectorDB.save_local("personal_knowledge_db")


