def print_quadro(quadro):
    for linha in quadro:
        print(" | ".join(linha))
        print("-" * 9)

def check_vencedor(quadro):
    
    for linha in quadro:
        if linha.count(linha[0]) == len(linha) and linha[0] != " ":
            return True

    
    for col in range(len(quadro[0])):
        if quadro[0][col] == quadro[1][col] == quadro[2][col] and quadro[0][col] != " ":
            return True

    
    if quadro[0][0] == quadro[1][1] == quadro[2][2] and quadro[0][0] != " ":
        return True
    if quadro[0][2] == quadro[1][1] == quadro[2][0] and quadro[0][2] != " ":
        return True

    return False

def jogodavelha():
    quadro = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_quadro(quadro)
        linha = int(input(f"Jogador {player}, escolha uma linha (0, 1 ou 2): "))
        col = int(input(f"Jogador {player}, escolha uma coluna (0, 1 ou 2): "))

        if quadro[linha][col] == " ":
            quadro[linha][col] = player
            if check_vencedor(quadro):
                print_quadro(quadro)
                print(f"Parabéns, jogador {player} venceu!")
                break
            elif all(" " not in linha for linha in quadro):
                print_quadro(quadro)
                print("Empate!")
                break
            else:
                player = "O" if player == "X" else "X"
        else:
            print("Essa posição já foi escolhida, escolha outra.")

jogodavelha()
