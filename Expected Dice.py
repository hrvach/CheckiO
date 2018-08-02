from itertools import *
from random import choice

def expected(dice_number, sides, target, board, iterations=200000):
    rolled = list(map(sum, product(range(1, sides+1), repeat=dice_number)))  
    board_size = len(board)
    modulo = lambda x: x % board_size

    moves = []
    position = 0

    for i in range(iterations):
        moves.append(0)
        position = 0
        while position != target:
            roll = choice(rolled)                               # Roll
            position = modulo(position + roll)                  # Move
            moves[-1] += 1                                      # Write down moves
            
            if board[position]:              # If we land on redirect
                position = modulo(position + board[position]) # Move again
            
    avg = lambda x: round(float(sum(x))/len(x), 1)
    return (avg(moves))