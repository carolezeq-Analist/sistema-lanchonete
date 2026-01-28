# sistema-lanchonete
Criei uma plataforma web onde o cliente faz o pedido sozinho e o dono da lanchonete recebe tudo organizado em um painel administrativo, com gráficos que mostram o que está vendendo mais em tempo real."
2. Como funciona para o Cliente (A Vitrine)
• Acesso Direto: O cliente acessa um link (pode estar na Bio do Instagram ou em um QR Code na mesa).
• Facilidade: Ele preenche o nome, escolhe o lanche e a quantidade.
• Envio: Ao clicar em enviar, o pedido não vai para um "limbo"; ele é gravado instantaneamente em um banco de dados relacional (SQLite).
3. Como funciona para o Dono (A Cozinha/Escritório)
• Segurança: O painel é protegido por senha para que apenas o dono veja o faturamento e os dados dos clientes.
• Gestão Visual: Em vez de papéis ou mensagens soltas no WhatsApp, ele tem uma tabela automática com todos os pedidos pendentes.
• Inteligência de Negócio: O sistema gera gráficos de barras automáticos. Se o "X-Burguer" tiver 20 pedidos e o "X-Salada" tiver 5, o gráfico mostra visualmente qual lanche é o campeão de vendas, ajudando o dono a decidir o estoque.

O sistema foi desenvolvido em Python utilizando o framework Streamlit para a interface.
• Os dados são armazenados em SQLite e processados com a biblioteca Pandas para a parte analítica.
• O projeto está hospedado na nuvem (Streamlit Cloud), integrado diretamente com o GitHub.

site: https://sistema-lanchonete-v1.streamlit.app/
senha: 692026
