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
    all_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    
    if len(horizontal) != 9:
        raise ValueError("Invalid sudoku puzzle")

    for row in horizontal:
        if len(row) != 9:
            raise ValueError("Invalid sudoku puzzle")

    for row in horizontal:
        seen = set()
        for val in row:
            if val != 0:
                if val not in all_nums:
                    raise ValueError("Invalid sudoku puzzle")
                if val in seen:
                    raise ValueError("Invalid sudoku puzzle")
                seen.add(val)

    solution = None
    stack = []
    solved_count = 0
    solvable = True
    while True:
        if solved_count == 2: raise ValueError("Invalid sudoku puzzle")
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

        if (best_cell is None) or (not best_cell[2]):
            if best_cell is None:
                solved_count += 1
                solution = [row[:] for row in horizontal]

            while stack:
                x, y, candidates = stack[-1]
                horizontal[x][y] = 0
                if not candidates:
                    stack.pop()
                else:
                    horizontal[x][y] = candidates.pop()
                    break
            if not stack:
                solvable = False
            continue
            
        if not solvable:
            break

        x,y,nums = best_cell
        horizontal[x][y] = best_cell[2].pop()
        stack.append(best_cell)
        
    if solution and (solved_count==1): return solution
    else: raise ValueError("Invalid sudoku puzzle")