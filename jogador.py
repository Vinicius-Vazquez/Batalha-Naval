"""
Módulo responsável pelas jogadas do jogador humano.
"""

from navios import checar_se_afundou
from tabuleiro import pedir_coordenada


def realizar_jogada_humano(tabuleiro_real, tabuleiro_exibicao, frota_alvo):
    """
    Realiza o disparo do jogador humano.
    - tabuleiro_real: matriz com a posição oculta dos navios ('N').
    - tabuleiro_exibicao: matriz visível
    para o jogador com histórico de tiros ('X' e 'O').
    """
    while True:
        linha, coluna = pedir_coordenada()
        coordenada_str = f"{chr(64 + coluna)}{linha}"
        # Verifica se o jogador já atirou nessa coordenada anteriormente
        if tabuleiro_exibicao[linha][coluna] in ['X', 'O']:
            print("Você já atirou nessa posição! Escolha outra.")
            continue

        # Acertou um navio no tabuleiro real
        if tabuleiro_real[linha][coluna] == 'N':
            tabuleiro_real[linha][coluna] = 'X'
            tabuleiro_exibicao[linha][coluna] = 'X'

            for navio in frota_alvo:
                if (linha, coluna) in navio["posicoes"] and checar_se_afundou(
                    tabuleiro_real, navio
                ):
                    print(
                        "Navio afundado! Você destruiu um navio "
                        f"{navio['tipo'].lower()} do adversário."
                    )
                    return coordenada_str, 'Acerto'

            print("Acerto! Você atingiu um navio inimigo.")
            return coordenada_str, 'Acerto'

        # Acertou a água
        elif tabuleiro_real[linha][coluna] == '~':
            tabuleiro_real[linha][coluna] = 'O'
            tabuleiro_exibicao[linha][coluna] = 'O'
            print("Agua! Nenhum navio atingido nessa posicao.")
            return coordenada_str, 'Agua'
