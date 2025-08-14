import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import utility functions
from utils.transcript import extract_transcript_details
from utils.summarizer import generate_gemini_content

# Prompt template for summarization
prompt = "Provided text and highlight the key points using bold formatting within appropriate headings, all contents should be in hindi. Below is the content to summarize:  "

# Header
header = '''
<div class="header">
    <h2 style='text-align: center; color: red;'><p>YouTube summarizer by Kuldeep Singh</p></h2>
</div>
'''
st.markdown(header, unsafe_allow_html=True)

# YouTube link input
st.markdown("<h3 style='text-align: center; color: green;'>Enter YouTube Video Link Below</h3>", unsafe_allow_html=True)
youtube_link = st.text_input("")

# Show thumbnail
if youtube_link:
    try:
        video_id = youtube_link.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)
    except IndexError:
        st.error("Please provide a valid YouTube link.")

# Button action
if st.button("Get Detailed Notes"):
    if youtube_link:
        try:
            transcript_text = extract_transcript_details(youtube_link)
            if transcript_text:
                summary = generate_gemini_content(transcript_text, prompt)
                st.markdown("## Detailed Notes:")
                st.write(summary)
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Footer
footer = '''
<div class="footer">
    <p>Learn more about AI and Machine Learning at 
    <a href="https://www.linkedin.com/in/kuldeep-singh-kamboj" style="color: red;">Kuldeep Singh</a></p>
</div>
'''
st.markdown(footer, unsafe_allow_html=True)
