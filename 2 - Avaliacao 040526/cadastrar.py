def pedir_numero(mensagem):
    # Fica em loop até o usuário digitar um número inteiro válido
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros (sem vírgula ou letras).")

def pedir_classe():
    classes = {1: "Guerreiro", 2: "Arqueiro", 3: "Mago", 4: "Ladrão"}
    while True:
        print("\nClasses disponíveis: [1] Guerreiro  [2] Arqueiro  [3] Mago  [4] Ladrão")
        try:
            opcao = int(input("Digite o número da classe: "))
            if opcao in classes:
                return classes[opcao] # Retorna o nome da classe escolhida
            else:
                print("Opção inválida! Escolha um número de 1 a 4.")
        except ValueError:
            print("Erro: Digite apenas o número correspondente à classe.")

def cadastrar_jogadores():
    jogadores = [] 
    
    while True:
        print("\n--- Cadastro de Jogador ---")
        nome = input("Nome do jogador (ou digite 'sair' para finalizar): ")
        
        if nome.lower() == 'sair':
            break
            
        # Usando as funções seguras que criamos
        classe = pedir_classe()
        kills = pedir_numero("Kills: ")
        deaths = pedir_numero("Deaths: ")
        dano = pedir_numero("Dano Causado: ")
        
        jogador = {
            "nome": nome,
            "classe": classe,
            "kills": kills,
            "deaths": deaths,
            "dano": dano
        }
        
        jogadores.append(jogador)
        print(f"\n{nome} ({classe}) adicionado com sucesso!")

    # Salvando no txt
    if jogadores:
        with open("partida.txt", "a", encoding="utf-8") as arquivo:
            for j in jogadores:
                arquivo.write(f"{j['nome']};{j['classe']};{j['kills']};{j['deaths']};{j['dano']}\n")
        print(f"\nSucesso! {len(jogadores)} jogador(es) salvo(s) em 'partida.txt'.")

if __name__ == "__main__":
    cadastrar_jogadores()