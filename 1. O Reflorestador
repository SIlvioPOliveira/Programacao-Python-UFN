# 1. O Reflorestador (Loop com Acumulador)
# Em um mini-game de reflorestamento, o jogador deve plantar árvores até atingir uma meta de "Biomassa".
# Crie um programa que peça ao usuário a meta de biomassa (em unidades). Depois, use um while para ler
# sucessivamente o valor de biomassa de cada árvore plantada. O programa deve parar assim que a meta for
# atingida ou superada e exibir quantas árvores foram necessárias.

meta_biomassa = int(input("Digite a meta de biomassa: "))

biomassa_total = 0
quantidade_arvores = 0

while(biomassa_total < meta_biomassa):

  biomassa_da_vez = int(input("Digite a biomassa da arvore: "))

  biomassa_total += biomassa_da_vez
  quantidade_arvores += 1

  if biomassa_total < meta_biomassa:
    faltam = meta_biomassa - biomassa_total
    print(f"Total atual: {biomassa_total}")
    print(f"Faltam: {faltam} unidades de biomassa")
  else:
    print(f"-----Meta atingida ou superada!-----")
    print(f"Arvores plantadas: {quantidade_arvores}")
    print(f"Total de biomassa: {biomassa_total}")
