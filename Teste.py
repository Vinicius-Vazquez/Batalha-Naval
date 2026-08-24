"""
Módulo de testes temporário (sem a IA do Computador).
Valida a criação do tabuleiro, posicionamento da frota e jogada do jogador humano.
"""

from Tabuleiro import criar_tabuleiro, exibir_tabuleiro
from Navios import criar_frota, posicionar_frota_automaticamente
from Jogador import realizar_jogada_humano


def rodar_teste():
    print("=== TESTE DE INTEGRACAO: BATALHA NAVAL (MODO HUMANO) ===\n")

    # 1. Cria o tabuleiro e a frota do adversário
    tabuleiro_inimigo = criar_tabuleiro()
    frota_inimiga = criar_frota()

    # 2. Posiciona a frota de forma automática
    posicionar_frota_automaticamente(tabuleiro_inimigo, frota_inimiga)

    print("--- Tabuleiro Inimigo (Gabarito para Testes) ---")
    exibir_tabuleiro(tabuleiro_inimigo)

    # 3. Executa uma jogada do jogador humano
    print("\n--- TESTE DE DISPARO DO HUMANO ---")
    resultado = realizar_jogada_humano(tabuleiro_inimigo, frota_inimiga)

    print(f"\nResultado da jogada: {resultado}")
    print("\n--- Tabuleiro Inimigo Após a Jogada ---")
    exibir_tabuleiro(tabuleiro_inimigo)


if __name__ == "__main__":
    rodar_teste()