# TO DOs: 
# 1. Summary Type drop down: Full Summary (default), Smart Brevity, Top Actionable Insights & Takeaways
# 2. Summarise URLs (will need scraper)
# 3. Add Claude 100k to summarise entire book
# 3.1. Using claude, provide a) executive summary, b) key points and takeaways, c) interesting examples

import os
import streamlit as st
from io import BytesIO
from streamlit_option_menu import option_menu
from summarise import summarise
from utils import chunk_text, convert_to_txt, get_transcript
from extract_topics import extract_topics

def TLDR(): 
    st.header("Summarise Anything")
    summarise_what = option_menu(
        menu_title=None,
        options=["Files","Tube","Text"],
        icons=["file-pdf","youtube","file-text"],
        default_index=0,
        orientation="horizontal"
    )
    st.write("")

    if summarise_what in ["Files", "Tube", "Text"]:
        if summarise_what == "Files":
            input_data = process_files_input()
        elif summarise_what == "Tube":
            input_data = process_tube_input()
        elif summarise_what == "Text":
            input_data = process_text_input()
        if input_data:
            create_summary(input_data)

def process_files_input():
    files = st.file_uploader("Upload PDF, ePub or text files you want to summarise:", ["pdf","epub","txt"], accept_multiple_files=True)
    st.write("")
    submitted = st.button("Start")

    if files and submitted:
        alltext = ""
        for file in files:
            file_ext = os.path.splitext(file.name)[1]
            file_data = file.getvalue()
            byte_file = BytesIO(file_data)
            text = convert_to_txt(byte_file, file_ext)
            alltext += str(text) + " " if file_ext == ".txt" else text + "\n\n"
        return alltext
    return None

def process_tube_input():
    url = st.text_input("Paste link to the Youtube video that you want to summarise below (e.g. https://www.youtube.com/watch?v=ad79nYk2keg):")
    st.write("")
    pressed = st.button("Start")
    return get_transcript(url) if url and pressed else None

def process_text_input():
    text = st.text_area("Paste any text you want to summarise:")
    st.write("")
    pasted = st.button("Start")
    return text if pasted and text else None

def create_summary(text):
    summary = ""
    my_bar = st.progress(0)
    st.markdown("#### Summary: ")

    use_claude = len(text) > 1000000
    too_long = len(text) > 10000

    if (use_claude):
        chunks = chunk_text(text,50000)
    else: 
        chunks = chunk_text(text, 10000)
    

    for i, chunk in enumerate(chunks):
        my_bar.progress((i + 1) / len(chunks))
        try:
            chunk_summary = summarise(chunk, too_long)
        except Exception as e:
            st.write("Something went wrong: " + str(e))
            return

        summary += "\n".join(chunk_summary.splitlines()) + "\n\n"

    if too_long:
        st.text_area(label="",value=summary, height=300)
    st.write("")
    st.download_button("Download Summary", data=summary, file_name="Summary.txt")
    st.write("---")
    
    # Extract topics
    st.markdown("#### Topics Explored: ")
    with st.spinner("Analysing..."):
        summary = extract_topics(text)
        st.text_area(label="",value=summary, height=300)
        st.write("")
        st.download_button("Download Topics", data=summary, file_name="Topics.txt")

    # Morpheus
    st.write("---")
    col1, col2 = st.columns([1, 9])
    with col1: 
        jun_icon = "./img/morpheus.png"
        st.image(jun_icon)
    with col2: 
        st.markdown("#### *\"There is a difference between knowing the path and walking path...\"*")
    st.write("---")