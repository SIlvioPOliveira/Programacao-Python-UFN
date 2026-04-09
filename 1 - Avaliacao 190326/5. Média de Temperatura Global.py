# 5. Média de Temperatura Global
# Para um painel informativo sobre mudanças climáticas, você precisa calcular a 
# média de temperatura de um período. O usuário deve informar quantos dias deseja 
# analisar. Use o while para ler a temperatura de cada um desses dias. Ao final, o 
# programa deve exibir a média aritmética das temperaturas e informar se a média 
# está "Acima do esperado" (caso seja maior que 25°C) ou "Dentro da normalidade".

# Entrada inicial: quantos dias serão analisados

total_dias = int(input("Quantos dias deseja analisar? "))

soma_temperaturas = 0
contador = 1

while contador <= total_dias:
  
    temp = float(input(f"Digite a temperatura do dia {contador}: "))
    
    soma_temperaturas += temp 
    contador += 1              


if total_dias > 0:
    media = soma_temperaturas / total_dias
    
    print("-" * 30)
    print(f"Média do período: {media:.2f}°C")

    if media > 25:
        print("Status: Acima do esperado")
    else:
        print("Status: Dentro da normalidade")
else:
    print("Nenhum dia foi analisado.")
