from random import sample
from itertools import islice
import sudokusolver as ss
import sudokuvalid as sv

base  = 3
side  = base*base

# make a sudoku board
def makesudoku():
    def pattern(r,c): return (base*(r%base)+r//base+c)%side
    def shuffle(s): return sample(s,len(s))
    rBase = range(base)
    rows = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1,base*base+1))
    board = [[nums[pattern(r,c)] for c in cols] for r in rows]
    return board

# remove some elements from sudoku board depending on the difficulty
def sudokuempty(board,difficulty):
    squares = side*side
    empties = squares * difficulty//8
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0
    numSize = len(str(side))
    return board

# function to check if board is full or not
def checkifanyempty(board):
    for i in range(len(board)):
        if "" in board[i]:
            return False
    return True

# driver code to create and return sudoku board
def createboard(difficulty):
    board1 = makesudoku()
    finalboard = sudokuempty(board1, difficulty)
    return finalboard

# driver code to check validity of sudoku board
def isvalid(board):
    grid = []
    for x in board:
        temp = []
        for y in x:
            if y == "":
                temp.append(0)
            else:
                temp.append(int(y))
        grid.append(temp)
    a = ss.solver(grid)
    b = sv.valid_board(grid)
    if a == False or b == False:
        return False
    else:
        return True

#driver code, returns if board is valid and is not empty   
def checkboard(board):
    return {'validity': isvalid(board), 'isfull': checkifanyempty(board)}
     
#driver code to solve a given sudoku board  
def solve(board):
    grid = []
    for x in board:
        temp = []
        for y in x:
            if y == "":
                temp.append(0)
            else:
                temp.append(int(y))
        grid.append(temp)
    if sv.valid_board(grid):
        return ss.solver(grid)
    else:
        return False
    
    
