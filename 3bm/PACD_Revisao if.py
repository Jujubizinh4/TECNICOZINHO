print("você precisa ou não pagar imposto? Descubra já")
salario = int(input("Digite o seu salario:"))
if salario >= 5000:
    print("Vossa senhoria necessitas pagar imposto")
else:
    print("Vossa senhoria nao necessitas pagar imposto, ganhas miseraveis",salario)