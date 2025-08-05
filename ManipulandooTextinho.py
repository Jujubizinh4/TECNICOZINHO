<<<<<<< HEAD
with open('textinho.txt', 'w') as arquivinho:
    arquivinho.write("Ola Leitores!\n")
#usamos o "w" poq é de "write" (escrita)
#esse "n" serve para quebrar linha
    listas = ['O Principe Cruel ', 'O Rei peverso ', 'A Rainha do nada']
=======
with open('textinho.txt', 'w') as arquivinho:
    arquivinho.write("Ola Leitores!\n")
#usamos o "w" poq é de "write" (escrita)
#esse "n" serve para quebrar linha
    listas = ['O Principe Cruel ', 'O Rei peverso ', 'A Rainha do nada']
>>>>>>> d6cbc19e817919756f5335cd9c90ffc6cd60aca2
    arquivinho.writelines(listas)