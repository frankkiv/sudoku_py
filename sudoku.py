import random


class Sudoku:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.board = board
        self.solve()

    # find the "." and return the position
    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.findUnassigned()
        # no unassigned position is found, puzzle solved
        if row == -1 and col == -1:
            return True

        # loop number from 1 to 9
        for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            # for each number check if it's safe or not
            if self.isSafe(row, col, num):
                # if number is valid and go run solve again to check next unassigned number
                self.board[row][col] = num
                if self.solve():
                    return True
                # if solve is False, need to overwrite the number back to the "0"
                self.board[row][col] = 0
        return False

    # check if the number is safe
    def isSafe(self, row, col, ch):
        # box row/col is to caculate the box position
        boxrow = row - row % 3
        boxcol = col - col % 3
        if self.checkrow(row, ch) and self.checkcol(col, ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False

    # check if the number already exist in the row
    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    # check if the number already exist in the col
    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    # check if the number already exist in the square
    def checksquare(self, row, col, ch):
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == ch:
                    return False
        return True

    # it's nothing, just a format prettier
    def report(self):
        # 2D to 1D list
        for a in self.board:
            print(a)
        print("---------------")

    def genRandomBoard(self, unknown = 60):
        # generate 9x9 2D array with default value 0
        board = []
        for i in range(1, 10):
            board.append([0 for j in range(1, 10)])

        # random pick a column
        # fill the random non-repetitive number from 1 to 9
        randomCol = random.randint(0, 9)
        randNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(randNumbers)
        board[randomCol] = randNumbers

        # call solve the board
        self.solveSudoku(board)

        # pick random position and purge the number to 0
        purgeTotal = unknown
        while purgeTotal > 0:
            randomX = random.randint(0, 8)
            randomY = random.randint(0, 8)
            self.board[randomX][randomY] = 0
            purgeTotal = purgeTotal - 1

        return self.board
