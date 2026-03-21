from dotenv import load_dotenv
import os

load_dotenv()  # must run first

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_classic.chains import RetrievalQA
import os

print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

embeddings = OpenAIEmbeddings()
db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

retriever = db.as_retriever()
qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model="gpt-4o-mini"), retriever=retriever)

def ask_bot(question: str):
    response = qa.run(question)
    return response