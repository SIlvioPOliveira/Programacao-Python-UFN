# 4. O Coletor de Itens e Inventário
# Em um jogo de exploração, o jogador tem uma mochila com capacidade máxima de 
# 15kg. Crie um programa que peça o peso de cada item encontrado no cenário, um 
# por um. O while deve permitir a entrada de itens enquanto o peso total não 
# ultrapassar 15kg. Se um item ultrapassar o limite, o programa deve avisar 
# "Mochila cheia, item descartado" e encerrar, mostrando o peso final total.

peso_total = 0

while peso_total < 15:
  peso_item = int(input("Digite o peso do item: "))
  peso_total += peso_item
  if peso_total > 15:
    print("Mochila cheia, item descartado")
    peso_total -= peso_item
    break

print(f"Peso total: {peso_total}")
