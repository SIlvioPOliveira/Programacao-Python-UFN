#6 - Construa um programa em Python em que o usuário insira a sigla de um estado brasileiro em que
#    uma pessoa nasceu e, em seguida imprima uma das seguintes mensagens:
#    Carioca Paulista Mineiro Outros estados
estado_adpatrio = {
    'AC': 'Dinossauro',
    'AL': 'Alagoano',
    'AP': 'Amapiano',
    'AM': 'Amazonense',
    'BA': 'Prefuisoso',
    'CE': 'Cabe',
    'ES': 'Capixaba',
    'GO': 'Goiano',
    'MA': 'Maranhense',
    'MT': 'Mato-grossense',
    'MS': 'Sul-mato-grossense',
    'MG': 'Mineiro',
    'PA': 'Paranaense',
    'PB': 'Paraibano',
    'PE': 'Pernambucano',
    'PI': 'Boca Seca',
    'PR': 'Paranaense',
    'RJ': 'Bandido',
    'RN': 'Rio-grandense',
    'RS': 'Racista',
    'RO': 'Rondoniano',
    'RR': 'Roraimaense',
    'SC': 'Racista+',
    'SP': 'Pulmao Podre',
    'SE': 'Sergipano',
    'TO': 'Tucantinense'
}

sigla = input('Digite a sigla do seu estado: ')
if sigla in estado_adpatrio:
    print(estado_adpatrio[sigla])
else:
  print("Estado invalido!")






