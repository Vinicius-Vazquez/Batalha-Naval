from navios import criar_frota, posicionar_frota_automaticamente, checar_vitoria
from estatisticas import salvar_estatisticas, exibir_estatisticas
from menu import exibir_menu_principal, selecao_de_modo_de_jogo
from tabuleiro import criar_tabuleiro, exibir_tabuleiro
from replay import salvar_replay, reproduzir_replay
from jogador import realizar_jogada_humano

from utils import exibir_fim_de_jogo
from computador import ComputadorIA
import time

while True:
    opcao = exibir_menu_principal()
    if opcao == '1':
        modo = selecao_de_modo_de_jogo()
        if modo == '1':
            print("Iniciando partida: Jogador vs Computador")
            computador = ComputadorIA()
            tabuleiro_humano_real = criar_tabuleiro()
            tabuleiro_humano_visivel = criar_tabuleiro()
            tabuleiro_computador_real = criar_tabuleiro()
            tabuleiro_computador_visivel = criar_tabuleiro()
            frota_humano = criar_frota()
            frota_computador = criar_frota()
            posicionar_frota_automaticamente(tabuleiro_humano_real, frota_humano)
            posicionar_frota_automaticamente(tabuleiro_computador_real, frota_computador)

            inicio = time.time()
            total_jogadas = 0
            acertos_humano = 0
            historico_jogadas = []

            print("\nSeu tabuleiro com a frota posicionada:")
            exibir_tabuleiro(tabuleiro_humano_real)
            while True:
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

                exibir_tabuleiro(tabuleiro_humano_visivel)
                coordenada, resultado = computador.realizar_jogada(tabuleiro_humano_real, tabuleiro_humano_visivel, frota_humano)
                jogada_str = f"Computador - {coordenada} - {resultado}"
                historico_jogadas.append(jogada_str)
                total_jogadas += 1
                if checar_vitoria(frota_humano):
                    duracao = int(time.time() - inicio)
                    vencedor = "Computador"
                    break

            acertos_vencedor = acertos_humano
            salvar_estatisticas(vencedor, total_jogadas, acertos_vencedor)
            salvar_replay(historico_jogadas)
            opcao_fim_de_jogo = exibir_fim_de_jogo(vencedor, total_jogadas, duracao)

            if opcao_fim_de_jogo == '1':
                reproduzir_replay()
            elif opcao_fim_de_jogo == '2':
                print("\nReiniciando uma nova partida...")
                continue  # Reinicia a seleção de modo/partida
            elif opcao_fim_de_jogo == '3':
                break

        elif modo == '2':
            print("Iniciando partida: Jogador 1 vs Jogador 2")
            tabuleiro_jogador1_real = criar_tabuleiro()
            tabuleiro_jogador1_visivel = criar_tabuleiro()
            tabuleiro_jogador2_real = criar_tabuleiro()
            tabuleiro_jogador2_visivel = criar_tabuleiro()
            frota_jogador1 = criar_frota()
            frota_jogador2 = criar_frota()
            posicionar_frota_automaticamente(tabuleiro_jogador1_real, frota_jogador1)
            posicionar_frota_automaticamente(tabuleiro_jogador2_real, frota_jogador2)

            print("\n================ JOGADOR 1 ================")
            print("Sua frota foi posicionada:")
            exibir_tabuleiro(tabuleiro_jogador1_real)
            input("\n[Jogador 1] Pressione ENTER para ocultar a tela e passar para o Jogador 2...")
            print("\n" * 50)  # Limpa a tela no terminal
            
            print("\n================ JOGADOR 2 ================")
            print("Sua frota foi posicionada:")
            exibir_tabuleiro(tabuleiro_jogador2_real)
            input("\n[Jogador 2] Pressione ENTER para ocultar a tela e começar a partida...")
            print("\n" * 50)  # Limpa a tela no terminal
            
            inicio = time.time()
            total_jogadas = 0
            acertos_jogador1 = 0
            acertos_jogador2 = 0
            historico_jogadas = []
            
            while True:
                exibir_tabuleiro(tabuleiro_jogador2_visivel)
                coordenada, resultado = realizar_jogada_humano(tabuleiro_jogador2_real, tabuleiro_jogador2_visivel, frota_jogador2)
                jogada_str = f"Jogador 1 - {coordenada} - {resultado}"
                historico_jogadas.append(jogada_str)
                if resultado == 'Acerto':
                    acertos_jogador1 += 1
                total_jogadas += 1
                if checar_vitoria(frota_jogador2):
                    duracao = int(time.time() - inicio)
                    vencedor = "Jogador 1"
                    break
            
                exibir_tabuleiro(tabuleiro_jogador1_visivel)
                coordenada, resultado = realizar_jogada_humano(tabuleiro_jogador1_real, tabuleiro_jogador1_visivel, frota_jogador1)
                jogada_str = f"Jogador 2 - {coordenada} - {resultado}"
                historico_jogadas.append(jogada_str)
                if resultado == 'Acerto':
                    acertos_jogador2 += 1
                total_jogadas += 1
                if checar_vitoria(frota_jogador1):
                    duracao = int(time.time() - inicio)
                    vencedor = "Jogador 2"
                    break
            
            salvar_estatisticas(vencedor, total_jogadas, acertos_vencedor)
            salvar_replay(historico_jogadas)
            opcao_fim_de_jogo = exibir_fim_de_jogo(vencedor, total_jogadas, duracao)

            if opcao_fim_de_jogo == '1':
                reproduzir_replay()
            elif opcao_fim_de_jogo == '2':
                print("\nReiniciando uma nova partida...")
                continue  # Reinicia a seleção de modo/partida
            elif opcao_fim_de_jogo == '3':
                break

        elif modo == '0':
            continue  

    elif opcao == '2':
        exibir_estatisticas()

    elif opcao == '3':
        reproduzir_replay()

    elif opcao == '4':
        print("""\n================ INSTRUÇÕES DE JOGO ================
        1. OBJETIVO: Afundar todos os navios da frota adversária antes que ela afunde a sua.
        2. COMO JOGAR: Informe a coordenada de disparo quando solicitado (ex: A5, C3, J10).
        3. SÍMBOLOS DO TABULEIRO:
           - '~' ou '.' : Água não atingida / Desconhecido
           - 'A'        : Tiro na água (Erro)
           - 'X'        : Tiro certeiro (Acerto em navio)
        ====================================================\n
        
        \n================ CRÉDITOS ================
        Nome do estúdio: GPTech Games
        Desenvolvedor: Vinicius Souza Vazquez
        Professor / Product Owner: Prof. Guido Pantuza
        Disciplina: Programação em Python - CEFET-MG
        ====================================================\n""")

    elif opcao == '5':
        break