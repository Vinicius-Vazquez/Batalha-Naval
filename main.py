from menu import exibir_menu_principal, selecao_de_modo_de_jogo
from tabuleiro import criar_tabuleiro, exibir_tabuleiro
from jogador import realizar_jogada_humano
from navios import criar_frota, posicionar_frota_automaticamente, checar_vitoria
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

            while True:
                exibir_tabuleiro(tabuleiro_computador_visivel)
                realizar_jogada_humano(tabuleiro_computador_real, tabuleiro_computador_visivel, frota_computador)
                total_jogadas += 1
                if checar_vitoria(frota_computador):
                    duracao = int(time.time() - inicio)
                    opcao_fim_de_jogo = exibir_fim_de_jogo("Jogador", total_jogadas, duracao)
                    break

                exibir_tabuleiro(tabuleiro_humano_visivel)
                computador.realizar_jogada(tabuleiro_humano_real, tabuleiro_humano_visivel, frota_humano)
                total_jogadas += 1
                if checar_vitoria(frota_humano):
                    duracao = int(time.time() - inicio)
                    opcao_fim_de_jogo = exibir_fim_de_jogo("Computador", total_jogadas, duracao)
                    break

            if opcao_fim_de_jogo == '1':
                print("\n[Módulo de Replay em desenvolvimento...]")
            elif opcao_fim_de_jogo == '2':
                print("\nReiniciando uma nova partida...")
            elif opcao_fim_de_jogo == '3':
                continue

        elif modo == '2':

        elif modo == '0':
            continue  

    elif opcao == '2':

    elif opcao == '3':

    elif opcao == '4':

    elif opcao == '5':
        break