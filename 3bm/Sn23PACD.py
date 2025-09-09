ano = 2025
nascimento = int(input("ano do seu nascimento"))
idade = 0
while ano > nascimento:
    idade = idade + 1
    ano = ano - 1

print("Sua idade é", idade)