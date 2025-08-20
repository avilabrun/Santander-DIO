# Santander-DIO

Este projeto irá tratar sobre o **BootCamp de Python do Santander 2025** em conjunto com a **DIO**.
O objetivo será criar um sistema bancário na linguagem Python.

## Informações Gerais

### Linguagem utilizada

A linguagem principal a ser utilizada no projeto será o ***Python***.

### Pré requisitos

O principal pré requisito para execução do projeto é possuir a linguagem Python instalada.

### Requisitos para o sistema

O objetivo é criar uma aplicação, separando as funções existentes de **saque**, **depósito** e **extrato** em funções.
Iremos também criar as funções **cadastrar usuário(cliente)** e **cadastrar conta bancária**.

### Requisitos para as funções

- Saque: Deve receber argumentos apenas por nome (keyword only)
    Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite saques
    Sugestão de retorno: saldo e extrato

- Depósito: receber argumentos apenas por posição (positional only)
    Sugestão de argumentos: saldo, valor, extrato
    Sugestão de retorno: saldo e extrato

- Extrato: recebe postional only (saldo) e keyword only (extrato).

- Cadastrar usuário (cliente): Armazena usuários em uma lista. o usuário é composto por nome, nascimento, cpf e endereço, este sendo uma string com formato: "Logradouro, número - Bairro - cidade/sigla estado. **Não é permitido mais de um usuário para cada CPF**

- Cadastrar conta bancária: Armazena as contas em uma lista. A conta é composta por agência (0001), Conta (sequencial, iniciando em 1) e Usuário (CPF do cliente). É permitido o usuário possuir mais de uma conta, mas uma conta pertence a apenas um usuário.