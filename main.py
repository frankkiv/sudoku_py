
import time
import csv
from sudoku import Sudoku
from oneDimSolution import OneDimensionSudoku
# load 2d array from csv
with open('input.csv', newline='') as csvfile:
    board = []
    reader = csv.reader(csvfile)
    for row in reader:
        board.append([int(val) for val in row])

tStart = time.time() # time start 

# init Solution class
s = Sudoku()
s.solveSudoku(board)

# s = OneDimensionSudoku()
# ans = s.solveSudoku(s.to1DList(board))
# print(ans)
# for a in ans:
#     for i in range(9):
#         print(a[i*9:i*9+9])
#     print('---------------') #if there is more than one solution

tEnd = time.time() # time end 
print("Total time= %f seconds" % (tEnd - tStart))


# Mock data
# sudoku= \
# [["5","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]]