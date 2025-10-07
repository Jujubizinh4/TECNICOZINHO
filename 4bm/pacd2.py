#mais um mini banco pra conta

SaldoInicial = float(input("Qual Valor inicial?"))
Estado = True
while Estado ==True:
    escolha = int(input("1.Visualizar\n 2.Depositar\n 3.Sacar\n 4.Sair"))
    if escolha ==1:
        visualizar = print(SaldoInicial)
    if escolha ==2:
        depositar = int(input("Quanto Gostaria de Depositar?"))
        SaldoInicial=   SaldoInicial + depositar
        print (SaldoInicial)
    if escolha ==3:
        saque = float(input("Quanto Gostaria de Sacar?"))
        juros = (SaldoInicial - saque) * 0.02
        SaldoInicial = SaldoInicial - saque - juros
        print(SaldoInicial)
    if escolha ==4:
        Estado = False
        print(f"Seu valor atual é : {SaldoInicial}")