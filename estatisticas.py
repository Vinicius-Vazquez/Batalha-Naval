import os

def salvar_estatisticas(vencedor, total_jogadas, acertos_humano):
    os.makedirs('data', exist_ok=True)
    caminho_arquivo = os.path.join('data', 'estatisticas.txt')

    total_partidas = 0
    vitorias_humano = 0
    total_jogadas_acumuladas = 0
    total_acertos_acumulados = 0

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

        total_partidas = int(linhas[0])
        vitorias_humano = int(linhas[1])
        total_jogadas_acumuladas = int(linhas[2])
        total_acertos_acumulados = int(linhas[3])
    except FileNotFoundError:
        pass

    total_partidas += 1
    if vencedor == "Jogador":
        vitorias_humano += 1
    total_jogadas_acumuladas += total_jogadas
    total_acertos_acumulados += acertos_humano

    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"{total_partidas}\n")
        arquivo.write(f"{vitorias_humano}\n")
        arquivo.write(f"{total_jogadas_acumuladas}\n")
        arquivo.write(f"{total_acertos_acumulados}\n")


def exibir_estatisticas():
    caminho_arquivo = os.path.join('data', 'estatisticas.txt')

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

            total_partidas = int(linhas[0])
            vitorias_humano = int(linhas[1])
            total_jogadas_acumuladas = int(linhas[2])
            total_acertos_acumulados = int(linhas[3])
    except FileNotFoundError:
        print("\n[!] Nenhuma estatística encontrada. Jogue uma partida primeiro!\n")
        return

    if total_jogadas_acumuladas > 0:
        aproveitamento = (total_acertos_acumulados/total_jogadas_acumuladas)*100
    else:
        aproveitamento = 0.0

    print("\n================ ESTATÍSTICAS ================")
    print(total_partidas)
    print(vitorias_humano)
    print(total_jogadas_acumuladas)
    print(total_acertos_acumulados)
    print(f"Aproveitamento: {aproveitamento:.1f}%")
    print("=============================================")