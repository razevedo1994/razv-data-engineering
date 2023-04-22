# Processamento de dados com AWS lambda

# O Projeto

O projeto consiste em uma aplicacao para controle de financas pessoais onde teremos o fluxo de dados transacionais e analiticos, é
um projeto simples porém com funcionalidade suficientes para exercitar as principais features de uma API e praticas de Engenharia de Dados.

Vamos focar no backend, ou seja, na API e no fluxo de processamento de dados.

### myfinance-api (Web API com FastAPI)

## Requisitos

- Computador com Python 3.10
- Docker & docker-compose
- Um editor de códigos como VSCode, Sublime, Vim, Micro

> **importante**: Os comandos apresentados serão executados em um terminal Linux, se estiver no Windows recomendo usar o WSL, uma máquina virtual ou um container Linux, ou por conta própria adaptar os comandos necessários.

## Ambiente

Primeiro precisamos de um ambiente virtual para instalar
as dependencias do projeto.

```console
python -m venv .venv
```

E ativaremos a virtualenv

```console
# Linux
source .venv/bin/activate
# Windows Power Shell
.\venv\Scripts\activate.ps1
```

Vamos instalar ferramentas de produtividade neste ambiente e para isso vamos criar um arquivo chamado
requirements-dev.txt


```
ipython         # terminal
ipdb            # debugger
sdb             # debugger remoto
pip-tools       # lock de dependencias
pytest          # execução de testes
pytest-order    # ordenação de testes
httpx           # requests async para testes
black           # auto formatação
flake8          # linter
```

Instalamos as dependencias iniciais.

```console
pip install --upgrade pip
pip install -r requirements-dev.txt
```

## Estrutura de pastas e arquivos

Script para criar os arquivos do projeto.

```bash
# Arquivos na raiz
touch setup.py
touch {settings,.secrets}.toml
touch {requirements,MANIFEST}.in
touch Dockerfile.dev docker-compose.yaml

# Imagem do banco de dados
mkdir postgres
touch postgres/{Dockerfile,create-databases.sh}

# Aplicação
mkdir -p myfinance/{models,routes}
touch myfinance/default.toml
touch myfinance/{__init__,cli,app,auth,db,security,config}.py
touch myfinance/models/{__init__,expense_category,user,financial_expense}.py
touch myfinance/routes/{__init__,auth,expense_category,user,financial_expense}.py

# Testes
touch test.sh
mkdir tests
touch tests/{__init__,conftest,test_api}.py
```