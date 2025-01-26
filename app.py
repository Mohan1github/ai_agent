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
    agent_manager = AgentManager(max_retries= 2,verbose = True)

    if task == "Summarize medical text":
        summarize_section(agent_manager)
    
    elif task ==" Write and Refine Article":
        write_and_refine_article_section(agent_manager)
    
    elif task == "Sanitize Medical Data (PHI)":
        Medical_data_sanitization_section(agent_manager)



    def summarize_section(agent_manager):
        st.header("Summarize Medical Text")
        text = st.text_area("Enter the medical text to summarize:",height = 200)
        if st.button("Summarize"):
            if text:
                summary_agent = agent_manager.get_agent("Summarize")
                validator_agent = agent_manager.get_agent("summary_validator")
                with st.spinner("Summarizing..."):
                    try:
                        summary = summary_agent.execute(text)
                        st.subheader("summary:")
                        st.write(summary)
                    except Exception as e:
                        st.error(f"Error : {e}")
                        logger.error(f"Summarizing Agent Error;{e}")
                        return
                
                with st.spinner("Validating.."):
                    try:
                        validation = validator_agent.execute(original_text = text , summary = summary)
                        st.subheader("Validation:")
                        st.write(validation)
                    except Exception as e:
                        st.error(f"Error : {e}")
                        logger.error(f"Validation Agent Error:{e}")
                        return
                    
            else:
                st.warning("Please enter a text for the summarization")




        
    def  write_and_refine_article_section():
        st.header("Writing and refining the article")
        topic = st.text_area("Enter the article name:",height = 200)
        if st.button("Write article"):
            if topic:
                article_agent = agent_manager.get_agent("Write_article")
                article_validator = agent_manager.get_agent( "Writer_article_validator_tool")
                with st.spinner("Summarizing..."):
                    try:
                        article = article_agent.execute(topic)
                        st.subheader("Article:")
                        st.write(article)
                    except Exception as e:
                        st.error(f"Error : {e}")
                        logger.error(f"Article Agent Error:{e}")
                        return
                
                with st.spinner("Validating Article .."):
                    try:
                        validation = article_validator.execute(topic  = topic , article = article)
                        st.subheader(" Article Validation:")
                        st.write(validation)
                    except Exception as e:
                        st.error(f"Error : {e}")
                        logger.error(f" Article Validation Agent Error:{e}")
                        return
                    
            else:
                st.warning("Please enter a topic for writing article")





    def Medical_data_sanitization_section():
        st.header("Medicall data sanitizer")
        text = st.text_area("Enter the medical data to sanitize:",height = 200)
        if st.button("Sanitize"):
            if text:
                sanitize_agent = agent_manager.get_agent("Data_sanitizer_toll")
                sanitize_validator_agent = agent_manager.get_agent("sanitizer_data_validator_tool")
                with st.spinner("Sanitizing..."):
                    try:
                        sanitized = sanitize_agent.execute(text)
                        st.subheader("Sanitized data:")
                        st.write(sanitized)
                    except Exception as e:
                        st.error(f"Error : {e}")
                        logger.error(f"Sanitizing Agent Error;{e}")
                        return
                
                with st.spinner("Sanitizing Validating.."):
                    try:
                        validation =sanitize_validator_agent.execute(original_data = text , sanitized_data = sanitized)
                        st.subheader("sanitized Validation:")
                        st.write(validation)
                    except Exception as e:
                        st.error(f"Error : {e}")
                        logger.error(f" Sanitizing Validation Agent Error:{e}")
                        return
                    
            else:
                st.warning("Please enter a original data for the sanitation")
