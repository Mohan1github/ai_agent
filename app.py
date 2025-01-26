import os
from .agents import AgentManager
import streamlit as st
from  utils.logger import logger
from dotenv import load_dotenv

load_dotenv()

def main():
    st.set_page_config(
        page_title ="Multi_Agent AI system", layout = "wide"
    )
    st.title("Multi_Agent AI system with collaboration and validation")

    st.sidebar.title("Select Task")
    task = st.sidebar.selectbox(
        "choose a task:"[
            "Summarize medical text",
            "Wrtie and Refine Article",
            "Sanitize Medical Data (PHI)"
        ]
    )
      