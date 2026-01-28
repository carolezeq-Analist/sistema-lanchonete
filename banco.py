import sqlite3 
# Conectando com banco de dados 
conexao = sqlite3.connect('Lanchonete.db')
cursor = conexao.cursor()
# Criando tabela de pedidos
cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
               lanche TEXT NOT NULL,
               quantidade TEXT NOT NULL,
               status TEXT DEFAULT 'Pendente'
)
               ''')

print("Banco de dados e tabelas criados com sucesso!")

# Exemplo inserindo pedido teste 
def inserir_pedido(nome, lanche, quantidade):
    cursor.execute("INSERT INTO pedidos (cliente, lanche, quantidade) VALUES (?, ?, ?)",
                   (nome, lanche, quantidade)
                 )
    conexao.commit()
    print(f"Pedido de {nome} salvo!")

# Testando inserção 
inserir_pedido("João", "X-Burguer", "2")
# Fechando conexão
conexao.close()