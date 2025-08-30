# To-Do List API (Em desenvolvimento)
To-Do List é um projeto de lista de tarefas com o objetivo de aplicar conhecimentos em APIs.  
Foi desenvolvida com **SQLAlchemy** para manipulação do banco de dados e utiliza **Alembic** para migrações.  
O propósito deste projeto é criar uma API que permita ao usuário organizar suas atividades diárias, oferecendo funcionalidades para criar, ler, atualizar, excluir e finalizar tarefas.

### Tecnologias Utilizadas
- **Python 3.13.7**: Linguagem de programação principal
- **FastAPI**: Framework para desenvolvimento de APIs
- **SQLAlchemy**: Biblioteca ORM (Object-Relational Mapping) para interação com banco de dados
- **Alembic**: Ferramenta para gerenciar migrações de banco de dados
- **Uvicorn**: Servidor ASGI (Asynchronous Server Gateway Interface) para executar aplicações FastAPI
- **DBeaver**: Gerenciador multiplataforma para bancos de dados

---

### Estrutura do Projeto
A estrutura do projeto é organizada da seguinte forma:
```plaintext
backend_todolist/
  alembic/
    versions/              
    env.py                   
    README                   
    script.py.mako           

  project_todo_list/
    models/                  
      todo_list_model.py
    routers/
      todo_list_router.py
    schemas/
      schema.py
    
    shared/
      database.py
      dependencies.py
      exception.py
      exceptions_handler.py

  alembic.ini
  main.py
  requirements.txt -> arquivo com as dependências do projeto

frontend_todolist/
  public/
    index.html
  src/
    assets/
      img/
        logom.webp
    services/
      main.js
      message.js
  style/
    main.css
.gitignore

README.md
```
### Funcionalidades
-  A API permite que usuários possam:
    - Buscar todas as tarefas
    - Obter uma tarefa por ID
    - Criar uma nova tarefa
    - Atualizar uma tarefa por ID
    - Finalizar uma tarefa por ID
    - Excluir uma tarefa por ID
