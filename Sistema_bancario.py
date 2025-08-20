from datetime import date, datetime

# cadastrar usuário
# cadastrar agencia e conta

# vincular conta ao usuário
# modularizar o código


# Saque
    # função saque recebe argumentos apenas por nome ('saque(valor = variavel)')
        # entrada: saldo, valor, extrato, limite, numero_saques, 	limite_saques
        # saída: saldo e extrato

# Depósito
    # recebe argumentos por posição (variável)
        # entrada: saldo, valor e extrato
        # saída: saldo e extrato

# Extrato
    # recebe argumentos posicionais e por nome

# Cadastrar usuário
    # Nome, Nascimento, CPF e Endereço (Rua, N - Bairro - Cidade/Estado)
    # CPF recebe apenas numeros
    # Não podem ser usados CPFs repetidos

# Cadastrar Contas
    # Cada conta é vinculada a um usuário, que pode possuir mais contas
    # Agência: 0001
    # Contas tem numeração única


def menu():
    menu = """
    Olá!
    Informe o serviço desejado entre as opções:

        1 - Cadastrar usuário
        2 - Cadastrar conta
        3 - Listar contas
        4 - Consultar Saldo
        5 - Extrato
        6 - Saque
        7 - Depósito
        
        0 - Sair

    => """
    
    return int(input(menu))

def cadastrar_usuario(usuarios):
    pass

def filtrar_usuario(cpf, usuarios):
    pass

def cadastrar_conta(usuarios, contas):
    pass

def listar_contas(contas):
    pass

def consultar_saldo(conta):
    pass

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    pass

def depositar(saldo, valor, extrato):
    pass

def exibir_extrato(saldo, extrato, /, *, data=None):
    pass

def main():
    pass

main()