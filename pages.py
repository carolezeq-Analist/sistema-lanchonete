# Formulario para pedidos 
import streamlit as st 
import sqlite3

# Colocando um formulario 
st.divider()
st.subheader("Registrar Novo Pedido")

# Criando o formulário
with st.form("meu_formulario"):
    nome = st.text_input("Nome do Cliente")
    lanche = st.selectbox("Escolha o Lanche", ["X-Burguer", "X-Salada", "X-Bacon",
                                               "Cachorro Quente", "Batata Frita", "Refrigerante"])
    quantidade = st.number_input("Quantidade", min_value=1, step=1)
    botao = st.form_submit_button("Finalizar Pedido")
    if botao:
        conn = sqlite3.connect('Lanchonete.db')
        c = conn.cursor()
        c.execute("INSERT INTO pedidos (cliente, lanche, quantidade) VALUES (?, ?, ?)",
                  (nome, lanche, quantidade))
        conn.commit()
        conn.close()
        st.success(f"Pedido de {nome} enviado com sucesso!")