from sudoku import Sudoku
from algorithms import cspBasic, cspForwardCheck, cspForwardCheckMRV

sudoku = Sudoku(9)

assignment = [4, 0, 0, 0, 0, 0, 8, 0, 5,
    0, 3, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 7, 0, 0, 0, 0, 0,
    0, 2, 0, 0, 0, 0, 0, 6, 0,
    0, 0, 0, 0, 8, 0, 4, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 6, 0, 3, 0, 7, 0,
    5, 0, 0, 2, 0, 0, 0, 0, 0,
    1, 0, 4, 0, 0, 0, 0, 0, 0]

def init_domains(problem, assignment):
    domains = [set(range(1, problem.n + 1)) if assignment[i] == 0 else set() for i in range(len(assignment))]
    for i, v in enumerate(assignment):
        if v != 0:
            for Y in problem.susjedi(i):
                domains[Y].discard(v)
    return domains

domains = init_domains(sudoku, assignment)
print(domains)
# print(domains[1])
# print(cspForwardCheck(sudoku, assignment, domains))
cspForwardCheckMRV(sudoku, assignment, domains)

for i in range(81):
    if i % 9 == 0:
        print()
    print(assignment[i], end=' ')



