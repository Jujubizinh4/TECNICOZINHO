vendas = [
    ("Melancia", 10, 8.50),
    ("Banana", 5,  12.00),
    ("Maça", 3, 6.0),
    ("Pamonha", 8, 7.5),
    ("Melancia", 7, 12.00)
]

#receita é o quanto foi vendido de cada item
contagem = {}
receita = {}

#o get significa coletar "(prduto, 0)" seria o nome do alimento, pc conta apartir do 0
for produto, qnt, valor in vendas:
    contagem[produto] = contagem.get(produto, 0) + 1
    receita[produto] = receita.get(produto, 0) + qnt * valor

for produto in contagem:
    print(f"{produto}: {contagem[produto]} vendas, receita total = R$ {receita[produto]}")