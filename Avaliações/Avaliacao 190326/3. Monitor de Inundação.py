# 3. Monitor de Inundação (Sentinela)
# Você está desenvolvendo um sistema de alerta para uma Smart City. O programa deve ler o nível do rio (em metros) continuamente.

# * Se o nível for menor que 3m: "Estado Normal".
# * Entre 3m e 5m: "Estado de Alerta".
# * Acima de 5m: "Evacuação Imediata".
# O programa só deve encerrar a leitura se o usuário digitar um valor negativo (flag/bandeira de encerramento).

estado_de_perigo = ['Normal', 'Alerta', 'Evacuacao']

  
while (True):
  entrada = input("Digite o nível do rio em metros(Valor vazio pra sair): ")

  if not entrada:
    print("----- FIM DO PROGRAMA -----")
    break

  nivel_rio = int(entrada)
  
  if nivel_rio < 3:
    indice_estado = 0

  if nivel_rio >= 3 and nivel_rio <= 5:
    indice_estado = 1

  if nivel_rio > 5:
    indice_estado = 2

  print(f"----- {estado_de_perigo[indice_estado]} -----")
