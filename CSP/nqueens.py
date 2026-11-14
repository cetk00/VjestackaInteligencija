from copy import deepcopy
class NQueens:

    def __init__(self, n):
        self.n = n

    def isComplete(self, assignment):
        return None not in assignment

    def isValid(self, assignment):
        for X, u in enumerate(assignment):
            for Y, v in enumerate(assignment):
                if X != Y and u is not None and v is not None:
                    if u == v or abs(X - Y) == abs(u - v):
                        return False
        return True

    def forwardCheck(self, assignment, domains, X, u):
        newDomains = deepcopy(domains)
        for Y, v in enumerate(assignment):
            if v is None:
                newDomains[Y].discard(u)
                newDomains[Y].discard(u + abs(X - Y))
                newDomains[Y].discard(u - abs(X - Y))
        return newDomains