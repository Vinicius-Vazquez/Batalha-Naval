"""
Módulo responsável pela criação, posicionamento e gerenciamento dos navios no tabuleiro.
Atende aos Requisitos Funcionais RF03, RF04 e RF10.
"""

import random


def criar_frota():
    return [
        {"tipo": "Grande", "tamanho": 4, "posicoes": [], "afundado": False},
        {"tipo": "Pequeno", "tamanho": 2, "posicoes": [], "afundado": False},
        {"tipo": "Pequeno", "tamanho": 2, "posicoes": [], "afundado": False}
    ]


def validar_posicionamento(tabuleiro, linha, coluna, tamanho, orientacao):
    for i in range(tamanho):
        r = linha + i if orientacao == 'V' else linha
        c = coluna + i if orientacao == 'H' else coluna

        if r > 10 or c > 10:
            return False

        if tabuleiro[r][c] != '~':
            return False

    return True


def posicionar_navio(tabuleiro, navio, linha, coluna, orientacao):
    navio["posicoes"] = []
    for i in range(navio["tamanho"]):
        r = linha + i if orientacao == 'V' else linha
        c = coluna + i if orientacao == 'H' else coluna

        tabuleiro[r][c] = 'N'
        navio["posicoes"].append((r, c))


def posicionar_frota_automaticamente(tabuleiro, frota):
    for navio in frota:
        posicionado = False
        while not posicionado:
            orientacao = random.choice(['H', 'V'])

            if orientacao == 'H':
                linha = random.randint(1, 10)
                coluna = random.randint(1, 10 - navio["tamanho"] + 1)
            else:
                linha = random.randint(1, 10 - navio["tamanho"] + 1)
                coluna = random.randint(1, 10)

            if validar_posicionamento(tabuleiro, linha, coluna, navio["tamanho"], orientacao):
                posicionar_navio(tabuleiro, navio, linha, coluna, orientacao)
                posicionado = True


def checar_se_afundou(tabuleiro, navio):
    for (r, c) in navio["posicoes"]:
        if tabuleiro[r][c] != 'X':
            return False
    navio["afundado"] = True
    return True


def checar_vitoria(frota):
    for navio in frota:
        if not navio["afundado"]:
            return False
    return True


def conferir_frota(frota):
    print("\n--- RESUMO DA FROTA ---")
    for idx, navio in enumerate(frota, 1):
        posicoes_formatadas = [f"{chr(64 + c)}{r}" for r, c in navio["posicoes"]]
        print(f"Navio {idx} [{navio['tipo']} - {navio['tamanho']} casas]: {', '.join(posicoes_formatadas)}")
    print("-----------------------\n")