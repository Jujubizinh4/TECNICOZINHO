def busca_linear(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return - 1

lista = ["chocolate branco", "chocolate ao leite", "ovomaltine"]
elemento = "chocolate ao leite"
indice = busca_linear(lista,elemento)
print(f"Escolha seu Chocolate '{elemento}' encontrado no mercado {indice}" if indice != -1 else "nao encontrou")