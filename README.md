# To-Do List API

**Descrição:**

Esta API RESTful foi desenvolvida em Python utilizando o framework FastAPI para criar uma aplicação completa de gerenciamento de tarefas. A aplicação permite aos usuários:

* **Criar usuários:** Cadastrar novos usuários com autenticação JWT.
* **Criar tarefas:** Adicionar novas tarefas à lista.
* **Ler tarefas:** Visualizar todas as tarefas ou tarefas específicas.
* **Editar tarefas:** Atualizar informações das tarefas existentes.
* **Deletar tarefas:** Remover tarefas da lista.

**Tecnologias Utilizadas:**

* **FastAPI:** Framework Python moderno.
* **Pydantic:** Biblioteca para validação de dados e geração de modelos de dados.
* **Pytest:** Framework de testes unitários para Python.
* **SQLite:** Banco de dados leve e embutido utilizado para armazenar as tarefas e usuários.
* **SQLAlchemy:** ORM (Object-Relational Mapper) para interagir com o banco de dados SQLite.
* **Alembic:** Ferramenta para gerenciamento de migrações de banco de dados.
* **Docker:** Plataforma de containerização para criar um ambiente de desenvolvimento e produção consistente.
* **JWT:** JSON Web Tokens para autenticação de usuários.

**Estrutura do Projeto:**

* **models:** Contém os modelos de dados utilizando Pydantic.
* **schemas:** Define os esquemas de entrada e saída das APIs.
* **database:** Contém as configurações do banco de dados e as funções para interagir com ele.
* **auth.py:** Arquivo principal das regras de autenticação.
* **main.py:** Arquivo principal da aplicação FastAPI.
* **tests:** Diretório com os testes unitários.

**Como Executar:**

1. **Pré-requisitos:**
   * Docker instalado e em execução.
   * Python e pip instalados.

2. **Clonar o repositório:**
   ```bash
   git clone https://github.com/thiagosnx/todo.git
   ```
3. **Construir a imagem Docker:**
    ```bash
    cd todo
    ```
    ```bash
    docker build -t todo .
     ```

4. **Executar o container:**
   ```bash
   docker run -d -p 9000:8000 --name apis to-do-api
   ```

5. **Acessar a API:**
   [http://localhost:9000/docs](http://localhost:9000/docs)

6. **Rodar os testes unitários:**
    ```bash
   docker exec apis pytest tests/
    ```
   
   