# 💳 API Bancária Assíncrona com FastAPI

API RESTful assíncrona desenvolvida com **FastAPI** para simular operações bancárias como criação de contas, depósitos, saques e consulta de extrato.  
O projeto aplica boas práticas de arquitetura backend, autenticação com JWT e acesso assíncrono ao banco de dados.

---

## 🚀 Demonstração

### 📚 Swagger UI

![Swagger UI](./docs/swagger.png)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12  
- FastAPI  
- Uvicorn  
- SQLite (aiosqlite)  
- SQLAlchemy  
- Databases (async)  
- Pydantic v2  
- PyJWT  
- Alembic  
- Poetry  
- Pytest (testes automatizados)  
- pytest-cov (cobertura de testes)

---

## 📌 Funcionalidades

### 👤 Autenticação
- Login com JWT
- Proteção de rotas privadas

### 💰 Operações Bancárias
- Criação de contas
- Depósito
- Saque com validação de saldo

### 📄 Extrato
- Listagem de transações por conta
- Histórico completo

---

## 🧪 Testes Unitários

O projeto possui testes automatizados com Pytest.

### ▶️ Rodar testes
pytest

### 📊 Cobertura
pytest --cov=src --cov-report=term-missing

---

## ⚙️ Regras de Negócio

- Depósitos não podem ser negativos  
- Saques não podem ser negativos  
- Saques não podem exceder saldo  
- Cada transação pertence a uma conta  

---

## 🧱 Estrutura do Projeto

api-bancaria/
├── src/
├── tests/
├── alembic/
├── pyproject.toml
└── README.md

---

## 🎯 Objetivo

Projeto para prática de backend com Python e FastAPI.

---

## 📄 Licença

Uso livre para estudo e portfólio.