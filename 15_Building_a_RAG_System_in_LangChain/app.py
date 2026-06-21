import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from src.transcript import get_transcript
from src.rag_pipeline import generate_rag_answer

st.set_page_config(page_title="YouTube RAG System", page_icon="🎥")

st.title("🎥 YouTube Video Q&A")
st.markdown("Ask questions about any YouTube video using RAG.")

url = st.text_input("Paste YouTube URL")
question = st.text_input("Ask a question (e.g., 'Can you summarize the video?')")

if st.button("Generate Answer"):
    if url and question:
        with st.spinner("Fetching Transcript..."):
            transcript = get_transcript(url)

        if transcript == "No captions available for this video.":
            st.error(transcript)
        else:
            with st.spinner("Processing Documents & Generating Answer..."):
                answer = generate_rag_answer(transcript, question)

            st.success("Done")
            st.markdown(answer)
    else:
        st.warning("Please provide both a YouTube URL and a question.")
