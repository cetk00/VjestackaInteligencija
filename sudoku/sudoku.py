from copy import deepcopy
class Sudoku:

    def __init__(self, start, n):
        self.start = start
        self.n = n
        self.box = int(n ** 0.5)

    def isComplete(self, assignment):
        return all(0 not in red for red in assignment)

    def u_istom_redu(self, assignment):
        for k in range(self.n):
            vrijednosti = [v for v in assignment[k] if v != 0]
            if len(vrijednosti) != len(set(vrijednosti)):
                return False
        return True

    def u_istoj_koloni(self, assignment):
        for k in range(self.n):
            vrijednosti = [assignment[i][k] for i in range(self.n) if assignment[i][k] != 0]
            if len(vrijednosti) != len(set(vrijednosti)):
                return False
        return True

    def u_istoj_kutiji(self, assignment):
        for i in range(0, self.n, self.box):
            for j in range(0, self.n, self.box):
                vrijednosti = [assignment[x][y] for x in range(i, i + self.box) for y in range(j, j + self.box) 
                                if assignment[x][y] != 0]
                if len(vrijednosti) != len(set(vrijednosti)):
                    return False
        return True

    def is_valid(self, assignment):
        return (self.u_istom_redu(assignment) and self.u_istoj_koloni(assignment) and self.u_istoj_kutiji(assignment))

    def get_actions(self, assignment):
        for i in range(self.n):
            for j in range(self.n):
                if assignment[i][j] == 0:
                    return [(i, j, v) for v in range(1, self.n + 1)]
        return []

    def get_successors(self, assignment, action):
        i, j, v = action
        new_domain = deepcopy(assignment)
        new_domain[i][j] = v
        return new_domain

    def solve(self, assignment = None):
        if assignment is None:
            assignment = self.start
        if self.isComplete(assignment):
            return assignment
        for action in self.get_actions(assignment):
            nova = self.get_successors(assignment, action)
            if self.is_valid(nova):
                rezultat = self.solve(nova)
                if rezultat is not None:
                    return rezultat
        return None