"""
Módulo responsável pela criação, posicionamento e gerenciamento dos navios no tabuleiro.
Atende aos Requisitos Funcionais RF03 e RF04 (Pequeno: 2 posições, Grande: 4 posições).
"""

import random


def criar_frota():
    """
    Define a composição padrão da frota.
    Retorna uma lista de dicionários representando os navios.
    """
    return [
    {"tipo": "Grande", "tamanho": 4, "posicoes": [], "afundado": False},
    {"tipo": "Pequeno", "tamanho": 2, "posicoes": [], "afundado": False},
    {"tipo": "Pequeno", "tamanho": 2, "posicoes": [], "afundado": False} 
    ]


def validar_posicionamento(tabuleiro, linha, coluna, tamanho, orientacao):
    """
    Verifica se um navio pode ser posicionado nas coordenadas informadas sem
    sair do tabuleiro 10x10 e sem sobrepor navios já existentes.
    """
    for i in range(tamanho):
        r = linha + i if orientacao == 'V' else linha
        c = coluna + i if orientacao == 'H' else coluna

        # Checa limites do tabuleiro (linhas 1-10 e colunas 1-10)
        if r > 10 or c > 10:
            return False

        # Checa sobreposição (a casa deve conter apenas água '~')
        if tabuleiro[r][c] != '~':
            return False

    return True


def posicionar_navio(tabuleiro, navio, linha, coluna, orientacao):
    """
    Escreve as posições do navio no tabuleiro e salva as coordenadas no dicionário do navio.
    """
    navio["posicoes"] = []
    for i in range(navio["tamanho"]):
        r = linha + i if orientacao == 'V' else linha
        c = coluna + i if orientacao == 'H' else coluna

        tabuleiro[r][c] = 'N'  # Marca visual de navio na matriz
        navio["posicoes"].append((r, c))


def posicionar_frota_automaticamente(tabuleiro, frota):
    #RF04: Posiciona todos os navios da frota automaticamente de forma aleatória, garantindo que não haja sobreposição.

    for navio in frota:
        posicionado = False
        while not posicionado:
            orientacao = random.choice(['H', 'V'])
            
            # Sorteia coordenadas iniciais respeitando o tabuleiro 10x10
            if orientacao == 'H':
                linha = random.randint(1, 10)
                coluna = random.randint(1, 10 - navio["tamanho"] + 1)
            else:
                linha = random.randint(1, 10 - navio["tamanho"] + 1)
                coluna = random.randint(1, 10)

            if validar_posicionamento(tabuleiro, linha, coluna, navio["tamanho"], orientacao):
                posicionar_navio(tabuleiro, navio, linha, coluna, orientacao)
                posicionado = True


def verificar_afundamento(frota, linha, coluna):
    """
    RN03: Verifica se o disparo em (linha, coluna) fez algum navio afundar.
    Retorna o nome do tipo do navio afundado ("Grande" ou "Pequeno") ou None.
    """
    for navio in frota:
        if (linha, coluna) in navio["posicoes"]:
            # Verifica se todas as posições do navio já foram atingidas
            # (Essa validação será checada junto com o histórico de acertos do tabuleiro)
            return navio
    return None


def checar_se_afundou(tabuleiro, navio):
    """
    Confere se todas as coordenadas registradas para aquele navio contêm 'X' (acerto).
    """
    for (r, c) in navio["posicoes"]:
        if tabuleiro[r][c] != 'X':
            return False
    navio["afundado"] = True
    return True