with open('textinho.txt', 'w') as arquivinho:
    arquivinho.write("Ola Leitores!\n")
#usamos o "w" poq é de "write" (escrita)
#esse "n" serve para quebrar linha
    listas = ['O Principe Cruel ', 'O Rei peverso ', 'A Rainha do nada']
    arquivinho.writelines(listas)