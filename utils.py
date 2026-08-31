import time

def exibir_fim_de_jogo(vencedor, total_jogadas, tempo_segundos):
    """
    Exibe a tela de encerramento da partida com estatísticas e opções pós-jogo.
    Atende ao Requisito Funcional RF07.
    """
    # Converte o tempo em segundos para o formato HH:MM:SS
    horas = tempo_segundos // 3600
    minutos = (tempo_segundos % 3600) // 60
    segundos = tempo_segundos % 60
    tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    print("""\n==================================================
                      FIM DE JOGO                     
    ==================================================
    Vencedor: {vencedor}
    Total de jogadas: {total_jogadas}""")
    print(f"Tempo de partida: {tempo_formatado}")
    print("--------------------------------------------------")

    while True:
        print("[1] Ver replay  [2] Nova partida  [3] Menu principal")
        opcao = input("Escolha uma opcao: ").strip()

        if opcao in ["1", "2", "3"]:
            return opcao

        print("\n[!] Opcao invalida! Escolha 1, 2 ou 3.\n")