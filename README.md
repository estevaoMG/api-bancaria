# 💳 API Bancária Assíncrona com FastAPI

API RESTful assíncrona desenvolvida com **FastAPI** para simular operações bancárias como depósitos, saques e consulta de extrato. O projeto aplica boas práticas de arquitetura backend, autenticação com JWT e acesso assíncrono ao banco de dados.

---

## 🚀 Demonstração

### 📚 Swagger UI

![Swagger UI](./docs/swagger.png)

Interface interativa para testar os endpoints diretamente no navegador.

---

## 🚀 Tecnologias Utilizadas

* Python 3.12
* FastAPI
* Uvicorn
* SQLite (aiosqlite)
* SQLAlchemy
* Databases (async)
* Pydantic
* PyJWT
* Alembic
* Poetry

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

## ⚙️ Regras de Negócio

* Não é permitido:

  * Depósitos com valores negativos
  * Saques com valores negativos
  * Saques sem saldo suficiente
* Cada transação pertence a uma conta
* Uma conta pode ter múltiplas transações

---

## 🧱 Estrutura do Projeto

```bash
api-bancaria/
├── migrations/              
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│   └── README
│
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
├── .env                     
├── alembic.ini              
├── pyproject.toml           
├── poetry.lock              
├── README.md                
└── LICENSE
```

---

## 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas:

* **Controllers:** recebem requisições HTTP
* **Services:** regras de negócio
* **Models:** representação do banco
* **Schemas:** validação de dados
* **Security:** autenticação JWT
* **Database:** conexão com banco

---

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` na raiz:

```env
ENVIRONMENT=local
DATABASE_URL=sqlite+aiosqlite:///./bank.db
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## ▶️ Como Executar

```bash
# Instalar dependências
poetry install --no-root

# Rodar a aplicação
poetry run uvicorn src.main:app --reload
```

---

## 📚 Acessar a API

* Swagger: http://127.0.0.1:8000/docs
* OpenAPI: http://127.0.0.1:8000/openapi.json

---

## 🧪 Endpoints principais

### Auth

* `POST /auth/login`

### Conta

* `GET /accounts`
* `POST /accounts`
* `GET /accounts/{id}/transactions`

### Transações

* `POST /transactions`

---

## 🔄 Migrations com Alembic

```bash
# Criar migration
alembic revision --autogenerate -m "init"

# Aplicar migration
alembic upgrade head
```

---

## 📈 Melhorias Futuras

* PostgreSQL
* Docker
* Testes automatizados (Pytest)
* Deploy em cloud (Render, AWS)
* CI/CD

---

## 🎯 Objetivo

Projeto desenvolvido para:

* Prática de backend com Python
* Construção de APIs modernas com FastAPI
* Aplicação de arquitetura em camadas
* Composição de portfólio para vagas na área

---

## 📄 Licença

Uso livre para fins de estudo e aprimoramento profissional.
