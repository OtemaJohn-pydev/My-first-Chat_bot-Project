import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_groq import ChatGroq
from dotenv import dotenv_values

st.title("My first Chat Trial")

st.chat_input("Ask anything")