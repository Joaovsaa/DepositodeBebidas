# DepositodeBebidas

# Descrição

O projeto tem como objetivo gerenciar as vendas de um depósito de bebidas, permitindo ao usuário cadastrar clientes, produtos e vendas. Além disso, o usuário poderá consultar as vendas realizadas e a quantidade de cada produto em estoque.
Funcionalidades

    Cadastro de clientes, produtos e vendas
    Consulta de vendas e produtos em estoque

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
