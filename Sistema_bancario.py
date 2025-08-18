menu = """

# Sistema Bancario - Menu Principal
[ 1 ] Depositar
[ 2 ] Sacar
[ 3 ] Consultar Extrato
[ 0 ] Sair

Digite a opção desejada: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        valor_deposito = float(input("Informe o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")

        else:
            print("Valor inválido para depósito!")
    
    elif opcao == "2":
        valor_saque = int(input("Informe o valor do saque: "))
        if valor_saque <= 0:
            print("Valor informado inválido para operações de saque!")
        elif valor_saque > saldo:
            print("Saldo insuficiente para operação")
        elif valor_saque > limite:
            print("Valor informado acima do limite permitido para operações de saque!")
        
        else:
            if numero_saques >= LIMITE_SAQUES:
                print("Número de saques diários excedido.")
            else:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
            
        print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")

    elif opcao == "3":
        print("\n************** EXTRATO **************")
        print(extrato)
        print("\n*************************************")
        print(f"Saldo:         R$ {saldo:.2f}\n")
        print("\n*************************************")
    
    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Opção inválida, por favor tente novamente.")