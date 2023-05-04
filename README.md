# Depósito de Bebidas

Este projeto é um sistema simples de gerenciamento de depósito de bebidas, desenvolvido com o framework Django. Ele permite o gerenciamento de clientes, produtos e vendas.
# Instalação

Para executar o projeto, siga as instruções abaixo:

    Clone o repositório para o seu computador: git clone https://github.com/Joaovsaa/DepositodeBebidas.git
    Certifique-se de que você tem o Python 3 instalado.
    Crie um ambiente virtual para o projeto e ative-o:

    bash

python3 -m venv myenv
source myenv/bin/activate

Instale as dependências do projeto:

pip install -r requirements.txt

Execute as migrações do banco de dados:

python manage.py migrate

Inicie o servidor:

    python manage.py runserver

# Funcionalidades
# Clientes

    Adicionar, editar e excluir clientes.
    Visualizar uma lista de todos os clientes cadastrados.

# Produtos

    Adicionar, editar e excluir produtos.
    Visualizar uma lista de todos os produtos cadastrados.

# Vendas

    Criar uma nova venda.
    Adicionar produtos a uma venda.
    Visualizar as vendas existentes.
    Visualizar detalhes de uma venda, incluindo o cliente, a data e a lista de produtos.
    Exportar os dados de uma venda em formato CSV, XLSX, TSV ou ODS.

# Importações

    import_export.admin: adiciona funcionalidades de importação e exportação ao Django Admin.
    import_export.resources: fornece recursos para importação e exportação de dados.
    import_export.fields: fornece campos personalizados para importação e exportação de dados.
    import_export.widgets: fornece widgets personalizados para importação e exportação de dados.
    import_export.formats: fornece formatos de arquivo suportados para importação e exportação de dados.

# Licença

Este projeto é protegido pela Lei de Direitos Autorais e é de propriedade de João Sá, com e-mail joao.vsaa90@gmail.com. Este projeto é fornecido gratuitamente e pode ser utilizado para fins comerciais e não comerciais, desde que seja feita a atribuição apropriada e a utilização seja realizada em conformidade com os termos e condições estabelecidos nesta licença.

Permissões:

    É permitido o uso comercial deste projeto.
    É permitido o uso privado e pessoal deste projeto.
    É permitida a modificação e distribuição deste projeto.
    É permitida a utilização deste projeto em produtos derivados.

Restrições:

    Este projeto não pode ser vendido sem autorização expressa do proprietário.
    Este projeto não pode ser utilizado em atividades ilegais ou imorais.
    Este projeto não pode ser utilizado de forma prejudicial ou perigosa para pessoas ou animais.
    Este projeto não pode ser utilizado de forma a violar direitos autorais de terceiros.

Atribuição:

Ao utilizar este projeto, é necessário fornecer a atribuição adequada. Isso inclui a adição do nome do autor, João Sá, e o e-mail de contato, joao.vsaa90@gmail.com, em qualquer documentação ou produto que faça uso deste projeto.

Este projeto é fornecido "como está", sem garantia de qualquer tipo, expressa ou implícita, incluindo, mas não se limitando a garantias de comercialização, adequação a uma finalidade específica e não violação. Em nenhum caso o autor será responsável por qualquer reivindicação, danos ou outras responsabilidades, independentemente do tipo de ação, seja em contrato, delito ou de outra forma, decorrente ou relacionada ao uso deste projeto.
