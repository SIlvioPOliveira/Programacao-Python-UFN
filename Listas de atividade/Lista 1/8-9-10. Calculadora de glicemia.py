T#8 - Faça um programa em Python que manipule listas com números inteiros, representando
#    valores de glicemia (45 a 450) de um doente diabético. O programa deve receber valores de
#    glicemia (um a um) até que o usuário não queira mais cadastrá-los. Os dados digitados
#    devem ser inseridos na lista listaDadosOriginais.
#9 - Faça uma adição/complemento no código anterior para mostrar os valores de glicemia
#    da listaDadosOriginais, um abaixo do outro.
#10 - Faça um complemento no código anterior para copiar a listaDadosOriginais para a
#     listaDadosOrdenados, que na sequência precisa ser ordenada.
listaDadosOriginais = []

while True:
    entrada = input("Digite a glicemia (Valor vazio pra sair): ")

    if not entrada:
        break

    glicemia = int(entrada)

    if 45 <= glicemia <= 450:
        listaDadosOriginais.append(glicemia)
    else:
        print("Valor inválido! Digite entre 45 e 450.")

print("\n--- Valores Originais ---")
for valor in listaDadosOriginais:
    print(valor)

listaDadosOrdenados = listaDadosOriginais[:]
listaDadosOrdenados.sort()

print("\n--- Valores Ordenados ---")
print(listaDadosOrdenados)





