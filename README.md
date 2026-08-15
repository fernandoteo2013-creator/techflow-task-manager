# 🚀 TechFlow Task Manager

## 📖 Sobre o Projeto (Objetivo)
A TechFlow Solutions foi contratada para desenvolver um sistema de gerenciamento de tarefas baseado em metodologias ágeis para uma startup de logística. O principal objetivo deste sistema é permitir que o cliente acompanhe o fluxo de trabalho da sua equipe em tempo real, priorize tarefas críticas e monitore o desempenho geral.

Este repositório contém a simulação do desenvolvimento desse sistema, aplicando conceitos de Engenharia de Software, gestão ágil, controle de qualidade e integração contínua[cite: 1].

## 🎯 Escopo Inicial
O projeto consiste em uma aplicação web básica para gestão de tarefas, composta por:
*   **API REST (Back-end):** Desenvolvida com FastAPI, fornecendo endpoints para criação (`POST`), listagem (`GET`), atualização de status (`PATCH /tasks/{id}/status`) e exclusão (`DELETE`) de tarefas.
*   **Interface Visual (Front-end):** Desenvolvida em React, consumindo a API e exibindo as tarefas em um formato de quadro interativo.
*   **Controle de Qualidade:** Testes automatizados cobrindo os endpoints principais (CRUD)[cite: 1].
*   **CI/CD:** Pipeline configurado via GitHub Actions para execução automática de testes a cada nova alteração no código[cite: 1, 2].

## 🔄 Metodologia Ágil (Kanban)
Para o gerenciamento deste projeto, adotamos a metodologia **Kanban** integrada diretamente ao **GitHub Projects**[cite: 1, 2]. 
*   **Três colunas, um fluxo:** As tarefas estão organizadas nas colunas *A Fazer* (To Do), *Em Progresso* (In Progress) e *Concluído* (Done), permitindo entender o estado do projeto num relance[cite: 1, 2].
*   **Cartão como unidade de valor:** Cada cartão no quadro corresponde a uma *issue* real no repositório, contendo prioridade, estimativa em pontos e o responsável.
*   **Rastreabilidade e Auditoria:** Como a gestão ocorre junto ao código, toda mudança de status fica registrada, e é possível ligar um commit diretamente à issue que ele resolve.

## ⚠️ Gestão de Mudanças (Mudança de Escopo)
Durante o ciclo de desenvolvimento, identificou-se uma nova necessidade de negócio que exigiu uma adaptação no escopo inicial do projeto[cite: 1].

*   **Alteração solicitada:** Adicionar o campo "responsável" (assignee) ao modelo de Tarefa.
*   **Justificativa:** A startup de logística percebeu que, com o aumento da equipe, apenas rastrear o status da tarefa não era suficiente; era crucial saber quem estava executando a ação para evitar gargalos na operação.
*   **Impacto no Kanban:** Uma nova *issue* foi adicionada ao backlog, o diagrama de classes foi atualizado e o código modificado para refletir a nova estrutura de dados.

## 🛠️ Como Executar o Projeto
1. Clone este repositório: `git clone https://github.com/SEU_USUARIO/techflow-task-manager.git`
2. Navegue até a pasta do projeto: `cd techflow-task-manager`
3. Instale as dependências do back-end e front-end (conforme documentação interna nas pastas `/src`).
4. Execute os testes localmente usando `pytest`.
