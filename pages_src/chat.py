import streamlit as st
import asyncio
from ai_core.mcp_tools import connect_to_server
from langchain_core.messages import AIMessage, HumanMessage

class AIChatPage:                                   # AI Chat page
    def render(self):
        st.title("AI Chat")
        st.write(f"User: {st.session_state.get('user', 'Unknown')}")

        if "chat" not in st.session_state:
            st.session_state.chat = []

        # Mostrar histórico do chat
        for message in st.session_state.chat:
            st.write(message.content)

        # Entrada de mensagem
        user_input = st.text_input("Mensagem:", "")

        if st.button("Enviar"):
            if user_input.strip() != "":
                st.session_state.chat.append(HumanMessage(content=f"👤 Usuário: {user_input}"))
                response = asyncio.run(connect_to_server(st.session_state.chat[-5:]))
                st.session_state.chat.append(AIMessage(content=f"🤖 AI: {response}"))
                st.rerun()

