from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain_classic.chains import RetrievalQA
import os

embeddings = OpenAIEmbeddings()
db = FAISS.load_local("faiss_index", embeddings)

retriever = db.as_retriever()
qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model="gpt-4o-mini"), retriever=retriever)

def ask_bot(question: str):
    response = qa.run(question)
    return response