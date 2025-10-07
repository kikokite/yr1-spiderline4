# 🕷️ Spider Line 4

**Spider Line 4** is a variant of the classic **Connect Four** game, developed in Python with Pygame.  
It introduces new mechanics, AI opponents with adjustable difficulty, and a dynamic board size for an enhanced gameplay experience.

---

## 🎮 The Game

Unlike the traditional Connect Four, pieces in Spider Line 4 can **only be placed on the board’s edges or in front of already placed pieces**.  
Players alternate turns until one connects four pieces (horizontally, vertically, or diagonally) or the board is full.

### 🧩 Key Features
- Five possible board sizes: `6x6`, `7x7`, `8x8`, `9x9`, `10x10`
- Two piece colors: **Red** and **Blue**
- Visual hints for valid moves (highlighted when hovering)
- Intuitive graphical interface with menus and game options
- Multiple game modes:
  - 🧍 **Player vs Player**
  - 💻 **Player vs Computer**
  - 🤖 **Computer vs Computer**

---

## 🧠 Algorithms & Difficulty

Spider Line 4 includes AI opponents with varying skill levels based on different search algorithms:

- **Minimax** — classic decision tree with α–β pruning  
- **Negamax** — simplified Minimax variant with heuristic evaluation  
- **Monte Carlo Tree Search (MCTS)** — probabilistic search with exploration/exploitation balance  

The **heuristic function** prioritizes control of the board center, as occupying central positions increases the chance of winning.  
For larger boards (9x9, 10x10), computation time increases due to the expanded search space.

---

## ⚙️ Installation & Setup

Clone the repository and install the dependencies:

```bash
git clone https://github.com/<your-username>/Spider-Line-4.git
cd Spider-Line-4
pip install -r requirements.txt



## Bibliography
- https://www.youtube.com/watch?v=l-hh51ncgDI
- https://www.youtube.com/watch?v=zp3VMe0Jpf8
- https://www.youtube.com/watch?v=6TsL96NAZCo
- https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5



