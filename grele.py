import math
moves = [0, 1, 2, -1, 5, -3]

# Red is maximizing
# Black is minimizing
RED = 1
BLACK = -1

def best_move(moves, is_maximizing_player):
    if is_maximizing_player:
        best_move = -math.inf
        for move in moves:
            if move > best_move:
                best_move = move
        return best_move
    
    else:
        best_move = math.inf
        for move in moves:
            if move < best_move:
                best_move = move
        return best_move

def best_move_int(moves, player_int):
    best_move = -math.inf
    for move in moves:
        if move * player_int > best_move:
            best_move = move 
    return best_move

print(best_move_int(moves, RED))
print(best_move_int(moves, BLACK))