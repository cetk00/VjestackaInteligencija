from sudoku import Sudoku
import time
puzzle = [
    [4, 0, 0, 0, 0, 0, 8, 0, 5],
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 8, 0, 4, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 3, 0, 7, 0],
    [5, 0, 0, 2, 0, 0, 0, 0, 0],
    [1, 0, 4, 0, 0, 0, 0, 0, 0]
]
problem = Sudoku(puzzle, 9)
t0 = time.perf_counter()
rez = problem.solve()
t1 = time.perf_counter()

def printGrid(grid):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("------+-------+------")
        red = ""
        for c in range(9):
            if c % 3 == 0 and c != 0:
                red += "| "
            red += str(grid[r][c]) + " "
        print(red)

if rez is not None:
    printGrid(rez)

print(t1-t0)

