# 💳 API Bancária Assíncrona com FastAPI

API RESTful assíncrona desenvolvida com **FastAPI** para simular operações bancárias como criação de contas, depósitos, saques e consulta de extrato.
O projeto aplica boas práticas de arquitetura backend, autenticação com JWT e acesso assíncrono ao banco de dados.

---

## 🚀 Demonstração

### 📚 Swagger UI

![Swagger UI](./docs/swagger.png)

---

## 🛠️ Tecnologias Utilizadas

* Python 3.12
* FastAPI
* Uvicorn
* SQLite (aiosqlite)
* SQLAlchemy
* Databases (async)
* Pydantic v2
* PyJWT
* Alembic
* Poetry
* Pytest (testes automatizados)
* pytest-cov (cobertura de testes)

---

## 📌 Funcionalidades

### 👤 Autenticação

* Login com JWT
* Proteção de rotas privadas

### 💰 Operações Bancárias

* Criação de contas
* Depósito
* Saque com validação de saldo

### 📄 Extrato

* Listagem de transações por conta
* Histórico completo

---

## ⚙️ Como Rodar o Projeto

### 📦 1. Pré-requisitos

* Python 3.12+
* Poetry instalado

Instalar Poetry (caso não tenha):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

---

### 📥 2. Clonar o repositório

```bash
git clone https://github.com/estevaoMG/api-bancaria.git
cd api-bancaria
```

---

### 📦 3. Instalar dependências

```bash
poetry install
```

---

### 🗄️ 4. Rodar migrations (banco de dados)

```bash
poetry run alembic upgrade head
```

---

### 🚀 5. Executar a aplicação

```bash
poetry run uvicorn src.main:app --reload
```

---

## 🌐 Acessar a API

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* OpenAPI JSON: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## 🧪 Testes Unitários

### ▶️ Rodar testes

```bash
pytest
```

### 📊 Cobertura de testes

```bash
pytest --cov=src --cov-report=term-missing
```

---

## ⚙️ Regras de Negócio

* Depósitos não podem ser negativos
* Saques não podem ser negativos
* Saques não podem exceder saldo
* Cada transação pertence a uma conta

---

## 🧱 Estrutura do Projeto

```bash
api-bancaria/
├── src/
│   ├── controllers/
│   ├── services/
│   ├── models/
│   ├── schemas/
│   ├── views/
│   ├── config.py
│   ├── database.py
│   ├── exceptions.py
│   ├── security.py
│   └── main.py
│
├── tests/
├── alembic/
├── pyproject.toml
├── poetry.lock
└── README.md
```

---

## 🎯 Objetivo

Projeto para prática de backend com Python e FastAPI.

---

## 📄 Licença

Uso livre para estudo e portfólio.
