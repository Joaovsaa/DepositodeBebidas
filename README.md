# DepositodeBebidas

# Descrição

Este projeto é um sistema de gerenciamento de um depósito de bebidas. Ele foi desenvolvido utilizando a linguagem de programação Python e o framework Django.

O sistema permite o cadastro de clientes, produtos e vendas. Os produtos podem ser categorizados em bebidas, alimentos, kits e utensílios. Para cada venda, é possível selecionar o cliente e adicionar vários produtos a serem vendidos. O valor total da venda é calculado automaticamente.

Os modelos do projeto são:

    Cliente: armazena o nome, contato e endereço do cliente.
    Produto: armazena o nome, valor, categoria e quantidade do produto.
    Venda: armazena o cliente, data e valor total da venda.
    VendaProduto: modelo de relacionamento que armazena a quantidade de cada produto vendido em cada venda.

O sistema conta com uma interface administrativa, onde é possível visualizar, adicionar, editar e excluir os registros de clientes, produtos e vendas. Além disso, o sistema possui uma página inicial que lista todas as vendas registradas.

# Instalação

    Clone este repositório: git clone https://github.com/Joaovsaa/DepositodeBebidas.git
    Crie um ambiente virtual: python -m venv env
    Ative o ambiente virtual: source env/bin/activate (Linux/Mac) ou .\env\Scripts\activate (Windows)
    Instale as dependências: pip install -r requirements.txt
    Configure o banco de dados no arquivo settings.py
    Realize as migrações: python manage.py migrate
    Crie um superusuário: python manage.py createsuperuser
    Inicie o servidor: python manage.py runserver

# Uso

Após a instalação, basta acessar o endereço http://localhost:8000/admin/ e fazer login com as credenciais do superusuário criado.

No painel de administração é possível gerenciar as entidades do sistema. Para cadastrar uma venda, é necessário selecionar o cliente, adicionar os produtos e informar a quantidade vendida.
Contribuindo

Contribuições são bem-vindas! Caso encontre algum problema ou tenha uma sugestão de melhoria, por favor, abra uma issue ou um pull request.
# Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
