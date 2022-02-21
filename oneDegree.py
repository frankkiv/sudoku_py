def same_row(i,j): return (i//9 == j//9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i//27 == j//27 and i%9//3 == j%9//3)

def solveSudoku(board):
    ans = []
    idx = board.index('0') if '0' in board else -1

    if idx == -1: # puzzle solved
        return [board]
    exclude = {board[j] for j in range(81) if same_row(idx,j) or same_col(idx,j) or same_block(idx,j)}

    for m in set('123456789')-exclude:
        ans += solveSudoku(board[:idx]+[m]+board[idx+1:])
    return ans


sudoku= \
["9","8","4","6","7","2","5","3","1",
 "0","0","7","0","0","0","6","4","9",
 "6","1","3","5","4","9","0","2","0",
 "0","6","0","9","0","8","3","7","4",
 "0","0","9","0","6","0","1","8","5",
 "0","0","8","0","0","0","9","6","2",
 "0","3","2","0","0","7","4","9","6",
 "0","4","0","3","9","0","2","1","0",
 "0","9","0","0","0","0","0","5","3"]

import time
tStart = time.time() #start
ans = solveSudoku(sudoku)
print(ans)
for a in ans:
    for i in range(9):
        print(a[i*9:i*9+9])
    print('---------------') #if there is more than one solution
tEnd = time.time() #end
print("Total time= %f seconds" % (tEnd - tStart))

