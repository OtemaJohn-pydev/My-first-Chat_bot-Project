"""
A simple Streamlit application that uses Langchain-Groq for chat functionality.
"""
import streamlit as st
from dotenv import dotenv_values
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

config = dotenv_values('.env')

system_message = SystemMessage(
    content="""
    You are a helpful assistant.
    You should not be too verbose, but you should be helpful.
    """
    )

if "llm" not in st.session_state:
    llm = ChatGroq(
        api_key=config["Groq_API_Key"],
        model_name=config["Groq_model"],
        temperature=0.2,
        # max_tokens=131_072,
    )
    st.session_state.llm = llm
else:
    llm = st.session_state.llm

st.title("My streamlit App with Langchain-Groq")

if "message" not in st.session_state:
    st.session_state.message = [system_message]
    
for message in st.session_state.message:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("Assistant"):
            st.write(message.content)
        

def generate_response():
    """Generate a response from the LLM based on the current session messages.
    """
    message = st.session_state.message
    response = llm.invoke(message)
    st.session_state.message.append(response)
    return response


if msg := st.chat_input("Enter your question here:"):
    st.session_state.message.append(HumanMessage(content=msg))
    response = generate_response()
    # st.session_state.message.append(AIMessage(content=response))
    st.rerun()