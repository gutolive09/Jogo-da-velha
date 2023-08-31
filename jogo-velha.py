def inicializarTabuleiro():
    tabuleiro = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]
    return tabuleiro

def imprimirTabuleiro(tabuleiro):
    for i in tabuleiro:
        for j in i:
            print(j, end=" ")
        print()

def imprimeMenuPrincipal():
    print("Bem vindo ao Jogo da Velha!")
    opcao = input("Qual modo deseja jogar: \n 1 - Jogador x Jogador \n 2 - Jogador x Maquina (Fácil) \n 3 - Jogador x Maquina (Difícil)")
    if opcao == "1":
        modoJogador()
    elif opcao == "2":
        modoFacil()
    elif opcao == "3":
        modoDificil()
    else: 
        print("Selecione um das opções acima !")

def jogar(i, j, jogada, tabuleiro):


def modoJogador():
    tabuleiro = inicializarTabuleiro()
    score1, score2 = 0
    while score1 < 3 




