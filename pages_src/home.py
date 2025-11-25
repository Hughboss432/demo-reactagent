import streamlit as st

class HomePage:                                    # Home page
    def render(self):
        st.title("Home")

        st.text_input("Buscar produtos...", "")

        st.subheader("Categories")
        categories = ["Type1", "Type2", "Type3", "Type4"]
        st.write(" | ".join(categories))

        st.subheader("Produtos")
        for i in range(8):
            st.write(f"Produto {i+1}")
