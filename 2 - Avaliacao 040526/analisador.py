def ler_arquivo(caminho_arquivo):
    jogadores = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            for linha in file:
                linha = linha.strip()
                if not linha:
                    continue
                
                dados = linha.split(";")
                jogador = {
                    "nome": dados[0],
                    "classe": dados[1],
                    "kills": int(dados[2]),
                    "deaths": int(dados[3]),
                    "dano": int(dados[4])
                }
                jogadores.append(jogador)
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique se 'partida.txt' está na mesma pasta.")
    
    return jogadores

def calcular_kda(kills, deaths):
    if deaths == 0:
        return float(kills)
    return kills / deaths

def filtrar_por_classe(jogadores, classe):
    return [jogador for jogador in jogadores if jogador["classe"].lower() == classe.lower()]

def gerar_relatorio(jogadores):
    if not jogadores:
        return
    
    maior_dano = max(jogadores, key=lambda j: j["dano"])
    
    total_kills = sum(jogador["kills"] for jogador in jogadores)
    media_kills = total_kills / len(jogadores)
    
    destaques_kda = [
        jogador["nome"].upper() 
        for jogador in jogadores 
        if calcular_kda(jogador["kills"], jogador["deaths"]) > 2.0
    ]
    
    print("\n=== RELATÓRIO DE PERFORMANCE ===")
    print(f"Maior Dano: {maior_dano['nome']} com {maior_dano['dano']} de dano.")
    print(f"Média de Kills da Partida: {media_kills:.2f}")
    print("Jogadores com KDA > 2.0:")
    for nome in destaques_kda:
        print(f" - {nome}")

if __name__ == "__main__":
    nome_do_arquivo = "partida.txt"
    

    lista_jogadores = ler_arquivo(nome_do_arquivo)

    classe_buscada_mago = "Mago"
    magos_encontrados = filtrar_por_classe(lista_jogadores, classe_buscada_mago)
    
    classe_buscada_guerreiro = "Guerreiro"
    guerreiros_encontrados = filtrar_por_classe(lista_jogadores, classe_buscada_guerreiro)

    classe_buscada_arqueiro = "Arqueiro"
    arqueiros_encontrados = filtrar_por_classe(lista_jogadores, classe_buscada_arqueiro)

    classe_buscada_ladrao = "Ladrão"
    ladroes_encontrados = filtrar_por_classe(lista_jogadores, classe_buscada_ladrao)


    print(f"\n=== FILTRO DE CLASSE: {classe_buscada_mago.upper()} ===")
    if magos_encontrados:
        for mago in magos_encontrados:
            print(f"- {mago['nome']} (Kills: {mago['kills']} | Dano: {mago['dano']})")
    else:
        print("Nenhum jogador encontrado com essa classe.")
    
    print(f"\n=== FILTRO DE CLASSE: {classe_buscada_guerreiro.upper()} ===")
    if guerreiros_encontrados:
        for guerreiro in guerreiros_encontrados:
            print(f"- {guerreiro['nome']} (Kills: {guerreiro['kills']} | Dano: {guerreiro['dano']})")
    else:
        print("Nenhum jogador encontrado com essa classe.")

    print(f"\n=== FILTRO DE CLASSE: {classe_buscada_ladrao.upper()} ===")
    if ladroes_encontrados:
        for ladrao in ladroes_encontrados:
            print(f"- {ladrao['nome']} (Kills: {ladrao['kills']} | Dano: {ladrao['dano']})")
    else:
        print("Nenhum jogador encontrado com essa classe.")
    
    print(f"\n=== FILTRO DE CLASSE: {classe_buscada_arqueiro.upper()} ===")
    if arqueiros_encontrados:
        for arqueiro in arqueiros_encontrados:
            print(f"- {arqueiro['nome']} (Kills: {arqueiro['kills']} | Dano: {arqueiro['dano']})")
    else:
        print("Nenhum jogador encontrado com essa classe.")

    gerar_relatorio(lista_jogadores)