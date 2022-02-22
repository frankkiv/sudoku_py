# python -m unittest sudoku_test.py

import unittest
from sudoku import Sudoku

class SudokuTest(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """

    sudoku = Sudoku()
    sudoku.board = [
        [9, 8, 4, 6, 7, 2, 5, 3, 1],
        [0, 0, 7, 0, 0, 0, 6, 4, 9],
        [6, 1, 3, 5, 4, 9, 0, 2, 0],
        [0, 6, 0, 9, 0, 8, 3, 7, 4],
        [0, 0, 9, 0, 6, 0, 1, 8, 5],
        [0, 0, 8, 0, 0, 0, 9, 6, 2],
        [0, 3, 2, 0, 0, 7, 4, 9, 6],
        [0, 4, 0, 3, 9, 0, 2, 1, 0],
        [0, 9, 0, 0, 0, 0, 0, 5, 3],
    ]

    def test_findUnassigned(self):
        # The first unassigned position should be (row: 1, col:0)
        position = self.sudoku.findUnassigned()
        self.assertEqual(position, (1,0))

    def test_checkRow(self):
        # 4 is already exist in row 0, should return False
        suoldBeFalse = self.sudoku.checkrow(0, 4)
        self.assertFalse((suoldBeFalse))

        # 4 is not exist in row 1, should return True
        suoldBeTrue = self.sudoku.checkrow(1, 5)
        self.assertTrue((suoldBeTrue))
    
    def test_checkCol(self):
        # 4 is already exist in col 1, should return False
        suoldBeFalse = self.sudoku.checkcol(1, 4)
        self.assertFalse((suoldBeFalse))

        # 4 is not exist in col 0, should return True
        suoldBeTrue = self.sudoku.checkcol(0, 5)
        self.assertTrue((suoldBeTrue))
    
    def test_checkSquare(self):
        # 4 is already exist in square (0,0) , should return False
        suoldBeFalse = self.sudoku.checksquare(0, 0, 4)
        self.assertFalse((suoldBeFalse))

        # 5 is not exist in square 0, should return True
        suoldBeTrue = self.sudoku.checksquare(0, 0, 5)
        self.assertTrue((suoldBeTrue))
    
    def test_isSafe(self):
        # 4 is not safe in position (row: 1, col:0), should return False
        suoldBeFalse = self.sudoku.isSafe(1, 0, 4)
        self.assertFalse((suoldBeFalse))

        # 2 is safe in position (row: 1, col:0), should return True
        suoldBeTrue = self.sudoku.isSafe(1, 0, 2)
        self.assertTrue((suoldBeTrue))

    def test_solve(self):
        # The result should match the sudoku board once invoke the solve method
        self.sudoku.solve()
        result = [[9, 8, 4, 6, 7, 2, 5, 3, 1],
                [2, 5, 7, 8, 3, 1, 6, 4, 9],
                [6, 1, 3, 5, 4, 9, 8, 2, 7],
                [5, 6, 1, 9, 2, 8, 3, 7, 4],
                [4, 2, 9, 7, 6, 3, 1, 8, 5],
                [3, 7, 8, 4, 1, 5, 9, 6, 2],
                [8, 3, 2, 1, 5, 7, 4, 9, 6],
                [7, 4, 5, 3, 9, 6, 2, 1, 8],
                [1, 9, 6, 2, 8, 4, 7, 5, 3]]
        self.assertEqual(self.sudoku.board, result)


    

    


if __name__ == "__main__":
    # begin the unittest.main()
    unittest.main()
