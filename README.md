AI SaaS Support Chatbot
RAG-based AI chatbot trained on PDFs and websites.

An AI-powered customer support chatbot demo project.
It learns from PDFs and websites, and provides AI-generated answers to user questions.

Features

📄 PDF & Website-based knowledge base

🧠 FAISS Vector Database for semantic search

🤖 OpenAI GPT for answer generation

🖥️ Streamlit user interface for easy testing


Project Structure

ai-saas-support-chatbot/
├── app/
│   ├── ingest.py         # Index PDFs and websites
│   ├── scraper.py        # Optional: web scraping
│   └── chatbot.py        # Chatbot logic
├── data/
│   ├── notion_docs.pdf
│   ├── stripe_docs.pdf
│   └── legal_contract.pdf
├── faiss_index/          # Generated FAISS index files
├── frontend/
│   └── streamlit_app.py
├── .env                  # OpenAI API key
├── requirements.txt
└── README.md


Installation

Create a virtual environment:

python -m venv venv

Activate the environment and install dependencies:

pip install -r requirements.txt

Add your OpenAI API key to .env:

OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX

Place the demo PDFs in data/

Run the ingestion script to build the vector index:

python app/ingest.py

Start the Streamlit interface:

streamlit run frontend/streamlit_app.py


Usage Examples
How do I create a workspace in Notion?
How does Stripe API work?
What is an NDA contract?
How It Works

Load PDFs and optionally scrape websites

Split text into smaller chunks

Generate embeddings with OpenAI

Store embeddings in FAISS vector database

Retrieve relevant chunks for user queries

Generate answers using GPT

Notes

For production, optimize website scraping and embeddings

You can add source attribution to responses

Multi-PDF support and conversation memory can enhance the chatbot