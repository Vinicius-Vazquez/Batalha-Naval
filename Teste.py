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

# 1. Cria a frota e os DOIS tabuleiros do adversário (Computador)
frota_computador = criar_frota()

tabuleiro_comp_real = criar_tabuleiro()     # Guarda os navios ocultos 'N'
tabuleiro_comp_visivel = criar_tabuleiro()  # Mostra apenas o que o Humano já descobriu ('~', 'X', 'O')

# 2. Posiciona os navios APENAS no tabuleiro real do Computador
posicionar_frota_automaticamente(tabuleiro_comp_real, frota_computador)

# 3. Na hora da jogada do humano:
# Exibe apenas o tabuleiro visível (onde o humano não vê as letras 'N')
exibir_tabuleiro(tabuleiro_comp_visivel)

# Passa o REAL para conferir se acertou 'N' e o VISÍVEL para marcar 'X' ou 'O'
realizar_jogada_humano(tabuleiro_comp_real, tabuleiro_comp_visivel, frota_computador)