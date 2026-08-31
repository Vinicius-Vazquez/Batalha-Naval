import os

CAMINHO_REPLAY = os.path.join('data', 'ultimo_replay.txt')


def salvar_replay(historico_jogadas):
    os.makedirs('data', exist_ok=True)
    try:
        with open(CAMINHO_REPLAY, 'w', encoding='utf-8') as arquivo:
            for jogada in historico_jogadas:
                arquivo.write(f"{jogada}\n")
    except OSError as e:
        print(f"\n[!] Erro ao salvar arquivo de replay: {e}")


def reproduzir_replay():
    if not os.path.exists(CAMINHO_REPLAY):
        print("\n[!] Nenhum replay encontrado. Jogue uma partida primeiro!\n")
        return

    try:
        with open(CAMINHO_REPLAY, 'r', encoding='utf-8') as arquivo:
            linhas = [linha.strip() for linha in arquivo.readlines() if linha.strip()]
    except OSError:
        print("\n[!] Erro ao ler o arquivo de replay.\n")
        return

    if not linhas:
        print("\n[!] O arquivo de replay está vazio.\n")
        return

    total_jogadas = len(linhas)
    print("\n================ REPRODUZINDO REPLAY ================")

    for i, jogada_str in enumerate(linhas, start=1):
        print(f"Jogada {i:02d}/{total_jogadas:02d} -> {jogada_str}")

        if i == total_jogadas:
            print("\nFim da reprodução do replay!")
            print("===================================================\n")
            break

        opcao = input("[ENTER] Próxima jogada | [Q] Sair do replay: ").strip().upper()
        if opcao == 'Q':
            print("\nReprodução cancelada pelo usuário.")
            print("===================================================\n")
            break