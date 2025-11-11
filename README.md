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
| **Backend** | Python (funcional) | Linguagem de propósito geral, com foco em clareza, imutabilidade e funções puras. | Conclúido |
| | Flask | Micro-framework leve, ideal para iniciar APIs de forma rápida e modular. | Conclúido |
| | SQLite | Banco de dados relacional para persistência local inicial. | Conclúido |
| **Frontend** | React + TS | Biblioteca moderna com tipagem estática, aumentando a manutenibilidade. | Pendente |
| | Tailwind CSS | Framework de CSS *utility-first* para desenvolvimento rápido e responsivo | Pendente |
| **Qualidade** | `pytest` | Ferramenta padrão para testes unitários em Python. | Conclúido |

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
| `/tarefas/<id>` | GET | Busca uma tarefa específica por ID. |  **Concluída** |
| `/tarefas/<id>` | PUT | Atualiza o status/dados de uma tarefa. |  **Concluída** |
| `/tarefas/<id>` | DELETE | Remove uma tarefa. |  **Concluída** |

## Product Backlog (Próximos Passos)

1. **[Frontend]** Definir o setup inicial do Frontend (React, TypeScript, tailwind(CSS)).
2. **[Frontend]** Criar o componente de listagem de tarefas (`GET /tarefas`).
3. **[Frontend]** Criar componente de formulário para adicionar novas tarefas (`POST /tarefas`).
4. **[Frontend]** Implementar a funcionalidade de marcar/desmarcar (atualizar `status` via `PUT`).
5. **[Frontend]** implementar a funcionalidade de excluir tarefas (`DELETE /tarefas/<id>`).
2. **[Integração]** Conectar o Frontend às rotas `POST` e `GET` para criar e listar as tarefas.