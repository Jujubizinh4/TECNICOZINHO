money=(2000)
print("Escolha:\n 1. Sacar\n 2. Depositar\n 3. Sair")
n1 = int(input())
while n1 != 3:
    if n1 == 1:
        print("saque seu dinheiro aq")
        saque = int(input())
        money = (money - saque)
        print(money)
        print("Escolha:\n 1. Sacar\n 2. Depositar\n 3. Sair")
        n1 = int(input())
    elif n1 == 2:
        print("Deposite seu Dinheiro")
        depositando= int(input())
        money = depositando + money
        print (money)
        print("Escolha:\n 1. Sacar\n 2. Depositar\n 3. Sair")
        n1 = int(input())    
if n1 == 3:
    print("Obrigado, seu saldo final é de", money)