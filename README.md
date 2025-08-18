# Santander-DIO

Este projeto irá tratar sobre o **BootCamp de Python do Santander 2025** em conjunto com a **DIO**.
O objetivo será criar um sistema bancário na linguagem Python.

## Informações Gerais

### Linguagem utilizada

A linguagem principal a ser utilizada no projeto será o ***Python***.

### Pré requisitos

O principal pré requisito para execução do projeto é possuir a linguagem Python instalada.

### Requisitos para o sistema

Para o Desafio 01, devemos implementar 3 operações: ***Depósito***, ***Saque*** e ***Extrato***.
Nesta versão, o sistema irá trabalhar apenas com **1 usuário**, não sendo preciso identificar qual é a agência e conta. 

 - *Depósito:*
        Os depósitos serão armazenados em uma variável
        O sistema deve permitir apenas valores positivos

 - *Saque:*
        O sistema deve limitar a 3 saques diários
        O valor máximo de saque é R$ 500,00 por saque
        O sistema deve exibir uma mensagem quando o saldo não for suficiente para o saque
        Todos os sques devem ser armazenados em uma variável

 - *Extrato:*
        O extrato deverá listar todos depósitos e saques realizados
        No fim da listagem deve ser exibido o saldo atual
        O formato de exibição deverá ser "R$ xxxx.xx"