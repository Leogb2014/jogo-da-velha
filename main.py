def interface():
    print("   0   1   2")
    print("0 [{}] [{}] [{}]".format(tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]))
    print("1 [{}] [{}] [{}]".format(tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2]))
    print("2 [{}] [{}] [{}]".format(tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]))

tabuleiro = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

parar = False
rodada = "X"
jogadas = 0

while parar == False:

    if jogadas == 9:
        interface()
        print("Empate")
        parar = True

    interface()

    linha = int(input("Digite a linha: "))
    coluna = int(input("Digite a coluna: "))

    if rodada == "X":
        tabuleiro[linha][coluna] = "X"
        jogadas += 1
        rodada = "O"
    elif rodada == "O":
        tabuleiro[linha][coluna] = "O"
        jogadas += 1
        rodada = "X"



print("Fim de Jogo!")
