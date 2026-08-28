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
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("\n[!] Nenhum replay encontrado. Jogue uma partida primeiro!\n")
        return

    if not linhas:
        print("\n[!] O arquivo de replay está vazio.\n")
        return

    total_jogadas = len(linhas)
    print("\nReproduzindo replay da ultima partida...\n")

    for i, linha in enumerate(linhas, start=1):
        jogada_str = linha.strip()
        print(f"Jogada {i:02d}/{total_jogadas:02d} - {jogada_str}")

        opcao = input("[ENTER] Proxima jogada [Q] Sair do replay: ").strip().upper()
        if opcao == 'Q':
            break