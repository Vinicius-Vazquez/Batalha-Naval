import time
from navios import criar_frota, posicionar_frota_automaticamente, checar_vitoria, conferir_frota
from estatisticas import salvar_estatisticas, exibir_estatisticas
from menu import exibir_menu_principal, selecao_de_modo_de_jogo
from tabuleiro import criar_tabuleiro, exibir_tabuleiro
from replay import salvar_replay, reproduzir_replay
from jogador import realizar_jogada_humano
from utils import exibir_fim_de_jogo
from computador import ComputadorIA


def jogar_partida_vs_computador():
    computador = ComputadorIA()
    computador.reset()

    tabuleiro_computador_real = criar_tabuleiro()
    tabuleiro_computador_visivel = criar_tabuleiro()
    frota_computador = criar_frota()
    posicionar_frota_automaticamente(tabuleiro_computador_real, frota_computador)

    while True:
        tabuleiro_humano_real = criar_tabuleiro()
        tabuleiro_humano_visivel = criar_tabuleiro()
        frota_humano = criar_frota()
        posicionar_frota_automaticamente(tabuleiro_humano_real, frota_humano)

        print("\nSeu tabuleiro com a frota posicionada:")
        exibir_tabuleiro(tabuleiro_humano_real)
        conferir_frota(frota_humano)

        confirmar = input("Deseja confirmar esse posicionamento? [S]im / [R]eposicionar: ").strip().upper()
        if confirmar == 'S':
            break
        elif confirmar == 'R':
            print("\nReposicionando sua frota...")
        else:
            print("\n[!] Opção inválida! Digite 'S' para confirmar ou 'R' para reposicionar.")

    inicio = time.time()
    total_jogadas = 0
    acertos_humano = 0
    historico_jogadas = []

    while True:
        print("\n--- SEU TABULEIRO ADVERSÁRIO ---")
        exibir_tabuleiro(tabuleiro_computador_visivel)
        coordenada, resultado = realizar_jogada_humano(tabuleiro_computador_real, tabuleiro_computador_visivel, frota_computador)
        jogada_str = f"Jogador - {coordenada} - {resultado}"
        historico_jogadas.append(jogada_str)
        
        if resultado == 'Acerto':
            acertos_humano += 1
        total_jogadas += 1

        if checar_vitoria(frota_computador):
            duracao = int(time.time() - inicio)
            vencedor = "Jogador"
            break

        coordenada, resultado = computador.realizar_jogada(tabuleiro_humano_real, tabuleiro_humano_visivel, frota_humano)
        jogada_str = f"Computador - {coordenada} - {resultado}"
        historico_jogadas.append(jogada_str)
        total_jogadas += 1

        if checar_vitoria(frota_humano):
            duracao = int(time.time() - inicio)
            vencedor = "Computador"
            break

    salvar_estatisticas(vencedor, total_jogadas, acertos_humano)
    salvar_replay(historico_jogadas)

    while True:
        opcao_fim = exibir_fim_de_jogo(vencedor, total_jogadas, duracao)
        if opcao_fim == '1':
            reproduzir_replay()
        elif opcao_fim in ['2', '3']:
            return opcao_fim


