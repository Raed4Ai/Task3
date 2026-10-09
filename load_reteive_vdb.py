from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


VDB_PATH =r"D:\Ra'ed\Cellula_internship_NLP\Week3_task\RAG\Task3\personal_knowledge_db"



def load_vdb():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )

    vectorDB = FAISS.load_local(
        VDB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    print("FAISS database loaded successfully!")
    return vectorDB


def retrieve_context(vectorDB, query, k=4):
    similar_doc = vectorDB.similarity_search_with_score(query, k=k)

    context = []
    sources = []

    for doc, score in similar_doc:
        source = doc.metadata.get("source", "Unknown source")
        page = doc.metadata.get("page_number")

        citation = f"[Source: {source}"

        if page is not None:
            citation += f", Page: {page}"

        citation += "]"

        context.append(f"{citation}\n{doc.page_content}")
        sources.append(citation)

    return "\n\n".join(context), sources
