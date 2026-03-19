# 2. Simulador de Combate: Turnos de RPG
# Em um jogo de turno, um herói tem 100 de HP e enfrenta um monstro com 100 de HP.
# O programa deve pedir ao usuário o dano do ataque do herói e o dano do ataque do
# monstro por rodada. Use um while que continue enquanto ambos estiverem com HP
# acima de zero. Ao final de cada turno, mostre o HP restante de ambos. Se alguém
# chegar a 0, encerre e anuncie o vencedor.


player_hp = 100
enemy_hp = 100

while player_hp > 0 and enemy_hp > 0:
  
  player_damage = int(input("Digite o dano do ataque do jogador: "))
  enemy_damage = int(input("Digite o dano do ataque do inimigo: "))

  player_hp -= enemy_damage
  enemy_hp -= player_damage

  print(f"HP Herói: {player_hp} | HP Monstro: {enemy_hp}")

if player_hp <= 0 and enemy_hp <= 0:
  print("--- AMBOS CAÍRAM EM COMBATE! (EMPATE) ---")
elif player_hp <= 0:
  print("----- VITÓRIA DO MONSTRO -----")
else:
  print("----- VITÓRIA DO JOGADOR -----")
