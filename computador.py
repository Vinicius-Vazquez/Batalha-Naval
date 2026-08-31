import random
from navios import checar_se_afundou


class ComputadorIA:
    def __init__(self):
        self.jogadas_realizadas = set()
        self.alvos_pendentes = []

    def reset(self):
        self.jogadas_realizadas.clear()
        self.alvos_pendentes.clear()

    def _obter_vizinhos_validos(self, linha, coluna):
        vizinhos = [
            (linha - 1, coluna),
            (linha + 1, coluna),
            (linha, coluna - 1),
            (linha, coluna + 1)
        ]
        
        validos = []
        for r, c in vizinhos:
            if 1 <= r <= 10 and 1 <= c <= 10 and (r, c) not in self.jogadas_realizadas:
                validos.append((r, c))
        return validos

    def sortear_jogada(self):
        while self.alvos_pendentes:
            alvo = self.alvos_pendentes.pop(0)
            if alvo not in self.jogadas_realizadas:
                self.jogadas_realizadas.add(alvo)
                return alvo

        while True:
            linha = random.randint(1, 10)
            coluna = random.randint(1, 10)

            if (linha, coluna) not in self.jogadas_realizadas:
                self.jogadas_realizadas.add((linha, coluna))
                return linha, coluna

    def realizar_jogada(self, tabuleiro_alvo, tabuleiro_visivel, frota_alvo):
        linha, coluna = self.sortear_jogada()
        coluna_letra = chr(64 + coluna)
        coordenada_str = f"{coluna_letra}{linha}"
        print(f"\nComputador atirou em {coluna_letra}{linha}...")

        if tabuleiro_alvo[linha][coluna] == 'N':
            tabuleiro_alvo[linha][coluna] = 'X'
            tabuleiro_visivel[linha][coluna] = 'X'

            novos_alvos = self._obter_vizinhos_validos(linha, coluna)
            for alvo in novos_alvos:
                if alvo not in self.alvos_pendentes:
                    self.alvos_pendentes.append(alvo)

            for navio in frota_alvo:
                if (linha, coluna) in navio["posicoes"]:
                    if checar_se_afundou(tabuleiro_alvo, navio):
                        print(f"O computador afundou o seu navio {navio['tipo'].lower()}!")
                        return coordenada_str, 'Acerto'

            print("O computador acertou um dos seus navios!")
            return coordenada_str, 'Acerto'

        else:
            tabuleiro_alvo[linha][coluna] = 'O'
            tabuleiro_visivel[linha][coluna] = 'O'
            print("O computador acertou a água.")
            return coordenada_str, 'Agua'