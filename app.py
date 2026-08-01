import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Sistema de Clientes", page_icon="👥", layout="wide")
st.title("👥 Sistema de Gestão de Clientes")

ARQUIVO_DADOS = "clientes.csv"

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        return pd.read_csv(ARQUIVO_DADOS)
    else:
        return pd.DataFrame(columns=["Nome", "Telefone", "E-mail", "Cidade"])

df = carregar_dados()
menu = st.sidebar.selectbox("Menu", ["Cadastrar Cliente", "Ver Clientes"])

if menu == "Cadastrar Cliente":
    st.subheader("Cadastrar Novo Cliente")
    with st.form("form_cliente", clear_on_submit=True):
        nome = st.text_input("Nome Completo")
        telefone = st.text_input("Telefone")
        email = st.text_input("E-mail")
        cidade = st.text_input("Cidade")
        enviar = st.form_submit_button("Salvar Cliente")
        
        if enviar:
            if nome:
                novo_dado = pd.DataFrame([[nome, telefone, email, cidade]], columns=["Nome", "Telefone", "E-mail", "Cidade"])
                df = pd.concat([df, novo_dado], ignore_index=True)
                df.to_csv(ARQUIVO_DADOS, index=False)
                st.success(f"Cliente {nome} cadastrado com sucesso!")
            else:
                st.error("Preencha o nome do cliente.")

elif menu == "Ver Clientes":
    st.subheader("Clientes Cadastrados")
    if not df.empty:
        st.dataframe(df, use_container_width=True)
        if st.button("Limpar Todos os Cadastros"):
            if os.path.exists(ARQUIVO_DADOS):
                os.remove(ARQUIVO_DADOS)
            st.rerun()
    else:
        st.info("Nenhum cliente cadastrado ainda.")
