try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ValueError:  #Value - valor Error - erro
    print("Você não digitou um número valido")
except ZeroDivisionError:
    print("Não é possivel dividir por zero.")
else:
    print("Nenhuma exceção ocorreu.")
finally:
    print("Este bloco sempre será executado")