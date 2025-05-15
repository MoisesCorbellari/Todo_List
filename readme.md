# ToDo List (Em desenvolvimento)
ToDo List é um projeto de lista de tarefas (ToDo List), com o objetivo aplicar conhecimentos com API's, 
desenvolvida com **SQLAlchemy** para manipulação de banco de dados, uso de migrações de banco de dados com **Alembic**.
O objetivo deste projeto é criar uma API que permite o usuário organizar suas atividades diárias, com funcionalidades de criação, leitura, atualização, exclusão e finalização das tarefas.

## Tecnologias Utilizadas
- **Python 3.13.3**: Linguagem de programação principal.
- **FastAPI**: Framework para desenvolvimento de APIs.
- **SQLAlchemy**: Biblioteca ORM (Object-Relational Mapping) para interação com banco de dados.
- **Alembic**: Ferramente para gerenciamento de versões do banco de dados (migrações).
- **Uvicorn**: Servidor ASGI para execução da aplicação FastAPI.
- **DBeaver**: Gerenciador multiplataforma e universal de bancos de dados.

## Estrutura do Projeto
- A estrutura do projeto é organizada da seguinte forma:
```plaintext
- alembic/
  - versions/                
  - env.py                   
  - README                   
  - script.py.mako           

- project_todo_list/
  - models/                  
    - todo_list_model.py
  
  - routers/
    - todo_list_router.py
  
  - shared/
    - database.py
    - dependencies.py
    - exception.py
    - exceptions_handler.py

- alembic.ini
- main.py
- README.md
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
