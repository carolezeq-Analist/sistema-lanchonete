# Dashboard com streamlit para lanchonete
import streamlit as st 
import sqlite3 
import pandas as pd 

# Configuração da página 
st.set_page_config(page_title="Painel da Lanchonete", layout="wide")
senha = st.sidebar.text_input("Senha de Acesso", type="password")
if senha == "692026":
    st.title("Painel de pedidos - Cozinha")
    st.write("Acompanhe os pedidos em tempo real e gerencie suas vendas!")


    # Função para buscar dados do banco 
    def carregar_dados():
        conexao = sqlite3.connect('Lanchonete.db')
        st.subheader("lista de pedidos atualizada")
        st.dataframe(dados)
        
    # o pandas lê diretamente do banco de dados
        df = pd.read_sql_query("SELECT * FROM pedidos", conexao)
        conexao.close()
        return df 

    # Botão para atualizar dados
    if st.button("Atualizar Pedidos"):
        st.rerun()

    # Buscando os dados 
    dados = carregar_dados()

    # Criando colunas no Dashboard
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Resumo de Vendas")
        if not dados.empty:
            contagem = dados['lanche'].value_counts()
            st.bar_chart(contagem)
    with col2:
        st.subheader("Total de unidades")
        if not dados.empty:
            vendas_por_Lanche = dados.groupby('lanche')['quantidade'].sum()
            st.bar_chart(vendas_por_Lanche)
        else:
            st.write("Nenhum pedido realizado ainda.")

