import random
from Navios import checar_se_afundou

class computadorIA:
    def __init__(self):
        self.jogadas_realizadas = set()

    def sortear_jogada(self):
        while True:
            linha = random.randint(1, 10)
            coluna = random.randint(1, 10)

            if not (linha, coluna) in self.jogadas_realizadas:
                self.jogadas_realizadas.add((linha, coluna))
                return linha, coluna

    def realizar_jogada(self, tabuleiro_alvo, frota_alvo):
        linha, coluna = self.sortear_jogada()
        coluna_letra = chr(64 + coluna)
        print(f"\nComputador atirou em {coluna_letra}{linha}...")