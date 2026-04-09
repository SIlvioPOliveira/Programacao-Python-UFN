#7 - Faça um programa Python que receba duas notas, calcule a média aritmética e mostre o resultado.
#    Além disso, deve mostrar ao lado da média Aprovado (se média >= 7.0) Reprovado (se média <= 3.0),
#    Exame (se média entre 3.0 e 7.0)



n1 = int(input("Digite a nota 1: "))
n2 = int(input("Digite a nota 2: "))

media = (n1 + n2) / 2

if media >= 7.0:
  print("Aprovado")
if media <= 3.0:
  print("Reprovado")
if media > 3.0 and media < 7.0:
  print("Exame")
