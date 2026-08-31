import os


def salvar_replay(historico_jogadas):
    # Garantir a pasta data:
    os.makedirs('data', exist_ok=True)
    caminho_arquivo = os.path.join('data', 'ultimo_replay.txt')

    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        for jogada in historico_jogadas:
            arquivo.write(f"{jogada}\n")


def reproduzir_replay():
    caminho_arquivo = os.path.join('data', 'ultimo_replay.txt')

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = [linha.strip() for linha in arquivo.readlines() if linha.strip()]
    except FileNotFoundError:
        print("\n[!] Nenhum replay encontrado. Jogue uma partida primeiro!\n")
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