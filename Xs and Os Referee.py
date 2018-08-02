def checkio(board):
    transposed = [''.join(i) for i in zip(*board)]
    for i in board+transposed:       
      if 3*i[0] == i and '.' not in i[0]: return i[0]
            
    if (board[0][0] == board[1][1] == board[2][2] or \
        board[2][0] == board[1][1] == board[0][2]) and board[1][1].isalpha():
            return board[1][1]
    
    return "D"