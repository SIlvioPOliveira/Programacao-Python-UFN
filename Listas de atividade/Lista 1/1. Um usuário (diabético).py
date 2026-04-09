#1 - Um usuário (diabético) de insulina rápida precisa fazer uso do medicamento sempre que for realizar
#    uma refeição. Assim, faça um programa que receba do usuário sua glicemia do momento (mg/dl),
#    meta pré-refeição (em geral é 100 mg/dl), fator de sensibilidade (valor inteiro entre 20 a 60).
#    A partir desses valores, o programa deve calcular e exibir para o usuário a quantidade de insulina
#    que ele deverá administrar baseada na equação:
#    quantidade_insulina = (glicemia_do_momento - meta_pre_refeicao) / fator_sensibilidade


glicemia_do_momento = int(input('Digite a glicemia do momento: '))
meta_pre_refeicao = 100
fator_sensibilidade = int(input('Digite o fator de sensibilidade: '))

if (fator_sensibilidade < 20) or (fator_sensibilidade > 60):
  print('Fator de sensibilidade invalido')
else:
  quantidade_insulina = (glicemia_do_momento - meta_pre_refeicao) / fator_sensibilidade
  print("A sua quantdade de insulina é: " + str(quantidade_insulina))
