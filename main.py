from langchain_classic.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import dotenv_values
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from load_reteive_vdb import load_vdb , retrieve_context



env_values=dotenv_values(r"D:\Ra'ed\Cellula_internship_NLP\Week3_task\RAG\Task3\app.env")

api_key=env_values["OPENAPI_key"]


llm=ChatOpenAI(

   api_key=api_key,
   base_url="https://openrouter.ai/api/v1",
   model="openrouter/free",
   temperature=0.8
)





text="""you are assistant, Answer the next Question using provided context,
If you don't know the answer, just say you don't know.
answer should be within 200 words or fewer 
Include citations using the exact source labels provided in the context.
Do not invent sources or page numbers.

## context:
  {context}

## Question:
  {Question}

"""



temp=PromptTemplate.from_template(text)

vectorDB = load_vdb()

query="who is raed"

context, sources = retrieve_context(vectorDB, query, k=4)

prompt = temp.format(context="\n".join(context),Question=query)

response = llm.invoke(prompt).content
print(response)


prompt=temp.format(context="\n".join(context),Question =query)


respone=llm.invoke(prompt).content


print(respone)