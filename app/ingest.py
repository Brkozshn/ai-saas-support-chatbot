from dotenv import load_dotenv
import os

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# PDF dosyaları
pdf_files = [
    "data/notion_docs.pdf",
    "data/stripe_docs.pdf",
    "data/legal_contract.pdf"
]

documents = []

for pdf in pdf_files:
    loader = PyPDFLoader(pdf)
    documents += loader.load()

# Website scraping (isteğe bağlı)
urls = [
    "https://www.notion.so/help",
    "https://docs.stripe.com"
]

for url in urls:
    loader = WebBaseLoader(url)
    documents += loader.load()

# Text parçalama
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# Embeddings
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(chunks, embeddings)

# Kaydet
os.makedirs("faiss_index", exist_ok=True)
db.save_local("faiss_index")
print("FAISS index hazir!")