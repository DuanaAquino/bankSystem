menu = """

[1] Deposit
[2] Withdraw
[3] Statement
[4] Quit

=> """

balance = 0
limit = 500
statement = ""
withdraw_number = 0
withdraw_limit = 3

while True:

    option = input(menu)

    if option == "1":
        amount = float(input("Informe o valor do depósito: "))

        if amount > 0:
            balance += amount
            statement += f"Depósito: R$ {amount:.2f}\n"

        else:
            print("A operação falhou. O valor informado é inválido.")
        
    elif option == "2":
        amount = float(input("Informe o valor do saque: "))

        balance_exceeded = amount > balance

        limit_exceeded = amount > limit

        withdraw_exceeded = withdraw_number >= withdraw_limit

        if withdraw_exceeded:
            print("A operação falhou. Você não possui saldo o suficiente.")

        elif limit_exceeded:
            print(" A operação falhou. O valor do saque excede o limite diário.")

        elif withdraw_exceeded:
            print("A operação falhou. O número máximo de saques foi excedido.")

        elif amount > 0:
            balance -= amount
            statement += f"Saque: R$ {amount:.2f}\n"
            withdraw_number += 1

        else:
            print("A operação falhou. O valor informado é inválido.")

    elif option == "3":
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~  e x t r a t o ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Não foram realizadas movimentações." if not statement else statement)
        print(f"\nSaldo: R$ {statement:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    elif option == "4":
        break

    else:
        print("Operação inválida. Por favor selecione novamente a operação desejada.")