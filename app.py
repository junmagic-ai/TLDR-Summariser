import streamlit as st
from styling import local_css
from sidebar import sidebar
from TLDR import TLDR
from AFAIK import AFAIK
from IMHO import IMHO
from IIRC import IIRC
from CHAT import CHAT
from DEBATE import DEBATE

if __name__=="__main__":

    st.set_page_config(page_title="GPTools", page_icon=":gear:", layout="wide")
    local_css('style/style.css')
    state = ""
    selected_tool = sidebar()
    if (selected_tool == "TLDR"):
        TLDR()
    if (selected_tool == "CHAT"):
        CHAT()
    if (selected_tool == "Q&A"):
        AFAIK()
    if (selected_tool == "AGENT"):
        IMHO()
    if (selected_tool == "MINUTES"):
        IIRC()
    if(selected_tool == "DEBATE"):
        DEBATE()