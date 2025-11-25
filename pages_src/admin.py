import streamlit as st

class AdminPage:                                     # Super user page
    def render(self):
        st.title("Administração")
        st.write(f"User: {st.session_state.get('user', 'Unknown')}")

        st.write("Funções disponíveis:")
        st.write("[Create] [View] [Update] [Delete]")

        st.subheader("Produtos cadastrados:")
        for i in range(8):
            st.write(f"Produto {i+1}")