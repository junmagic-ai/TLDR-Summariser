import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate

def summarise (chunk,too_long):

    openai.api_base = st.secrets["OPENAI_BASE_URL"]
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    api_key = openai.api_key 
    docs = [Document(page_content=chunk)]
    prompt_template="""
        You are a world best summariser. Concisely summarise the text below, capturing essential points and core ideas. Include relevant examples, omit excess details, and ensure the summary's length matches the original's complexity:
    
        {text}
    """
    PROMPT = PromptTemplate(template = prompt_template,input_variables = ["text"])
    llm=ChatOpenAI(openai_api_base=openai.api_base,openai_api_key=api_key, temperature=0,model_name="gpt-3.5-turbo-16k", max_tokens=8000)
    chain = load_summarize_chain(llm, chain_type="stuff",prompt=PROMPT)
    summary = chain.run (docs)
    
    if not too_long:
        st.write(f'{summary}')
    return summary