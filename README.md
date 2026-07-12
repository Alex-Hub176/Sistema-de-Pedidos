# 📦 Sistema de Pedidos

Sistema desenvolvido em Python para praticar conceitos de Banco de Dados Relacional, utilizando SQLite e relacionamentos entre tabelas. O projeto simula o fluxo básico de uma loja, permitindo cadastrar usuários, criar pedidos e adicionar produtos aos pedidos.

---

## 🎯 Objetivo

Este projeto foi criado com o objetivo de consolidar conhecimentos em:

Python
SQLite
Modelagem de Banco de Dados
Relacionamentos entre tabelas (1:N)
Consultas SQL com JOIN
Organização de projetos em módulos

---

## 🚀 Funcionalidades

Cadastro de usuários
Criação de pedidos
Associação de pedidos aos usuários
Adição de produtos aos pedidos
Consulta de pedidos utilizando JOIN
Persistência de dados em SQLite

---

## 🛠️ Tecnologias utilizadas

Python 3
SQLite
SQL
Git e GitHub

---

## 📂 Estrutura do projeto

Sistema de Pedidos
│
├── dados/
│   └── loja.db
│
├── utils/
│   ├── cadastros.py
│   ├── pedido.py
│   ├── adicionar_produto.py
│   ├── listar_produtos.py
│   ├── database.py
│   └── __init__.py
│
└── main.py

---

## 🗄️ Modelo de Banco de Dados

O projeto utiliza três tabelas relacionadas:

Usuários
    │
    │ 1:N
    ▼
Pedidos
    │
    │ 1:N
    ▼
Itens do Pedido

Esse modelo representa um cenário comum em sistemas de vendas, onde:

Um usuário pode possuir vários pedidos.
Um pedido pode conter vários produtos.

---

## 📚 Conceitos praticados

CRUD
Relacionamentos entre tabelas
Chaves Primárias e Estrangeiras
INNER JOIN
INSERT
SELECT
Organização em módulos
Funções reutilizáveis
Context Manager (with)

---

## 🔮 Próximas melhorias

Este projeto continuará evoluindo durante meus estudos em Desenvolvimento Back-end.

Planejo implementar:

CRUD completo (Atualizar e Excluir)
Validação de dados
Tratamento de exceções
Cadastro de produtos em tabela própria
Interface gráfica com Tkinter
API REST utilizando Flask ou FastAPI
Migração do SQLite para MySQL ou PostgreSQL
Utilização do SQLAlchemy

---

## 💡 Aprendizados

Durante o desenvolvimento deste projeto, pratiquei conceitos importantes para o desenvolvimento Back-end, como modelagem de banco de dados, relacionamentos entre tabelas, manipulação de dados com SQL, organização de código em módulos e integração entre Python e SQLite. Este projeto representa minha evolução no estudo de persistência de dados e serve como base para futuras implementações com APIs REST e frameworks como Flask e FastAPI.

---

## 👨‍💻 Autor

Desenvolvido por Alex como projeto de estudo para praticar Python e Banco de Dados Relacional durante a minha graduação em Análise e Desenvolvimento de Sistemas.