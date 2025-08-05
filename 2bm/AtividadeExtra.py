#partiu calcular sua Frequencia
Materia = input("Digite a Materia Desejada")
AulasSemanais = int(input("Digite suas Aulas Semanais"))
Semanas= 8
Bimestre = AulasSemanais*Semanas
FaltasObtidas = int(input("Me diga suas faltas"))
Presenca = Bimestre-FaltasObtidas
Resultado = Presenca*100/Bimestre

if Resultado >= 85:
    print("Boa")
else:
    print("Venha mais a Escola!")

print(Resultado)