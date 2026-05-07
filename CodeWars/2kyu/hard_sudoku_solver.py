
#TODO

"""
There are several difficulty of sudoku games, we can estimate the difficulty of a sudoku game based on how many cells are given of the 81 cells of the game.

Easy sudoku generally have over 32 givens
Medium sudoku have around 30–32 givens
Hard sudoku have around 28–30 givens
Very Hard sudoku have less than 28 givens
Note: The minimum of givens required to create a unique (with no multiple solutions) sudoku game is 17.

A hard sudoku game means that at start no cell will have a single candidates and thus require guessing and trial and error. A very hard will have several layers of multiple candidates for any empty cell.

Task:
Write a function that solves sudoku puzzles of any difficulty. The function will take a sudoku grid and it should return a 9x9 array with the proper answer for the puzzle.

Or it should raise an error in cases of: invalid grid (not 9x9, cell with values not in the range 1~9); multiple solutions for the same puzzle or the puzzle is unsolvable
"""

from itertools import product as prd

def sudoku_solver(horizontal):
    stack = []
    all_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    solved_count = 0
    while True:
        best_cell = None
        min_candidates = 10
        for x, y in prd(range(9), range(9)):
            if horizontal[x][y] == 0:

                set_row = set(horizontal[x])
                set_col = set(horizontal[r][y] for r in range(9))
                r_start, c_start = (x // 3) * 3, (y // 3) * 3
                set_sqr = {horizontal[r][c] for r, c in prd(range(r_start, r_start + 3), range(c_start, c_start + 3))}

                current_nums = all_nums - set_row - set_col - set_sqr
                num_candidates = len(current_nums)
                
                if num_candidates == 0:
                    best_cell = (x, y, [])
                    break 
                
                if num_candidates < min_candidates:
                    min_candidates = num_candidates
                    best_cell = (x, y, list(current_nums))
                    
                if num_candidates == 1:
                    break

        if best_cell is None:
            solved_count += 1
            solution = [row[:] for row in horizontal]
            continue
        
        # 0 candidates handling
        
        # x>1 candidates handling
        
    return solution