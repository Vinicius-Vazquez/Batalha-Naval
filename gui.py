"""
Módulo de Interface Gráfica Estilizada em Tkinter.
Desenvolvido para Batalha Naval - GPTech Games.
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
import time
import os

from tabuleiro import criar_tabuleiro
from navios import criar_frota, posicionar_frota_automaticamente, checar_se_afundou, checar_vitoria
from computador import ComputadorIA
from estatisticas import salvar_estatisticas
from replay import salvar_replay


# ==============================================================
# PALETA DE CORES & ESTILOS TÁTICOS
# ==============================================================
BG_DARK = "#0F172A"       # Azul Escuro Profundo (Fundo)
BG_CARD = "#1E293B"       # Cartões e Containers
ACCENT_BLUE = "#38BDF8"   # Azul Neon (Destaques)
ACCENT_GREEN = "#22C55E"  # Verde Sucesso
ACCENT_RED = "#EF4444"    # Vermelho Alerta / Acerto
COLOR_WATER = "#1E3A5F"   # Água do Tabuleiro
COLOR_MISS = "#64748B"    # Cor para Tiro na Água
COLOR_SHIP = "#475569"    # Navio Humano
TEXT_LIGHT = "#F8FAFC"    # Texto Principal
FONT_MAIN = ("Consolas", 10, "bold") # Fonte estilo radar/terminal


class BatalhaNavalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("⚡ BATALHA NAVAL - GPTech Games")
        self.root.configure(bg=BG_DARK)
        self.root.geometry("820x520")
        self.root.resizable(False, False)

        self.computador = ComputadorIA()
        
        self.modo_de_jogo = None
        self.turno_atual = 1
        self.inicio_tempo = None
        self.total_jogadas = 0
        self.acertos_j1 = 0
        self.acertos_j2 = 0
        self.historico_jogadas = []

        self.botoes_alvo = {}
        self.botoes_frota = {}

        self.criar_menu_inicial()

    def limpar_janela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ==============================================================
    # MENUS COM DESIGN MODERNO
    # ==============================================================
    def criar_menu_inicial(self):
        self.limpar_janela()
        self.root.geometry("450x520")

        frame_card = tk.Frame(self.root, bg=BG_CARD, padx=30, pady=30, highlightbackground=ACCENT_BLUE, highlightthickness=1)
        frame_card.pack(expand=True, padx=20, pady=20)

        lbl_icone = tk.Label(frame_card, text="⚓", font=("Arial", 36), bg=BG_CARD, fg=ACCENT_BLUE)
        lbl_icone.pack()

        lbl_titulo = tk.Label(frame_card, text="BATALHA NAVAL", font=("Segoe UI", 20, "bold"), bg=BG_CARD, fg=TEXT_LIGHT)
        lbl_titulo.pack()

        lbl_sub = tk.Label(frame_card, text="— GPTech Games —", font=("Segoe UI", 10, "italic"), bg=BG_CARD, fg=ACCENT_BLUE)
        lbl_sub.pack(pady=(0, 20))

        botoes = [
            ("⚔️ Jogador vs Computador", self.iniciar_pvc),
            ("👥 Jogador vs Jogador", self.iniciar_pvp),
            ("📊 Ver Estatísticas", self.exibir_estatisticas_gui),
            ("🎬 Reproduzir Replay", self.reproduzir_replay_gui),
            ("🚪 Sair do Jogo", self.root.quit)
        ]

        for text, command in botoes:
            btn = tk.Button(
                frame_card, text=text, font=("Segoe UI", 11, "bold"), bg=BG_DARK, fg=TEXT_LIGHT,
                activebackground=ACCENT_BLUE, activeforeground=BG_DARK, bd=0, relief="flat",
                width=24, pady=8, cursor="hand2", command=command
            )
            btn.pack(pady=6)
            self._aplicar_hover(btn, bg_normal=BG_DARK, bg_hover=ACCENT_BLUE, fg_normal=TEXT_LIGHT, fg_hover=BG_DARK)

    def _aplicar_hover(self, btn, bg_normal, bg_hover, fg_normal, fg_hover):
        """Adiciona animação de passar o mouse por cima dos botões."""
        btn.bind("<Enter>", lambda e: btn.config(bg=bg_hover, fg=fg_hover))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg_normal, fg=fg_normal))

    def ler_arquivo(self, caminho):
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return "Nenhum histórico registrado ainda. Jogue uma partida!"

    def exibir_estatisticas_gui(self):
        dados = self.ler_arquivo(os.path.join("data", "estatisticas.txt"))
        messagebox.showinfo("📊 Estatísticas Táticas", dados)

    def reproduzir_replay_gui(self):
        dados = self.ler_arquivo(os.path.join("data", "replay.txt"))
        janela_replay = tk.Toplevel(self.root)
        janela_replay.title("🎬 Replay da Última Batalha")
        janela_replay.configure(bg=BG_DARK)
        janela_replay.geometry("420x350")
        
        texto = scrolledtext.ScrolledText(janela_replay, width=45, height=16, font=FONT_MAIN, bg=BG_CARD, fg=TEXT_LIGHT)
        texto.pack(padx=10, pady=10)
        texto.insert(tk.INSERT, dados)
        texto.config(state=tk.DISABLED)

    # ==============================================================
    # TELA DE JOGO E TABULEIROS
    # ==============================================================
    def configurar_partida(self, modo):
        self.modo_de_jogo = modo
        self.inicio_tempo = time.time()
        self.total_jogadas = 0
        self.acertos_j1 = 0
        self.acertos_j2 = 0
        self.historico_jogadas = []
        self.turno_atual = 1

        self.tab_j1_real = criar_tabuleiro()
        self.tab_j1_visivel = criar_tabuleiro()
        self.frota_j1 = criar_frota()
        posicionar_frota_automaticamente(self.tab_j1_real, self.frota_j1)

        self.tab_adv_real = criar_tabuleiro()
        self.tab_adv_visivel = criar_tabuleiro()
        self.frota_adv = criar_frota()
        posicionar_frota_automaticamente(self.tab_adv_real, self.frota_adv)

    def iniciar_pvc(self):
        self.computador.reset()
        self.configurar_partida('PVC')
        self.montar_tela_tabuleiros("🛡️ Sua Frota", "🎯 Frota Inimiga")

    def iniciar_pvp(self):
        self.configurar_partida('PVP')
        self.tela_de_transicao()

    def tela_de_transicao(self):
        self.limpar_janela()
        self.root.geometry("450x320")
        
        frame = tk.Frame(self.root, bg=BG_CARD, padx=20, pady=20, highlightbackground=ACCENT_BLUE, highlightthickness=1)
        frame.pack(expand=True)

        tk.Label(frame, text="🔒 TROCA DE COMANDO", font=("Segoe UI", 16, "bold"), bg=BG_CARD, fg=ACCENT_RED).pack(pady=10)
        tk.Label(frame, text=f"Passe o controle para o JOGADOR {self.turno_atual}!", font=("Segoe UI", 11), bg=BG_CARD, fg=TEXT_LIGHT).pack(pady=5)
        
        btn_pronto = tk.Button(
            frame, text="PRONTO PARA COMBATE", font=("Segoe UI", 11, "bold"), bg=ACCENT_GREEN, fg=BG_DARK,
            bd=0, padx=15, pady=8, cursor="hand2", command=self.preparar_tabuleiros_pvp
        )
        btn_pronto.pack(pady=20)

    def preparar_tabuleiros_pvp(self):
        if self.turno_atual == 1:
            self.montar_tela_tabuleiros("🛡️ Frota do Jogador 1", "🎯 Tabuleiro do Jogador 2")
        else:
            self.montar_tela_tabuleiros("🛡️ Frota do Jogador 2", "🎯 Tabuleiro do Jogador 1")

    def montar_tela_tabuleiros(self, titulo_frota, titulo_alvo):
        self.limpar_janela()
        self.root.geometry("820x520")

        # Cabeçalho Status
        frame_status = tk.Frame(self.root, bg=BG_CARD, pady=5)
        frame_status.pack(fill=tk.X, padx=10, pady=(10, 0))

        self.lbl_status = tk.Label(frame_status, text="🎯 SEU TURNO: Clique em um quadrado do radar inimigo para disparar!", font=("Segoe UI", 11, "bold"), bg=BG_CARD, fg=ACCENT_BLUE)
        self.lbl_status.pack()

        frame_jogos = tk.Frame(self.root, bg=BG_DARK, padx=5, pady=5)
        frame_jogos.pack(expand=True)

        matriz_frota = self.tab_j1_real if self.turno_atual == 1 else self.tab_adv_real
        matriz_alvo = self.tab_adv_visivel if self.turno_atual == 1 else self.tab_j1_visivel

        # Frame Frota (Esquerda)
        frame_frota = tk.LabelFrame(frame_jogos, text=f" {titulo_frota} ", font=("Segoe UI", 10, "bold"), bg=BG_DARK, fg=TEXT_LIGHT)
        frame_frota.pack(side=tk.LEFT, padx=10)
        self.botoes_frota = {}
        self._construir_grade(frame_frota, self.botoes_frota, iterativo=False)
        self._colorir_frota_visivel(matriz_frota)

        # Frame Alvo (Direita)
        frame_alvo = tk.LabelFrame(frame_jogos, text=f" {titulo_alvo} ", font=("Segoe UI", 10, "bold"), bg=BG_DARK, fg=ACCENT_BLUE)
        frame_alvo.pack(side=tk.RIGHT, padx=10)
        self.botoes_alvo = {}
        self._construir_grade(frame_alvo, self.botoes_alvo, iterativo=True)
        self._restaurar_estado_alvo(matriz_alvo)

        # Botão de passar turno no modo PvP
        if self.modo_de_jogo == 'PVP':
            self.btn_passar = tk.Button(
                self.root, text="🔄 PASSAR TURNO", font=("Segoe UI", 10, "bold"), bg=COLOR_MISS, fg=TEXT_LIGHT,
                bd=0, state=tk.DISABLED, cursor="hand2", command=self.passar_turno_pvp
            )
            self.btn_passar.pack(pady=5)

    def _construir_grade(self, pai, dicionario, iterativo):
        colunas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for c, letra in enumerate(colunas, start=1):
            tk.Label(pai, text=letra, font=FONT_MAIN, bg=BG_DARK, fg=ACCENT_BLUE, width=3).grid(row=0, column=c)

        for r in range(1, 11):
            tk.Label(pai, text=f"{r:2d}", font=FONT_MAIN, bg=BG_DARK, fg=ACCENT_BLUE, width=3).grid(row=r, column=0)
            for c in range(1, 11):
                cmd = (lambda l=r, col=c: self.registrar_disparo(l, col)) if iterativo else None
                btn = tk.Button(
                    pai, text="~", font=FONT_MAIN, width=3, height=1,
                    bg=COLOR_WATER, fg=ACCENT_BLUE, bd=1, relief="ridge", command=cmd
                )
                btn.grid(row=r, column=c, padx=1, pady=1)
                
                if iterativo:
                    self._aplicar_hover(btn, bg_normal=COLOR_WATER, bg_hover=ACCENT_BLUE, fg_normal=ACCENT_BLUE, fg_hover=BG_DARK)
                
                dicionario[(r, c)] = btn

    def _colorir_frota_visivel(self, matriz_frota_real):
        for r in range(1, 11):
            for c in range(1, 11):
                valor = matriz_frota_real[r][c]
                btn = self.botoes_frota[(r, c)]
                if valor == 'N':
                    btn.config(bg=COLOR_SHIP, fg=TEXT_LIGHT, text="N")
                elif valor == 'X':
                    btn.config(bg=ACCENT_RED, fg=TEXT_LIGHT, text="💥")
                elif valor == 'O':
                    btn.config(bg=COLOR_MISS, fg=TEXT_LIGHT, text="•")

    def _restaurar_estado_alvo(self, matriz_alvo_visivel):
        for r in range(1, 11):
            for c in range(1, 11):
                valor = matriz_alvo_visivel[r][c]
                btn = self.botoes_alvo[(r, c)]
                if valor == 'X':
                    btn.config(bg=ACCENT_RED, fg=TEXT_LIGHT, text="💥", state=tk.DISABLED)
                elif valor == 'O':
                    btn.config(bg=COLOR_MISS, fg=TEXT_LIGHT, text="•", state=tk.DISABLED)

    # ==============================================================
    # LOGICA DE JOGO E ANIMAÇÃO BÁSICA
    # ==============================================================
    def registrar_disparo(self, r, c):
        btn = self.botoes_alvo[(r, c)]
        if btn['state'] == tk.DISABLED:
            return

        coordenada = f"{chr(64 + c)}{r}"
        
        if self.turno_atual == 1:
            matriz_real_alvo = self.tab_adv_real
            matriz_visivel_alvo = self.tab_adv_visivel
            frota_alvo = self.frota_adv
            quem_atirou = "Jogador 1" if self.modo_de_jogo == 'PVP' else "Jogador"
        else:
            matriz_real_alvo = self.tab_j1_real
            matriz_visivel_alvo = self.tab_j1_visivel
            frota_alvo = self.frota_j1
            quem_atirou = "Jogador 2"

        if matriz_real_alvo[r][c] == 'N':
            matriz_real_alvo[r][c] = 'X'
            matriz_visivel_alvo[r][c] = 'X'
            btn.config(text="💥", bg=ACCENT_RED, fg=TEXT_LIGHT, state=tk.DISABLED)
            resultado = 'Acerto'
            
            if self.turno_atual == 1:
                self.acertos_j1 += 1
            else:
                self.acertos_j2 += 1

            msg = f"🔥 ALVO ATINGIDO em {coordenada}!"
            for navio in frota_alvo:
                if (r, c) in navio["posicoes"] and checar_se_afundou(matriz_real_alvo, navio):
                    msg = f"☠️ NAVIO AFUNDADO: {navio['tipo'].upper()}!"
        else:
            matriz_real_alvo[r][c] = 'O'
            matriz_visivel_alvo[r][c] = 'O'
            btn.config(text="•", bg=COLOR_MISS, fg=TEXT_LIGHT, state=tk.DISABLED)
            resultado = 'Água'
            msg = f"🌊 TIRO NA ÁGUA em {coordenada}."

        self.total_jogadas += 1
        self.historico_jogadas.append(f"{quem_atirou} - {coordenada} - {resultado}")
        self.lbl_status.config(text=msg)

        for b in self.botoes_alvo.values():
            b.config(state=tk.DISABLED)

        if checar_vitoria(frota_alvo):
            self.finalizar_partida(quem_atirou)
            return

        if self.modo_de_jogo == 'PVP':
            self.btn_passar.config(state=tk.NORMAL, bg=ACCENT_GREEN, fg=BG_DARK)
        elif self.modo_de_jogo == 'PVC':
            self.root.after(800, self.jogada_do_computador)

    def passar_turno_pvp(self):
        self.turno_atual = 2 if self.turno_atual == 1 else 1
        self.tela_de_transicao()

    def jogada_do_computador(self):
        coord, result = self.computador.realizar_jogada(self.tab_j1_real, self.tab_j1_visivel, self.frota_j1)
        self.historico_jogadas.append(f"Computador - {coord} - {result}")
        self.total_jogadas += 1

        self._colorir_frota_visivel(self.tab_j1_real)

        if checar_vitoria(self.frota_j1):
            self.finalizar_partida("Computador")
            return
            
        self.lbl_status.config(text=f"🤖 O Computador atirou em {coord} ({result.upper()}). Sua vez!")
        
        for (r, c), btn in self.botoes_alvo.items():
            if self.tab_adv_visivel[r][c] not in ['X', 'O']:
                btn.config(state=tk.NORMAL)

    def finalizar_partida(self, vencedor):
        duracao = int(time.time() - self.inicio_tempo)
        salvar_estatisticas(vencedor, self.total_jogadas, self.acertos_j1)
        salvar_replay(self.historico_jogadas)

        messagebox.showinfo("🏆 VITORIA TÁTICA!", f"PARTIDA ENCERRADA!\n\n👑 Vencedor: {vencedor}\n🎯 Total de Jogadas: {self.total_jogadas}\n⏱️ Tempo de Batalha: {duracao} segundos")
        self.criar_menu_inicial()


def iniciar_interface_grafica():
    root = tk.Tk()
    app = BatalhaNavalGUI(root)
    root.mainloop()


if __name__ == "__main__":
    iniciar_interface_grafica()