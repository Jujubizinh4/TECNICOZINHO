print("bora fazer umas continhas?")
print("Escolha:\n 1.Somar\n 2.Subtrair\n 3.SAIR")
n1 = int(input())
while n1 != 3:
    if n1 == 1:
        number1 = int(input("1º Número:"))
        number2 = int(input("2º Número:"))
        Resultado = number1+number1
        print(Resultado)
        print("Escolha:\n 1.Somar\n 2.Subtrair\n SAIR")
        n1 = int(input())
    elif n1 == 2:
        number3 = int(input("1º Número:"))
        number4 = int(input("2º Número:"))
        Resultado = number3 - number4
        print(Resultado)
        print("Escolha:\n 1.Somar\n 2.Subtrair\n SAIR")
        n1 = int(input())
if n1 == 3:
    print("GoodBye")
