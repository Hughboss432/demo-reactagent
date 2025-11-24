import streamlit as st
import asyncio
from ai_core.mcp_tools import connect_to_server

if ('request' not in st.session_state):
    st.session_state['request'] = False

# Dados de exemplo para os produtos
produtos = [
    {"id": 1, "nome": "Produto 1", "preco": 10.99},
    {"id": 2, "nome": "Produto 2", "preco": 15.99}
]

# Função para exibir a lista de produtos
def exibir_produtos():
    st.header("Lista de Produtos")
    for produto in produtos:
        st.write(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

# Função para adicionar um novo produto
def adicionar_produto():
    st.header("Adicionar Novo Produto")
    nome = st.text_input("Nome do Produto")
    preco = st.number_input("Preço do Produto", min_value=0.0, step=0.01)
    
    if st.button("Adicionar"):
        produtos.append({"id": len(produtos) + 1, "nome": nome, "preco": preco})
        st.success("Produto adicionado com sucesso!")

# Função para conversar com a IA
def conversar_com_ia():
    st.header("Conversar com IA")
    
    # Placeholder para exibir as mensagens
    messages_placeholder = st.empty()
    
    # Input do usuário
    user_input = st.text_input("Você: ")
    
    if st.button("Enviar") and (st.session_state['request']==False or st.session_state['request'].done()):
        st.session_state['request'] = asyncio.run(connect_to_server(user_input))
        messages_placeholder.text(f"Você: {user_input}\nIA: {st.session_state['request']}")

# Configuração do Streamlit
st.set_page_config(page_title="Gerenciador de Produtos", page_icon="🛒")

# Sidebar com opções de navegação
menu = ["Visualizar Produtos", "Adicionar Produto", "Conversar com IA"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Visualizar Produtos":
    exibir_produtos()
elif choice == "Adicionar Produto":
    adicionar_produto()
elif choice == "Conversar com IA":
    conversar_com_ia()
