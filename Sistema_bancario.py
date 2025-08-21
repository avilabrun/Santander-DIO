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

def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF (somente números): ")
    
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada para o usuário informado!")
        print(f"Agência: {agencia} - Conta: {numero_conta}")
        
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        
    # else:
    print("\nUsuário não cadastrado. Por favor cadastre um usuário.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Titular: {conta['usuario']['nome']}
            Agência: {conta['agencia']} - Conta: {conta['numero_conta']}
        """
    print(linha)

def consultar_saldo(saldo):
    print(f"\nSaldo:         R$ {saldo:.2f}")

def sacar(*, saldo, valor, extrato, limite_saque, numero_saques, saques_diarios):
    mascara_ptbr = '%d/%m/%Y %H:%M'
    
    saldo_excedido = valor > saldo # Checa se existe saldo disponível
    limite_excedido = valor > limite_saque # checa se o valor do saque é maior que o limite permitido
    saques_exedidos = numero_saques >= saques_diarios # checa se o número de saques diários foi excedido

    if saques_exedidos:
        print("\nLimite de saques diários excedidos.")

    elif valor < 0:
        print("Valor informado inválido para a operação.")
    
    elif limite_excedido:
        print(f"\nLimite de saque excedido para a operação. (Limite atual: R$ {limite_saque:.2f})")
    
    elif saldo_excedido:
        print(f"\nSaldo insuficiente para a operação. Saldo atual: R$ {saldo}")

    else:
        saldo -= valor
        numero_saques += 1

        hora = datetime.now()
        extrato += f"{hora.strftime(mascara_ptbr)} - Saque:         R$ {valor:.2f}\n" # Registra extrato

    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    mascara_ptbr = '%d/%m/%Y %H:%M'
    
    if valor > 0:
        saldo += valor

        hora = datetime.now()
        extrato += f"{hora.strftime(mascara_ptbr)} - Depósito:      R$ {valor:.2f}\n" # Registra extrato

        print("Depósito realizado com sucesso!")

    else:
        print("Valor informado inválido para a operação.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n***************** EXTRATO *****************")
    print(extrato if extrato else "Não foram realizadas operações.")
    print("\n*******************************************")
    print(f"Saldo:         R$ {saldo:.2f}")
    print("\n*******************************************")

def main():
    usuarios = []

    AGENCIA = "0001"
    contas = []

    saldo = 0
    extrato = ""

    limite_saque = 500
    numero_saques = 0

    SAQUES_DIARIOS = 3
    
    while True:
        options = menu()

        if options == 1: # Cadastrar usuário
            cadastrar_usuario(usuarios)

        elif options == 2: # Cadastrar conta
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif options == 3: # Listar contas
            listar_contas(contas)

        elif options == 4: # Consultar saldo
            consultar_saldo(saldo)
        
        elif options == 5: # Consultar extrato
            exibir_extrato(saldo, extrato=extrato)

        elif options == 6: # Sacar
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_saque=limite_saque,
                numero_saques=numero_saques,
                saques_diarios=SAQUES_DIARIOS,
            )

        elif options == 7: # Depositar
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif options == 0: # Sair
            print("Obrigado por usar nossos serviços!")
            break

        else:
            print("Opção invalida!\nPor favor insira uma opção válida.")


main()