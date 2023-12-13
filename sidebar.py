import streamlit as st
from streamlit_option_menu import option_menu

def sidebar():
    with st.sidebar:
        selected_tool = option_menu(
            menu_title=None,
            # options = ["TLDR","AFAIK","IMHO","JPEG","BRAIN"],
            # icons=["book","search","person","palette","person-plus"],
            options = ["TLDR","CHAT","Q&A","MINUTES","DEBATE"],
            icons=["book","chat","search","mic","yin-yang"],
            default_index = 0,
        )
        # st.markdown("---")
        # api_key_input = st.text_input(
        #     label="Enter your OpenAI API key:",
        #     type="password",
        #     placeholder="sk-xxxxxxxxxxxxxxxxxxxxxxxx",
        #     help="You can get your API key from https://platform.openai.com/account/api-keys.",
        #     value=st.session_state.get("OPENAI_API_KEY", ""),
        # )
        # st.session_state["OPENAI_API_KEY"] = api_key_input
        st.markdown("---")
        
        col1, col2 = st.columns([3, 1])
        with col1: 
            st.markdown("Made by some random Asian...")
        with col2: 
            jun_icon = "./img/jun.png"
            st.image(jun_icon)
            
    return selected_tool