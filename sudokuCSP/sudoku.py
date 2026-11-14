from copy import deepcopy

class Sudoku:
    def __init__(self, n):
        self.n = n

    def is_complete(self, assignment):
        return 0 not in assignment

    def u_istom_redu(self, assignment, r):
        vrijednosti = [v for v in assignment[self.n * r : (r + 1) * self.n] if v != 0]
        return len(vrijednosti) != len(set(vrijednosti))

    def u_istoj_koloni(self, assignment, r):
        vrijednosti = [v for v in assignment[r : : 9] if v != 0]
        return len(vrijednosti) != len(set(vrijednosti))

    def u_istoj_kutiji(self, assignment, r):
        red = r // self.n
        kolona = r % self.n
        pocetak_reda = (red // 3) * 3
        pocetak_kolone = (kolona // 3) * 3

        vrijednosti = []
        for i in range(pocetak_reda, pocetak_reda + 3):
            for j in range(pocetak_kolone, pocetak_kolone + 3):
                v = assignment[i * self.n + j]
                if v != 0:
                    vrijednosti.append(v)

        return len(vrijednosti) != len(set(vrijednosti))

    def is_valid(self, assignment, r):
        return not(self.u_istoj_koloni(assignment, r) or self.u_istoj_kutiji(assignment, r) or self.u_istom_redu(assignment, r))

    def susjedi(self, X):
        red, kolona = divmod(X, self.n)
        pocetak_reda = (red // 3) * 3
        pocetak_kolone = (kolona // 3) * 3

        s = set()
        for j in range(self.n):
            s.add(red * self.n + j)
            s.add(kolona + j * self.n)
        for i in range(pocetak_reda, pocetak_reda + 3):
            for j in range(pocetak_kolone, pocetak_kolone + 3):
                s.add(i*self.n + j)
        s.discard(X)
        return s

    def forwardCheck(self, assignment, domains, X, u):
        newDomains = deepcopy(domains)
        for Y in self.susjedi(X):
            if assignment[Y] == 0:
                newDomains[Y].discard(u)
        return newDomains