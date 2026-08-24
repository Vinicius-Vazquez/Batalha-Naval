from Tabuleiro import pedir_coordenada
from Navios import checar_se_afundou

def realizar_jogada_humano(tabuleiro_alvo, frota_alvo):
    while True:
        linha, coluna = pedir_coordenada()

        if tabuleiro_alvo[linha][coluna] in ['X', 'O']:
            print("Você já atirou nessa posição! Escolha outra.")
            continue

        if tabuleiro_alvo[linha][coluna] == 'N':
            tabuleiro_alvo[linha][coluna] = 'X'
            for navio in frota_alvo:
                if (linha, coluna) in navio["posicoes"]:
                    # Se encontrou o navio, testa se TODAS as partes dele viraram 'X'
                    if checar_se_afundou(tabuleiro_alvo, navio):
                        print(f"Navio afundado! Você destruiu um navio {navio['tipo']} do adversário.")
                        return 'afundado'

            print("Acerto! Você atingiu um navio inimigo.")
            return 'acerto'
        
        elif tabuleiro_alvo[linha][coluna] == '~':
            tabuleiro_alvo[linha][coluna] = 'O'
            print("Erro! Você acertou a água!")
            return 'erro'