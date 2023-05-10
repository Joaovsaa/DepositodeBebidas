#Sistema de Gerenciamento de Depósito de Bebidas

Este é um sistema de gerenciamento básico para um depósito de bebidas, desenvolvido utilizando Django.
Funcionalidades

O sistema oferece as seguintes funcionalidades:

    Cadastro e gerenciamento de clientes.
    Cadastro e gerenciamento de produtos.
    Registro e acompanhamento de vendas.
    Cálculo automático do total de vendas.
    Exportação de relatórios de vendas em vários formatos (CSV, XLSX, TSV, ODS).
    Importação de dados para o sistema a partir de arquivos.

#Requisitos

Para executar o sistema localmente, você precisará ter os seguintes requisitos:

    Python 3.7 ou superior
    Django 3.2.5 ou superior
    Bibliotecas adicionais listadas no arquivo requirements.txt

Como executar o projeto

    Clone este repositório em sua máquina local:

    bash

git clone https://github.com/Joaovsaa/DepositodeBebidas.git

Acesse o diretório do projeto:

bash

cd DepositodeBebidas

Crie um ambiente virtual (opcional, mas recomendado):

bash

python -m venv env

Ative o ambiente virtual:

    Windows:

    bash

env\Scripts\activate

Linux/Mac:

bash

    source env/bin/activate

Instale as dependências do projeto:

pip install -r requirements.txt

Execute as migrações do banco de dados:

python manage.py migrate

Inicie o servidor de desenvolvimento:

    python manage.py runserver

    Acesse o sistema em seu navegador web em http://localhost:8000.

#Contribuindo

Se você deseja contribuir para este projeto, fique à vontade para abrir uma nova issue ou enviar um pull request com suas melhorias.
#Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.

Este projeto foi desenvolvido por [João Sá] e faz parte de um trabalho acadêmico/profissional.
