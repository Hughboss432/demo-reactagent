import streamlit as st
import asyncio
from mcp_tools import connect_to_server
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(page_title="Agente com MCP", layout="centered")
st.title("🤖 LPhantom")

user_input = st.chat_input("Digite algo...")

if user_input:
    result = asyncio.run(connect_to_server(user_input))
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(f"Echo: {result}")

