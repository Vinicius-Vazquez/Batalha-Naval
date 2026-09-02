# ⚓ Batalha Naval — GPTech Games

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Projeto acadêmico desenvolvido em Python focado na implementação da lógica do clássico jogo **Batalha Naval**, oferecendo tanto modo gráfico moderno (GUI) quanto modo via terminal (CLI), além de suporte a inteligência artificial tática, gerenciamento de estatísticas e sistema de replay das partidas.

---

## 📌 Sumário

- [Visão Geral](#-visão-geral)
- [Funcionalidades e Requisitos](#-funcionalidades-e-requisitos)
- [Arquitetura do Sistema](#-arquitetura-do-sistema)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Como Executar](#-como-executar)
- [Conceitos Aplicados](#-conceitos-aplicados)
- [Demonstração em Vídeo](#-demonstração-em-vídeo)
- [Autor](#-autor)

---

## 🎯 Visão Geral

O projeto consiste na recriação do jogo Batalha Naval com o objetivo de praticar conceitos fundamentais e intermediários da ciência da computação e engenharia de software, incluindo **programação orientada a objetos (POO)**, **estruturas de dados bidimensionais (matrizes)**, **inteligência artificial para jogos (algoritmos heurísticos)**, **persistência de dados via E/S de arquivos** e **interfaces gráficas orientadas a eventos**.

---

## 🚀 Funcionalidades e Requisitos

Abaixo está o mapeamento dos Requisitos Funcionais (RF) implementados no sistema:

| ID | Requisito Funcional | Módulo/Implementação |
| :--- | :--- | :--- |
| **RF01** | Menu principal com opções do sistema | `gui.py` e `main.py` |
| **RF02** | Tabuleiro de $10 \times 10$ para cada jogador | `tabuleiro.py` |
| **RF03** | Tipos de navio: pequeno (2 pos.) e grande (4 pos.) | `navios.py` |
| **RF04** | Posicionamento automático sem sobreposição | `navios.py` |
| **RF05** | Validação de jogadas (coordenadas válidas e não repetidas) | `gui.py` / `computador.py` |
| **RF06** | Mensagens de água, acerto e navio afundado | `gui.py` |
| **RF07** | Encerramento exibindo vencedor, jogadas e tempo | `gui.py` |
| **RF08** | Iniciar nova partida a qualquer momento | `gui.py` |
| **RF09** | Modos de jogo: PvC e PvP | `gui.py` e `computador.py` |
| **RF10** | Posicionamento e conferência dos navios | `gui.py` / `navios.py` |
| **RF11** | Registro do histórico de jogadas | `replay.py` |
| **RF12** | Estatísticas de desempenho acumuladas | `estatisticas.py` |
| **RF13** | Modo replay da última partida | `replay.py` / `gui.py` |

---

## 🧠 Arquitetura do Sistema

O software foi construído seguindo o princípio da **responsabilidade única (SoC)**, mantendo a regra de negócio totalmente separada da interface do usuário.

```text
                  ┌────────────────────────┐
                  │    Ponto de Entrada    │
                  │       (main.py)        │
                  └───────────┬────────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
    ┌──────────────────┐            ┌──────────────────┐
    │  Interface (GUI) │            │  Modo Terminal   │
    │     (gui.py)     │            │    (CLI/Core)    │
    └─────────┬────────┘            └─────────┬────────┘
              │                               │
              └───────────────┬───────────────┘
                              │
     ┌────────────────────────┼────────────────────────┐
     ▼                        ▼                        ▼
┌───────────────┐    ┌─────────────────┐     ┌───────────────────┐
│ Tabuleiro &   │    │  Inteligência   │     │  Estatísticas &   │
│ Frota (Navios)│    │ Artificial (IA) │     │ Persistência/Data │
└───────────────┘    └─────────────────┘     └───────────────────┘
```
---

## 📁 Estrutura do Repositório

```text
batalha_naval/
│
├── data/                      # Diretório reservado para persistência de dados
│   ├── estatisticas.txt       # Registro bruto acumulado de desempenho
│   └── ultimo_replay.txt      # Histórico serializado da última batalha
│
├── computador.py              # Algoritmo de IA e estado de caça/disparo
├── estatisticas.py            # Manipulação de E/S do relatório estatístico
├── gui.py                     # Interface Gráfica construída em Tkinter
├── main.py                    # Script de inicialização do programa
├── navios.py                  # Definições, posicionamento e colisão da frota
├── replay.py                  # Leitura e gravação de logs de partidas
└── tabuleiro.py               # Lógica de criação e gerenciamento das matrizes
```

---

## ⚙️ Como Executar

## Passo a passo:
1. Clone este repositório:
```bash
  git clone https://github.com/Vinicius-Vazquez/batalha-naval.git
cd batalha-naval
```

2. Execute o programa:
```bash
  python main.py
```

3. Escolha o modo de execução desejado (Interface Gráfica ou Terminal) no menu inicial.

---

## 💻 Conceitos Aplicados

- **Matrizes Bidimensionais:** Representação dos mapas $10 \times 10$ onde cada coordenada gerencia o estado da célula (água, navio ou alvo atingido).
- **Algoritmo de IA Tática:** A máquina opera em dois modos:
  - *Modo Busca (Aleatório):* Disparos aleatórios no tabuleiro procurando alvos não revelados.
  - *Modo Caça (Adjacência):* Ao atingir um navio, armazena a posição e prioriza células vizinhas na vertical/horizontal.
- **Persistência em Arquivos (I/O):** Leitura, sanitização de dados e gravação em tempo de execução sem corromper dependências de exibição.
- **Desenvolvimento de GUI Orientado a Eventos:** Uso de *callbacks*, janelas de diálogo do `tkinter.messagebox` e customização geométrica.

---

## 📹 Demonstração em Vídeo

- 🔗 [Clique aqui para assistir ao vídeo de apresentação do projeto no YouTube/Drive](https://link-do-seu-video-aqui.com) *(Duração: +5 min)*

---

## 🧑‍💻 Autor

Desenvolvido por **Vinicius Souza Vazquez**  
Estudante de **Engenharia da Computação — CEFET-MG (Campus Divinópolis)**  
Disciplina: Programação em Python | Professor: Guido Pantuza  

---
*Projeto acadêmico desenvolvido para a empresa fictícia GPTech Games.*
