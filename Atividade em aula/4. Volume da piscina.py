#4 - O volume de um cubo é determinado através do produto da área da base pela altura,
#    (mas as arestas do cubo possuem medidas iguais), então temos que:
#    V = Ab * a ou V = a * a * a → V = a³. A partir disso, faça um programa, adequando as variáveis
#    para receber medidas de uma piscina (altura, largura e comprimento), para responder o volume de
#    água necessário para enchê-la.


altura = int(input('Digite a altura da piscina: '))
largura = int(input('Digite a largura da piscina: '))
comprimento = int(input('Digite o comprimento da piscina: '))
V = (altura * largura)* comprimento
litros = V * 1000

print("O volume da piscina é: " + str(litros) + "L")

