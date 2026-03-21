import streamlit as st
from dotenv import load_dotenv
import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_classic.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load environment variables
load_dotenv()

st.set_page_config(page_title="AI Support Chatbot", page_icon="🤖")
st.title("🤖 AI Support Chatbot")

# --- Initialize embeddings & FAISS ---
@st.cache_resource
def load_qa():
    embeddings = OpenAIEmbeddings()
    # Load existing FAISS index if it exists, else create empty
    if os.path.exists("faiss_index"):
        db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    else:
        db = FAISS.from_documents([], embeddings)
    retriever = db.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4o-mini"),
        retriever=retriever
    )
    return db, qa_chain

db, qa = load_qa()

# --- Initialize session state ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []  # store uploaded PDFs persistently

# --- PDF uploader (always stays at top) ---
st.subheader("📄 Upload PDFs")
uploaded_files = st.file_uploader(
    "Choose one or more PDFs",
    type="pdf",
    accept_multiple_files=True,
    key="pdf_uploader"
)

# Only process new PDFs
new_files = [f for f in uploaded_files if f not in st.session_state.uploaded_files]

if new_files:
    new_documents = []
    import tempfile
    for uploaded_file in new_files:
        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getbuffer())
            tmp_path = tmp_file.name

        loader = PyPDFLoader(tmp_path)
        new_documents += loader.load()
    
    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(new_documents)
    
    # Add to FAISS
    db.add_documents(chunks)
    db.save_local("faiss_index")
    
    # Remember uploaded PDFs
    st.session_state.uploaded_files.extend(new_files)
    
    st.success(f"✅ {len(new_files)} PDF(s) added to the index!")

# --- Show previous messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat input ---
if prompt := st.chat_input("Ask your question..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = qa.invoke({"query": prompt})  # returns dict
            response_text = result["result"]       # only answer text
            st.markdown(response_text)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response_text})