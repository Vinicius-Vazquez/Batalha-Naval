"""
Módulo responsável pela criação, exibição e conversão de coordenadas do tabuleiro.
Aderente à Regra de Negócio RN01 e boas práticas PEP8.
"""

def criar_tabuleiro():
    tabuleiros = [[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']]
    for i in range(1, 11):
        linha = [str(i)] + ['~'] * 10
        tabuleiros.append(linha)
    return tabuleiros


def exibir_tabuleiro(tabuleiros):
    for linha in tabuleiros:
        print(' '.join(f"{item:>2}" for item in linha))


def converter_coordenada(entrada_str):
    entrada_str = entrada_str.strip().upper()
    
    if len(entrada_str) < 2 or len(entrada_str) > 3:
        return None, None
    
    coluna_char = entrada_str[0]
    linha_str = entrada_str[1:]
    
    if not ('A' <= coluna_char <= 'J') or not linha_str.isdigit():
        return None, None
        
    linha_int = int(linha_str)
    if not (1 <= linha_int <= 10):
        return None, None
        
    coluna_int = ord(coluna_char) - 64 
    return linha_int, coluna_int


def pedir_coordenada():
    while True:
        entrada = input("Sua jogada (ex.: C5): ")
        linha, coluna = converter_coordenada(entrada)
        
        if linha is not None and coluna is not None:
            return linha, coluna
        
        print("Entrada inválida! Digite uma letra entre A-J e um número de 1 a 10 (ex: C5).")