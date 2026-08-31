def exibir_menu_principal():
    while True:
        print("""==================================================
        t\tBATALHA NAVAL - GPTECH GAMES
        ==================================================
        1. Nova partida
        2. Ver estatisticas
        3. Assistir replay da ultima partida
        4. Instruções e créditos
        5. Sair
        --------------------------------------------------""")
        opcao_do_jogador = input("Escolha uma opcao: ").strip()

        if opcao_do_jogador in ['1', '2', '3', '4', '5']:
            return opcao_do_jogador
        print("\n[!] Opcao invalida! Digite um numero de 1 a 5.\n")


def selecao_de_modo_de_jogo():
    while True:
        print("""
        ================ MODO DE JOGO ================
        [1] Jogador vs Computador
        [2] Dois Jogadores
        [0] Voltar ao menu
        ==============================================""")
        
        modo_selecionado = input("Selecione o modo de jogo: ").strip()

        if modo_selecionado in ['1', '2', '0']:
            return modo_selecionado
        print("\n[!] Opcao invalida! Escolha 1, 2 ou 0.\n")