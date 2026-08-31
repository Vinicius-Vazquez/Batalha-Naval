import os

caminho_arquivo = os.path.join('data', 'estatisticas.txt')

def salvar_estatisticas(vencedor, total_jogadas, acertos_humano):
    os.makedirs('data', exist_ok=True)

    total_partidas = 0
    vitorias_humano = 0
    total_jogadas_acumuladas = 0
    total_acertos_acumulados = 0

    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                linhas = [linha.strip() for linha in arquivo.readlines() if linha.strip()]
                if len(linhas) >= 4:
                    total_partidas = int(linhas[0])
                    vitorias_humano = int(linhas[1])
                    total_jogadas_acumuladas = int(linhas[2])
                    total_acertos_acumulados = int(linhas[3])
        except (ValueError, IndexError):
            # Se o arquivo estiver corrompido, reinicia as métricas do zero
            total_partidas = 0
            vitorias_humano = 0
            total_jogadas_acumuladas = 0
            total_acertos_acumulados = 0

    total_partidas += 1
    if "Jogador" in vencedor:
        vitorias_humano += 1
    total_jogadas_acumuladas += total_jogadas
    total_acertos_acumulados += acertos_humano

    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"{total_partidas}\n")
        arquivo.write(f"{vitorias_humano}\n")
        arquivo.write(f"{total_jogadas_acumuladas}\n")
        arquivo.write(f"{total_acertos_acumulados}\n")


def exibir_estatisticas():
    if not os.path.exists(caminho_arquivo):
        print("\n[!] Nenhuma estatística encontrada. Jogue uma partida primeiro!\n")
        return

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = [linha.strip() for linha in arquivo.readlines() if linha.strip()]

        if len(linhas) < 4:
            print("\n[!] Arquivo de estatísticas corrompido ou incompleto.\n")
            return

        total_partidas = int(linhas[0])
        vitorias_humano = int(linhas[1])
        total_jogadas_acumuladas = int(linhas[2])
        total_acertos_acumulados = int(linhas[3])

        if total_jogadas_acumuladas > 0:
            aproveitamento = (total_acertos_acumulados / total_jogadas_acumuladas) * 100
        else:
            aproveitamento = 0.0

        print("\n================ ESTATÍSTICAS ================")
        print(f" Total de partidas:           {total_partidas}")
        print(f" Vitórias acumuladas:        {vitorias_humano}")
        print(f" Total de jogadas realizadas:{total_jogadas_acumuladas}")
        print(f" Total de disparos certeiros:{total_acertos_acumulados}")
        print(f" Taxa de aproveitamento:     {aproveitamento:.1f}%")
        print("=============================================\n")

    except (ValueError, IndexError):
        print("\n[!] Erro ao ler os dados do arquivo de estatísticas.\n")