# ToDo List (Em desenvolvimento)
Este é um projeto de uma aplicação de lista de tarefas (ToDo List), desenvolvida com FastAPI e SQLAlchemy. 
O objetivo deste projeto é criar uma API para ajudar a gerenciar tarefas, com funcionalidades de criação, leitura, atualização, exclusão e finalização das tarefas,
além da associação aos tipos de cada tarefa.

## Introdução
ToDo List é uma aplicação simples, que permite o usuário organizar suas atividades diárias. O projeto foi desenvolvido com o objetivo aplicar conhecimentos com API's, manipulação de banco de dados com **SQLAlchemy**, uso de migrações de banco de dados com **Alembic**.

## Tecnologias Utilizadas
- **Python 3.12.8**: Linguagem de programação principal.
- **FastAPI 0.115.4**: Framework para desenvolvimento de APIs.
- **SQLAlchemy 2.0.36**: Biblioteca ORM (Object-Relational Mapping) para interação com banco de dados.
- **Alembic 1.14.0**: Ferramente para gerenciamento de versões do banco de dados (migrações).
- **Pipenv**: Gerenciador de dependências virtual.
- **Pyenv**: Gerenciador de multiplas versões do Python.
- **Uvicorn**: Servidor ASGI para execução da aplicação FastAPI.
- **DBeaver**: Gerenciador de banco de dados universal.

## Estrutura do Projeto
- A estrutura do projeto é organizada da seguinte forma:
```plaintext
- alembic/
  - versions/                # Diretório das migrações do Alembic
  - env.py                   # Configuração do ambiente Alembic
  - script.py.mako           # Script de template para geração de migrações
  - README                   # Documentação sobre as migrações

- project_todo_list/
  - models/                  # Diretório dos modelos ORM
    - todo_client_model.py   # Modelo da lista dos tipos de tarefas
    - todo_list_model.py     # Modelo da lista de tarefas
  
  - routers/                 # Diretório das rotas da API
    - todo_client_router.py  # Rotas relacionadas aos tipos de tarefas
    - todo_list_router.py    # Rotas relacionadas a lista de tarefas
  
  - shared/                  # Diretório de arquivos compartilhados
    - database.py            # Configuração do banco de dados
    - dependencies.py        # Dependências do projeto
    - exception.py           # Arquivo para exceções personalizadas
    - exceptions_handler.py  # Manipulador de exceções

- alembic.ini                # Arquivo de configuração do Alembic
- main.py                    # Arquivo principal para rodar a aplicação
- Pipfile                    # Gerenciador de dependências (Pipenv)
- README.md                  # Documentação do projeto
```
## Funcionalidades
### A API permite que usuários sejam capazes de criar:
### - Tarefas (ToDo_List):
    - Buscar todas as tarefas;
    - Obter uma tarefa por ID:
    - Criar uma nova tarefa;
    - Consultar as tarefas existentes por ID;
    - Atualizar uma tarefa existente por ID;
    - Finalizar uma tarefa por ID;
    - Excluir uma tarefa por ID.

