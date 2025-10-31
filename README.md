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
* Python 3.14
* Node.js 18+ (para o Frontend)
* VS Code

## Product Backlog (Próximos Passos)

1. Definir estrutura de diretórios funcional (Backend)
2. **Módulo 1: Lógica - Fundamentos Funcionais em Python.**
3. Implementar a primeira Rota da API com Flask e Lógica Funcional.


## Endpoints da API (Backend - Flask)

| Rota | Método | Descrição | Status |
| :--- | :--- | :--- | :--- |
| `/tarefas` | **POST** | Cria uma nova tarefa no banco de dados. | **Concluída** |
| `/tarefas` | GET | Lista todas as tarefas. | Em desenvolvimento |
| `/tarefas/<id>` | GET | Busca uma tarefa específica por ID. |  Pendente |
| `/tarefas/<id>` | PUT | Atualiza o status/dados de uma tarefa. |  Pendente |
| `/tarefas/<id>` | DELETE | Remove uma tarefa. |  Pendente |

## Product Backlog (Próximos Passos)

1.  Implementar a função e rota **GET /tarefas** (Listar todas as tarefas).
2.  Adicionar Testes Unitários com `pytest` para as funções do Backend.
3.  Definir o setup inicial do Frontend (React, TypeScript, Tailwind CSS).