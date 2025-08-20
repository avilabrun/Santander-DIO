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
    cpf = input("\nInforme o CPF (somente números): ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com o CPF informado!")
        return

    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a Data de Nascimento: ")
    endereco = input("Informe o endereço (logradouro, número, bairro, sigla da cidade/sigla do estado): ")

    usuarios.append({"nome" : nome, "nascimento" : nascimento, "cpf": cpf, "endereco" : endereco})

    print("\nUsuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    # List comprehension para filtrar usuários
    usuarios_filtrados = []
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuarios_filtrados.append(usuario)
    
    # Retorna o primeiro usuário encontrado ou None se não houver
    if len(usuarios_filtrados) > 0:
        return usuarios_filtrados[0] 
    else:
        return None

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
    usuarios = []
    contas = []

    while True:
        options = menu()

        if options == 1: # Cadastrar usuário
            cadastrar_usuario(usuarios)

        elif options == 2: # Cadastrar conta
            cadastrar_conta()

        elif options == 3: # Listar contas
            listar_contas()

        elif options == 4: # Consultar saldo
            consultar_saldo()
        
        elif options == 5: # Consultar extrato
            exibir_extrato()

        elif options == 6: # Sacar
            pass

        elif options == 7: # Depositar
            pass

        elif options == 0: # Sair
            print("Obrigado por usar nossos serviços!")
            break

        else:
            print("Opção invalida!\nPor favor insira uma opção válida.")


main()