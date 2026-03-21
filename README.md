📚 AI SaaS Support Chatbot
 
A ChatGPT-like web application that allows users to chat with documents. Users can upload PDFs, and the bot answers questions based on both preloaded documents and uploaded PDFs using LangChain, FAISS, and OpenAI embeddings.

🚀 Features

Chat with your PDFs: Ask questions about the content of uploaded PDFs.
Preloaded documents support: Includes your initial PDFs or web scraping content.
Dynamic FAISS index: Newly uploaded PDFs are automatically added to the search index.
Streamlit interface: Simple, interactive web UI.
OpenAI GPT-4o-mini backend: Uses OpenAI embeddings for semantic search and GPT model for QA.
Persistent session: Chat history and uploaded PDFs remain during the session.
Safe deserialization: Loads FAISS index securely.

🛠️ Tech Stack

Python 3.10+
Streamlit – Web UI framework
LangChain – LLM orchestration & document processing
FAISS – Vector store for embeddings and semantic search
OpenAI API – GPT model for question answering
dotenv – Secure API key management

⚡ Installation

Clone the repository
git clone https://github.com/<your-username>/ai-pdf-chatbot.git
cd ai-pdf-chatbot
Create a virtual environment
python -m venv .venv
Activate the virtual environment
Windows (PowerShell):
.venv\Scripts\Activate.ps1
macOS / Linux:
source .venv/bin/activate
Install dependencies
pip install -r requirements.txt
Add your OpenAI API key

Create a .env file in the project root:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
🖥️ Usage

Run the Streamlit app:

streamlit run app/streamlit_app.py
Open your browser at http://localhost:8501
Upload PDFs in the 📄 Upload PDFs section
Ask questions using the chat box

The bot will answer based on both preloaded and newly uploaded PDFs.

🗂️ Project Structure
ai-pdf-chatbot/
│
├── app/
│   ├── chatbot.py          # QA chain and FAISS loading
│   ├── ingest.py           # Preload documents / PDFs into FAISS
│   └── streamlit_app.py    # Streamlit front-end
│
├── faiss_index/            # FAISS vector store (auto-generated)
├── data/                   # Preloaded PDFs
├── .env                    # OpenAI API key (not in repo)
├── requirements.txt
└── README.md

⚠️ Security Notes

FAISS uses pickle files for serialization.
The app sets allow_dangerous_deserialization=True for local, trusted files.
Never load untrusted FAISS indexes from unknown sources.
Keep .env secure and do not push it to GitHub.

📝 Dependencies

Key dependencies:

streamlit
langchain
langchain-classic
langchain-openai
langchain-community
faiss-cpu
python-dotenv

(Check requirements.txt for full versions.)

📌 Tips
Only PDFs are supported for upload.
Chat history is session-based; refreshing the browser will reset it.
The chatbot is retrieval-augmented: answers are based on the indexed PDFs, not generic web knowledge.
