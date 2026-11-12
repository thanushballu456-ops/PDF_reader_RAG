# 📄 Resume RAG Assistant using Endee

A Streamlit-based AI application that lets users upload a resume PDF, store its embeddings in **Endee Vector Database**, and ask natural-language questions about the resume using **RAG (Retrieval-Augmented Generation)**.

## Features

- Upload a PDF resume
- Extract text from the PDF
- Split the resume into chunks
- Generate embeddings using Sentence Transformers
- Store vectors in Endee
- Retrieve the most relevant chunks for a question
- Generate context-aware answers using OpenAI
- Show retrieved source chunks for transparency

## Tech Stack

- Python
- Streamlit
- Endee Vector Database
- Sentence Transformers
- PyPDF
- OpenAI API

## Project Structure

```text
.
├── app.py
├── resume_rag_app.py
├── upsert_test.py
├── pdf_test.py
├── chunk_test.py
├── embed_test.py
├── test_endee.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How It Works

1. The user uploads a resume PDF.
2. The app extracts text from the PDF.
3. The extracted text is split into smaller chunks.
4. Each chunk is converted into an embedding vector.
5. The vectors are stored in Endee.
6. When the user asks a question, the app embeds the question and retrieves the top relevant chunks from Endee.
7. The retrieved chunks are passed to an LLM to generate the final answer.

## Installation

Clone the repository:

```bash
git clone https://github.com/sreeja814/Resume-RAG-Endee
cd Resume-RAG-Endee
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Setup API Key

This app uses the OpenAI API for answer generation.

Create this file:

```text
.streamlit/secrets.toml
```

Add your key:

```toml
OPENAI_API_KEY = "your_openai_api_key_here"
```

Do **not** upload this file to GitHub.

## Run the App

If your main file is `app.py`:

```bash
streamlit run app.py
```

If your main file is `resume_rag_app.py`:

```bash
streamlit run resume_rag_app.py
```

## Example Questions

- What are the candidate’s technical skills?
- What projects has the candidate built?
- Where did the student study?
- What internships or achievements are listed?
- Which programming languages are mentioned?

## Notes

- Make sure your Endee configuration is set correctly before running the app.
- The app may create and reuse an index for storing resume chunks.
- Retrieved chunks are shown in the interface to help verify answer quality.
- PDF text extraction quality can vary depending on the PDF formatting.

## Recommended Cleanup Before Submission

For a cleaner repository, keep:
- `app.py` or `resume_rag_app.py` (only one main app file is better)
- `requirements.txt`
- `.gitignore`
- `README.md`
- helper test scripts if needed

Avoid uploading:
- personal PDF resumes
- generated runtime files like `uploaded_resume.pdf`
- API keys or secret files

## Future Improvements

- Add support for multiple uploaded resumes
- Add chat history
- Improve PDF text cleaning
- Add better chunking strategies
- Deploy on Streamlit Community Cloud
- Add support for Groq or local LLMs

## Author

Built as a mini AI project using Streamlit, Endee, and OpenAI.