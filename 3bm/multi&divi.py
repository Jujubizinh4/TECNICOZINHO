#temos que  multiplicar numeros ;3
print("partiu calcular?")
continuar = "s"
 
while continuar == "s":
    operador = input("escolha seu operador: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número:"))
    # verificação e cálculo
    if operador == "*":
        resultado = num1 * num2
        print(resultado)
    else:
        if operador == "/":
            resultado = num1 / num2
            print("Resultado:", resultado)
 
    continuar = input("Deseja fazer outra conta? (s/n): ")
print("Encerrando a calculadora...")