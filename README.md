# Sudoku_py
Take notes of the sudoku solutions and also take a chance to practice python

## How to use 
For now only allow for the 9x9 sudoku.
Please copy your sudoku to input.csv file and **split each digit by ","**

```python
python main.py
```


## Flow
- Load input.csv from file and turn it to 2D array 
- Init a Sudoku class
- Invoke solveSudoku function with 2D array
- Caculate the running time

## Sudoku class
### Responsibility:
- Check if there is no dupulacation from 1 to 9 in each row
- Check if there is no dupulacation from 1 to 9 in each col
- Check if there is no dupulacation from 1 to 9 in each 3x3 square

## Reference
- https://www.youtube.com/watch?v=auK3PSZoidc
- https://leetcode.com/problems/sudoku-solver/discuss/15959/Accepted-Python-solution
- https://ithelp.ithome.com.tw/articles/10220639