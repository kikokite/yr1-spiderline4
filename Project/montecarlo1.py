import copy
import random
import math
from carqueija_update import *



class Node:  
    def __init__(self, board, player, row, col, move = None , parent=None):
        self.row = row
        self.col = col
        self.board = board  #Instancia da classe board 
        self.parent = parent
        self.children = []
        self.move = move
        self.wins = 0
        self.visits = 0
        self.player = player

        

    def is_leaf(self):
        if (len(self.children) == 0) or self.board.win(1) or self.board.win(2) or self.board.is_full():
            return True
        else:
            return False
    def is_terminal(self):
        if self.board.win(1) or self.board.win(2) or self.board.is_full():
            return True
        else:
            return False
    def has_unexplored_moves(self):
        unexplored_moves = self.board.actions()
        if unexplored_moves: 
            return True
        else:
            return False
    
    def expand(self):
        # Identifica as jogadas possíveis que ainda não foram exploradas
        unexplored_moves = self.board.actions()
        
        if unexplored_moves:
            # Escolhe uma jogada não explorada aleatoriamente para a expansão
            move = random.choice(unexplored_moves)
            row_move = move[0]
            col_move = move[1]
            
            # Cria uma cópia do estado do tabuleiro e aplica a jogada escolhida
            new_board = copy.deepcopy(self.board)
            new_board.put_piece(self.player, row_move, col_move)
            
            # Cria um novo nó filho com o estado resultante e adiciona à lista de filhos
            new_node = Node(board=new_board, player= self.player, row = self.row, col = self.col, move=move, parent=self)
            self.children.append(new_node)
            
            # Retorna o novo nó para que seja utilizado na simulação
            return new_node
        
        # Retorna None se não houver mais movimentos não exploradoss
        return self

    def select_child(self, c):
        
        best_score = -float("inf")
        best_children = []
        unvisited_children = []

        for child in self.children:
            if child.visits == 0:
                unvisited_children.append(child)
            else:
                exploration_term = math.sqrt((math.log(self.visits+1)*2) / child.visits)
                score = child.wins / child.visits + c * exploration_term
                if  score == best_score:
                    best_score = score
                    best_children = [child]
                elif score > best_score:
                    best_score = score
                    best_children = [child]
            if len(unvisited_children) > 0:
                return random.choice(unvisited_children)
        return random.choice(best_children)
    
    def backpropagate(self, result, player):
        self.visits += 1
        if self.player == player:
            self.wins += result
        if self.parent is not None:
            self.parent.backpropagate(result, player)


def monte_carlo_tree_search(board, player,c, simulations, row, col):
    # Passo 1: Inicialize a árvore
    root = Node(board, player, row, col)

    count = 0
    for _ in range(simulations):
        node = root
        
        while not node.has_unexplored_moves():
            node = node.select_child(c)
        
        if not node.is_terminal():
            node = node.expand()
            count+= 1

        if not node.is_terminal(): 
            result = simulate_random_playout(node.board, player)
            node.backpropagate(result, player)

        else: 
            if(node.board.win(3-player)):
                node.backpropagate(1,3-player)
            elif (node.board.win(player)):
                node.backpropagate(1, player)
            elif(node.board.is_full()):
                node.backpropagate(0.5, player)

        

    best_ratio = -float("inf")
    best_move = None
    for child in root.children:
        if child.visits > 0:
            ratio = child.wins / child.visits
            print(f"{ratio} Coluna: {child.move} Numero de Vitorias: {child.wins} Numero de Visitas: {child.visits}")
        else:
            ratio = 0
        if ratio > best_ratio:
            best_ratio = ratio
            best_move = child.move
    print(f"Numero de Expansoes:  {count}")
    #Retorna o movimento do melhor filho
    return best_move
        
    
def simulate_random_playout(game_state, player):
    simulated_game = copy.deepcopy(game_state)
    current_player = player
    while not simulated_game.is_full() and not simulated_game.win(current_player):
        possible_moves = simulated_game.actions()
        move = random.choice(possible_moves)
        row_move = move[0]
        col_move = move[1]
        simulated_game.put_piece(current_player, row_move, col_move)
        if simulated_game.win(current_player):
            return 1 if current_player == player else 0
        current_player = 1 if current_player == 2 else 2  # Switch player
    
    if simulated_game.win(current_player):
        return 1 if current_player == player else 0
    else:
        return 0 # Consider draw as half a win

