"""
Módulo responsável pelo comportamento e jogadas do computador (IA).
Implementa o algoritmo Hunt-and-Target para garantir a pontuação bônus.
"""

import random
from navios import checar_se_afundou


class ComputadorIA:
    def __init__(self):
        self.jogadas_realizadas = set()
        self.alvos_pendentes = []  # Fila de coordenadas vizinhas a testar

    def _obter_vizinhos_validos(self, linha, coluna):
        """Retorna coordenadas adjacentes válidas (dentro do tabuleiro 10x10) e não jogadas."""
        vizinhos = [
            (linha - 1, coluna),  # Cima
            (linha + 1, coluna),  # Baixo
            (linha, coluna - 1),  # Esquerda
            (linha, coluna + 1)   # Direita
        ]
        
        validos = []
        for r, c in vizinhos:
            if 1 <= r <= 10 and 1 <= c <= 10 and (r, c) not in self.jogadas_realizadas:
                validos.append((r, c))
        return validos

    def sortear_jogada(self):
        """
        Seleciona a próxima jogada:
        1. Se houver alvos pendentes (modo Target), pega da fila.
        2. Caso contrário (modo Hunt), sorteia uma coordenada aleatória.
        """
        # Prioriza a fila de alvos estratégicos
        while self.alvos_pendentes:
            alvo = self.alvos_pendentes.pop(0)
            if alvo not in self.jogadas_realizadas:
                self.jogadas_realizadas.add(alvo)
                return alvo

        # Modo Caça (aleatório) se não houver alvos prioritários
        while True:
            linha = random.randint(1, 10)
            coluna = random.randint(1, 10)

            if (linha, coluna) not in self.jogadas_realizadas:
                self.jogadas_realizadas.add((linha, coluna))
                return linha, coluna

    def realizar_jogada(self, tabuleiro_alvo, tabuleiro_visivel, frota_alvo):
        """
        Executa o disparo automático do computador contra o tabuleiro alvo.
        """
        linha, coluna = self.sortear_jogada()
        coluna_letra = chr(64 + coluna)
        coordenada_str = f"{coluna_letra}{linha}"
        print(f"\nComputador atirou em {coluna_letra}{linha}...")

        # Caso acerte um navio
        if tabuleiro_alvo[linha][coluna] == 'N':
            tabuleiro_alvo[linha][coluna] = 'X'
            tabuleiro_visivel[linha][coluna] = 'X'

            # Adiciona os vizinhos da casa atingida para investigar no próximo turno
            novos_alvos = self._obter_vizinhos_validos(linha, coluna)
            for alvo in novos_alvos:
                if alvo not in self.alvos_pendentes:
                    self.alvos_pendentes.append(alvo)

            for navio in frota_alvo:
                if (linha, coluna) in navio["posicoes"]:
                    if checar_se_afundou(tabuleiro_alvo, navio):
                        print(f"O computador afundou o seu navio {navio['tipo']}!")
                        return coordenada_str, 'Acerto'

            print("O computador acertou um dos seus navios!")
            return coordenada_str, 'Acerto'

        # Caso acerte a água
        else:
            tabuleiro_alvo[linha][coluna] = 'A'
            tabuleiro_visivel[linha][coluna] = 'A'
            print("O computador acertou a água.")
            return coordenada_str, 'Agua'