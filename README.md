# 📦 Sistema de Pedidos

Sistema de pedidos desenvolvido em Python como projeto de estudo e portfólio para praticar conceitos de desenvolvimento Back-end, Programação Orientada a Objetos, bancos de dados relacionais e organização de código por responsabilidades.

O projeto começou como uma aplicação simples utilizando SQLite e funções separadas por módulos. Com a evolução dos estudos, foi sendo refatorado para uma estrutura mais próxima de aplicações Back-end reais, utilizando Models, Repositories, Services, validações e PostgreSQL.

🚧 Status: em desenvolvimento. O projeto está sendo construído e refatorado progressivamente conforme novos conceitos são estudados.

---

## 🎯 Objetivo

O principal objetivo deste projeto é aplicar, na prática, conceitos estudados durante minha formação em Análise e Desenvolvimento de Sistemas, especialmente relacionados ao desenvolvimento Back-end.

Entre os principais objetivos estão:

Praticar Python e Programação Orientada a Objetos;
Trabalhar com bancos de dados relacionais;
Criar operações CRUD;
Aprender a separar responsabilidades no código;
Praticar o padrão Repository;
Introduzir uma camada de Services para regras de negócio;
Criar validações reutilizáveis;
Trabalhar com relacionamentos entre entidades;
Evoluir a aplicação de uma estrutura simples para uma arquitetura mais organizada;
Preparar a base para estudos futuros de APIs REST.

---

## 🚀 Funcionalidades

### 👤 Usuários
Cadastro de usuários;
Atualização de dados;
Exclusão de usuários;
Consulta por ID;
Validação de nome, e-mail, telefone e ID.

### 📦 Produtos
Cadastro de produtos;
Atualização de produtos;
Exclusão de produtos;
Consulta por ID;
Validação de nome, preço, quantidade e ID.

### 🧾 Pedidos

A estrutura de pedidos já está sendo construída, incluindo:

Criação de pedidos;
Associação do pedido a um usuário;
Controle de status;
Estrutura para os itens do pedido.

### 🛒 Itens do pedido

Foi criada a entidade intermediária pedido_itens, responsável por relacionar:

Um pedido;
Um produto;
A quantidade do produto;
O preço unitário no momento do pedido.

Essa estrutura permite representar o relacionamento entre pedidos e produtos.
---

## 🛠️ Tecnologias utilizadas

Linguagens e ferramentas

* Python 3
* SQL
* PostgreSQL
* Git 
* GitHub

### Bibliotecas

* psycopg — conexão com PostgreSQL;
* python-dotenv — gerenciamento de variáveis de ambiente;
* Tkinter — interface gráfica.

---

## 📂 Estrutura do projeto

```text
Sistema-de-Pedidos/
│
├── database/
│   ├── conexao.py
│   └── loja.db
│
├── models/
│   ├── __init__.py
│   ├── usuarios.py
│   ├── produtos.py
│   ├── pedidos.py
│   └── pedido_itens.py
│
├── repository/
│   ├── __init__.py
│   ├── repository_base.py
│   ├── usuario_repository.py
│   ├── produtos_repository.py
│   ├── pedidos_repository.py
│   └── pedidos_itens_repository.py
│
├── services/
│   ├── pedido_service.py
│   ├── produto_service.py
│   └── usuario_service.py
│
├── utils/
│   └── validacoes.py
│
├── interface_principal.py
├── main.py
├── teste.py
├── .gitignore
└── LICENSE

Observação: alguns arquivos e funcionalidades ainda estão em processo de implementação e refatoração.
```
---

## 🗄️ Banco de Dados

O projeto começou utilizando SQLite, mas posteriormente foi migrado para PostgreSQL para aproximar o projeto de um cenário mais próximo de aplicações Back-end utilizadas em ambientes reais.

A conexão atualmente utiliza:

psycopg;
python-dotenv;
Variáveis de ambiente para as credenciais do banco.

Exemplo das variáveis utilizadas:

DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=

