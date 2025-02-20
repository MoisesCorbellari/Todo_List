# ToDo List (Em desenvolvimento)
ToDo List é um projeto de lista de tarefas (ToDo List), com o objetivo aplicar conhecimentos com API's, 
desenvolvida com **SQLAlchemy** para manipulação de banco de dados, uso de migrações de banco de dados com **Alembic**.
O objetivo deste projeto é criar uma API que permite o usuário organizar suas atividades diárias, com funcionalidades de criação, leitura, atualização, exclusão e finalização das tarefas.

## Tecnologias Utilizadas
- **Python 3.12.8**: Linguagem de programação principal.
- **FastAPI**: Framework para desenvolvimento de APIs.
- **SQLAlchemy**: Biblioteca ORM (Object-Relational Mapping) para interação com banco de dados.
- **Alembic**: Ferramente para gerenciamento de versões do banco de dados (migrações).
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
    - todo_list_model.py     # Modelo da lista de tarefas
  
  - routers/                 # Diretório das rotas da API
    - todo_list_router.py    # Rotas relacionadas a lista de tarefas
  
  - shared/                  # Diretório de arquivos compartilhados
    - database.py            # Configuração do banco de dados
    - dependencies.py        # Dependências do projeto
    - exception.py           # Arquivo para exceções personalizadas
    - exceptions_handler.py  # Manipulador de exceções

- alembic.ini                # Arquivo de configuração do Alembic
- main.py                    # Arquivo principal para rodar a aplicação
- README.md                  # Documentação do projeto
```
## Funcionalidade
### A API permite que usuários sejam capazes de criar:
### - Tarefas (ToDo_List):
    - Buscar todas as tarefas;
    - Obter uma tarefa por ID:
    - Criar uma nova tarefa;
    - Consultar as tarefas existentes por ID;
    - Atualizar uma tarefa por ID;
    - Finalizar uma tarefa por ID;
    - Excluir uma tarefa por ID.
