
import time
import csv
from sudoku import Sudoku
# load 2d array from csv
with open('input.csv', newline='') as csvfile:
    board = []
    reader = csv.reader(csvfile)
    for row in reader:
        board.append([int(val) for val in row])

# init Solution class
s = Sudoku()

# generate random board for fun
board = s.genRandomBoard()
s.report()

tStart = time.time() # time start 

s.solveSudoku(board)
s.report()

tEnd = time.time() # time end 
print("Total time= %f seconds" % (tEnd - tStart))