As credenciais não devem ser armazenadas diretamente no código ou versionadas no Git.

Modelo conceitual
```text
Usuários
    │
    │ 1:N
    ▼
Pedidos
    │
    │ 1:N
    ▼
Pedidos_Itens
    | 
    │ N:1
    ▼
Produtos
```
Um usuário pode possuir vários pedidos, e um pedido pode possuir vários itens. Cada item referencia um produto.

---

## 📚 Conceitos praticados

* Programação Orientada a Objetos;
* Classes e objetos;
* Atributos e métodos;
* CRUD;
* SQL;
* Chaves primárias e estrangeiras;
* Relacionamentos entre tabelas;
* Repository Pattern;
* Separação de responsabilidades;
* Camada de Services;
* Validação de dados;
* Tratamento de erros;
* Context Manager (with);
* Classes abstratas com ABC;
* Uso de @abstractmethod;
* Variáveis de ambiente;
* Organização de projetos Python em pacotes;
* Refatoração de código;
* Modelagem de banco de dados.

---

## 🔮 Próximas melhorias

O projeto continuará evoluindo conforme novos conceitos forem estudados.

### Organização e Back-end

* Finalizar PedidoService;
* Padronizar o retorno dos Services;
* Melhorar o tratamento de exceções;
* Melhorar as validações;
* Revisar consultas SQL.

### Testes

* Criar testes automatizados;
* Testar Services;
* Testar validações;
* Testar operações dos Repositories.

### Interface e API

* Melhorar a interface gráfica;
* Integrar completamente a interface com os Services;
* Criar uma API REST;

### Banco de dados
* Melhorar a modelagem;
* Revisar relacionamentos;
* Melhorar o gerenciamento das configurações do banco.

---

## 💡 Aprendizados

Mais do que construir um sistema de pedidos, este projeto está sendo utilizado para aprender como estruturar uma aplicação Back-end.

Alguns dos principais aprendizados até aqui:

* Uma aplicação funcionar não significa que sua arquitetura esteja organizada;
* Cada módulo deve possuir uma responsabilidade clara;
* Validações podem ser reutilizadas;
* Repositories devem se preocupar principalmente com persistência;
* Services podem concentrar regras e orquestrar operações;
* Models representam as entidades do domínio;
* Banco de dados e aplicação precisam possuir uma comunicação bem definida;
* Refatorar código faz parte do desenvolvimento;
* Erros de arquitetura também fazem parte do processo de aprendizagem.

Este projeto representa, portanto, não apenas um sistema de pedidos, mas também o registro da minha evolução estudando Python e desenvolvimento Back-end.

---

## ▶️ Como executar o projeto

### 1. Clone o repositório
git clone https://github.com/Alex-Hub176/Sistema-de-Pedidos.git

Entre na pasta:

cd Sistema-de-Pedidos

### 2. Crie um ambiente virtual
python -m venv .venv
Linux/macOS
source .venv/bin/activate
Windows
.venv\Scripts\activate

### 3. Instale as dependências
pip install psycopg python-dotenv

### 4. Configure as variáveis de ambiente

Crie um arquivo .env na raiz do projeto:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha

⚠️ Importante: nunca envie o arquivo .env para o GitHub. As credenciais do banco devem permanecer fora do código-fonte.

### 5. Configure o PostgreSQL

Certifique-se de que o PostgreSQL esteja instalado e em execução.

Crie o banco de dados utilizado pelo projeto e configure as respectivas credenciais no arquivo .env.

### 6. Execute o projeto

A entrada principal atual está em:

python main.py

🚧 Como o projeto ainda está em desenvolvimento, algumas funcionalidades podem exigir configuração adicional ou estar em processo de refatoração.

---

## 👨‍💻 Autor

Desenvolvido por Alex como projeto de estudo e portfólio durante minha formação em Análise e Desenvolvimento de Sistemas, com foco em Python e desenvolvimento Back-end.

O projeto continua sendo desenvolvido conforme novos conceitos são estudados e aplicados na prática.