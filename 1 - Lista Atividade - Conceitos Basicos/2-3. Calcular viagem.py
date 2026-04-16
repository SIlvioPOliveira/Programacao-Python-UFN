#2 - Faça um programa que ajude motoristas calcular e estimar viagens com diferentes tempos de viagem.
#    O programa deve receber do usuário do sistema (motorista) a distância a ser percorrida e o tempo
#    desejado da viagem. A partir disso, o programa deve calcular e exibir na tela a velocidade média
#    necessária.
#3 - Refaça o programa anterior (refatorar) para que o programa recebe a distância e a velocidade média,
#    mas calcule e exiba o tempo da viagem.


distancia = int(input('Digite a distancia a ser percorrida em KM: '))
velocidade_media = int(input('Digite a velocidade media em KM/H: '))
tempo = int(input('Digite o tempo desejado da viagem em horas: '))
calculo = distancia/tempo
tempo_viagem = distancia/velocidade_media
print("Deve dirigir a " + str(calculo) + " KM/H")
print("Deve levar " + str(tempo_viagem) + "h")