def jogar_partida_dois_jogadores():
    tabuleiro_j1_real = criar_tabuleiro()
    tabuleiro_j1_visivel = criar_tabuleiro()
    tabuleiro_j2_real = criar_tabuleiro()
    tabuleiro_j2_visivel = criar_tabuleiro()
    
    frota_j1 = criar_frota()
    frota_j2 = criar_frota()
    
    posicionar_frota_automaticamente(tabuleiro_j1_real, frota_j1)
    posicionar_frota_automaticamente(tabuleiro_j2_real, frota_j2)

    print("\n================ JOGADOR 1 ================")
    print("Sua frota foi posicionada:")
    exibir_tabuleiro(tabuleiro_j1_real)
    input("\n[Jogador 1] Pressione ENTER para ocultar a tela e passar para o Jogador 2...")
    print("\n" * 50)

    print("\n================ JOGADOR 2 ================")
    print("Sua frota foi posicionada:")
    exibir_tabuleiro(tabuleiro_j2_real)
    input("\n[Jogador 2] Pressione ENTER para começar a partida...")
    print("\n" * 50)

    inicio = time.time()
    total_jogadas = 0
    acertos_j1 = 0
    acertos_j2 = 0
    historico_jogadas = []

    while True:
        print("\n--- TURNO: JOGADOR 1 ---")
        exibir_tabuleiro(tabuleiro_j2_visivel)
        coordenada, resultado = realizar_jogada_humano(tabuleiro_j2_real, tabuleiro_j2_visivel, frota_j2)
        historico_jogadas.append(f"Jogador 1 - {coordenada} - {resultado}")
        if resultado == 'Acerto':
            acertos_j1 += 1
        total_jogadas += 1

        if checar_vitoria(frota_j2):
            duracao = int(time.time() - inicio)
            vencedor = "Jogador 1"
            break

        print("\n--- TURNO: JOGADOR 2 ---")
        exibir_tabuleiro(tabuleiro_j1_visivel)
        coordenada, resultado = realizar_jogada_humano(tabuleiro_j1_real, tabuleiro_j1_visivel, frota_j1)
        historico_jogadas.append(f"Jogador 2 - {coordenada} - {resultado}")
        if resultado == 'Acerto':
            acertos_j2 += 1
        total_jogadas += 1

        if checar_vitoria(frota_j1):
            duracao = int(time.time() - inicio)
            vencedor = "Jogador 2"
            break

    salvar_estatisticas(vencedor, total_jogadas, acertos_j1)
    salvar_replay(historico_jogadas)

    while True:
        opcao_fim = exibir_fim_de_jogo(vencedor, total_jogadas, duracao)
        if opcao_fim == '1':
            reproduzir_replay()
        elif opcao_fim in ['2', '3']:
            return opcao_fim


def main():
    # CONEXÃO DA INTERFACE GRÁFICA NO INÍCIO DO PROGRAMA
    print("==================================================")
    print("           BATALHA NAVAL - GPTECH GAMES           ")
    print("==================================================")
    modo_interface = input("Deseja iniciar o jogo em modo [G]ráfico ou [T]exto? ").strip().upper()

    if modo_interface == 'G':
        from gui import iniciar_interface_grafica
        iniciar_interface_grafica()
        return

    # MODO TEXTO CONVENCIONAL
    while True:
        opcao = exibir_menu_principal()
        
        if opcao == '1':
            while True:
                modo = selecao_de_modo_de_jogo()
                if modo == '0':
                    break

                if modo == '1':
                    acao = jogar_partida_vs_computador()
                elif modo == '2':
                    acao = jogar_partida_dois_jogadores()

                if acao == '3':
                    break

        elif opcao == '2':
            exibir_estatisticas()

        elif opcao == '3':
            reproduzir_replay()

        elif opcao == '4':
            print("""\n================ INSTRUÇÕES DE JOGO ================
1. OBJETIVO: Afundar todos os navios da frota adversária.
2. COMO JOGAR: Informe a coordenada de disparo quando solicitado (ex: C5, J10).
3. SÍMBOLOS DO TABULEIRO:
   - '~' : Água não jogada
   - 'O' : Tiro na água (Erro)
   - 'X' : Tiro certeiro (Acerto)
   - 'N' : Navio (Visível apenas no seu próprio tabuleiro)
====================================================

================ CRÉDITOS ================
Nome do estúdio: GPTech Games
Desenvolvedor: Vinicius Souza Vazquez
Professor / Product Owner: Prof. Guido Pantuza
Disciplina: Programação em Python - CEFET-MG
====================================================\n""")

        elif opcao == '5':
            print("Saindo do jogo... Até logo!")
            break


if __name__ == "__main__":
    main()