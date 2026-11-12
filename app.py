import streamlit as st
from dotenv import load_dotenv
import os
from sentence_transformers import SentenceTransformer
from endee import Endee
from google import genai

load_dotenv()

INDEX_NAME = "documents_v2"

st.title("Endee RAG Chatbot")

# ---- Check API key ----
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.warning("GEMINI_API_KEY not found in .env file.")
    st.stop()   # don't continue rendering the rest of the app without a key

# ---- Load models/clients once, not on every interaction ----
@st.cache_resource
def load_resources():
    embed_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    endee_client = Endee()
    index = endee_client.get_index(name=INDEX_NAME)
    gemini_client = genai.Client()
    return embed_model, index, gemini_client

embed_model, index, gemini_client = load_resources()

st.success("Connected to Gemini and Endee.")

# ---- Retrieval + generation ----
def retrieve(query, top_k=3):
    query_vector = embed_model.encode([query])[0].tolist()
    results = index.query(vector=query_vector, top_k=top_k)
    return [r["meta"]["text"] for r in results]

def generate_answer(query, retrieved_chunks):
    context = "\n\n".join(retrieved_chunks)
    prompt = f"""Answer the question using ONLY the context below.
If the context doesn't contain the answer, say "I don't know based on the provided material."

Context:
{context}

Question: {query}

Answer:"""
    response = gemini_client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return response.text

# ---- Chat UI ----
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_query = st.chat_input("Ask something about the document...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.write(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            top_chunks = retrieve(user_query)
            answer = generate_answer(user_query, top_chunks)
            st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})