# gerenciador_tarefas
Projeto de formação Fullstack com foco em Python Funcional, React, TS e QA.

<p align="center">
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow" alt="Status do Projeto">
  <img src="https://img.shields.io/badge/Metodologia-Scrum%20%2F%20Funcional-blue" alt="Metodologia">
</p>

## Visão Geral e Justificativa (Visão do Produto)
Este projeto serve como ambiente de aprendizado profissional e prático para o desenvolvimento Fullstack com o foca em arquitetura **funcional** (sem o uso de POO/classes para a lógica do négocio). O objetivo principal é dominar os conceitos de:
1. **Imutabilidade e Funções Puras** no backend
2. **Tipagem Estatica** Typescript no Frontend
3. **Qualidade** (Testes) e **Processo Ágil** (Scrum/QA)

## Tecnologias Utilizadas
| Categorias | Tecnologias | Justificativa | Status |
| :--- | :--- | :--- | :--- |
| **Backend** | Python (funcional) | Linguagem de propósito geral, com foco em clareza, imutabilidade e funções puras. | Em implementação |
| | Flask | Micro-framework leve, ideal para iniciar APIs de forma rápida e modular. | Em Implementação |
| | SQLite | Banco de dados relacional para persistência local inicial. | pendente |
| **Frontend** | React + TS | Biblioteca moderna com tipagem estática, aumentando a manutenibilidade. | Pendente |
| | Tailwind CSS | Framework de CSS *utility-first* para desenvolvimento rápido e responsivo | Pendente |
| **Qualidade** | `pytest` | Ferramenta padrão para testes unitários em Python. | Pendente |

## Configurações do Ambiente de Desenvolvimento

### Pré-requisitos
* Python 3.14
* Node.js 18+ (para o Frontend)
* VS Code

### backend(python)
1. Navegue atá a pasta `backend\`: `cd backend`
2. Crie um ambiente virtual: `python -m venv .venv`
3. Ative o ambiente: `.\.venv\Scripts\activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Rode o servidor: `python app.py`



## Product Backlog (Próximos Passos)

1. Definir estrutura de diretórios funcional (Backend)
2. **Módulo 1: Lógica - Fundamentos Funcionais em Python.**
3. Implementar a primeira Rota da API com Flask e Lógica Funcional.


## Endpoints da API (Backend - Flask)

| Rota | Método | Descrição | Status |
| :--- | :--- | :--- | :--- |
| `/tarefas` | **POST** | Cria uma nova tarefa no banco de dados. | **Concluída** |
| `/tarefas` | GET | Lista todas as tarefas. | **Concluída** |
| `/tarefas/<id>` | GET | Busca uma tarefa específica por ID. |  Pendente |
| `/tarefas/<id>` | PUT | Atualiza o status/dados de uma tarefa. |  Pendente |
| `/tarefas/<id>` | DELETE | Remove uma tarefa. |  Pendente |

## Product Backlog (Próximos Passos)

1. **[QA]** Adicionar Testes Unitários com `pytest` para `database.py` e rotas `POST` e `GET`. (prioridade máxima)  
2. **[Backend]** Implementar a função e rota **GET /tarefas/<id>**, `PUT /tarefas/<id>` e `DELETE /tarefas/<id>`.
3. **[Frontend]** Definir o setup inicial do Frontend (React, TypeScript, tailwind(CSS)).
4. **[Integração]** Conectar o Frontend às rotas `POST` e `GET` para criar e listar as tarefas.