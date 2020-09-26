
# N QUEEN PROBLEM
# Given a positive number n, returns how many legal chess boards of size nXn can contain N queens

def find_j(partial):
    '''(list) -> (int)
        returns the first empty row in partial board'''
    j=0
    while (j<len(partial)):
        if "Q" not in partial[j]:
            return j
        j+=1
    
def legal(partial, i):
    j = find_j(partial)    #find the first empty row
    row=0
    while(row<j):
        if(partial[row][i] == "Q"):
            return False
        row +=1
        
    index = i-1
    row = j-1
    while(index >= 0 and row >= 0):
        if(partial[row][index] == "Q"):
            return False
        index -=1
        row -=1
        
    index = i+1
    row = j-1
    while (index < len(partial) and row >=0):
        if partial[row][index] == "Q":
            return False
        index +=1
        row -=1
        
    return True
        
def queens(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    partial = [[' ']*n for i in range(0,n)]
    return count_legal(partial, n, 0)

def count_legal(partial,n, row):
    count =0
    for i in range(0,n):
        if legal(partial, i):
            if row == n-1:
                count +=1
            else:
                partial[row][i] = 'Q'
                count += count_legal(partial, n, row+1)
        partial[row][i] = ' '
    return count
  
# Harder version - Given a chess board of size N*N containing only dragons, returns how many
# legal ways exist to locate N queens on the board.

def legal_dragons(board, row, col):
    if row == 0 and col ==0:
        return True
    
    if board[row][col] == 'D':
        return False
        
    dragon = False
    queen = False
    j = row -1
    i = col 
    while( j>=0 and not dragon):
        if board[j][i] == 'D':
            dragon = True
        if board[j][i] == 'Q' and not dragon:
            return False
        j-=1

    
    dragon = False
    queen = False
    j = row -1
    i = col -1
    while(j >= 0 and i >=0 and not dragon):
        if board[j][i] == 'D':
            dragon = True
        if board[j][i] == 'Q' and not dragon:
            return False
        j-=1
        i-=1

    dragon = False
    queen = False
    j= row +1
    i = col -1
    while( j < len(board) and i >= 0 and not dragon):
        if board[j][i] == 'D':
            dragon = True
        if board[j][i] =='Q' and not dragon:
            return False
        j +=1
        i -=1
  
    dragon = False
    queen = False
    j = row
    i = col-1
    while(i >= 0 and not dragon):
        if board[j][i] == 'D':
            dragon = True
        if board[j][i] == 'Q' and not dragon:
            return False
        i -=1
        

    return True
    
    
def queens_dragons(board):
    return queens_dragons_rec(len(board), 0, 0, board)

def queens_dragons_rec(remaining, row, col, board):
    count =0
    while(col < len(board)):
        while(row < len(board)):
            if board[row][col] != 'D':
                if legal_dragons(board, row, col):
                    if (remaining == 1):
                        count +=1
                    else:
                        board[row][col] = 'Q'
                        if row == len(board) - 1 :
                            count += queens_dragons_rec(remaining-1, 0, col+1, board)
                        else:
                            count += queens_dragons_rec(remaining -1, row+1, col, board)
                board[row][col] = ' '
                

            row +=1
        row = 0    
        col +=1
    return count
