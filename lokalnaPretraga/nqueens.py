import random


class NQueens:

    def __init__(self, n):
        self.n = n
        self.start = [random.randint(0, n-1) for i in range(n)]

    def getActions(self, currState):
        actions = []
        for i in range(self.n):
            actions += [(i,j) for j in set(range(self.n)) - {currState[i]}]
        return actions

    def getSuccessor(self, currState, currActions):
        succState = [x for x in currState]
        i, j = currActions
        succState[i] = j
        return succState

    def score(self, currState):
        cnt = 0
        for j1, i1 in enumerate(currState[:-1]):
            for j2, i2 in enumerate(currState[j1+1:], start= j1+1):
                if i1 != i2 and abs(i1 - i2) != abs(j1 - j2):
                    cnt += 1
        return cnt

    def printState(self, currState):
        for i in range(self.n):
            for j in range(self.n):
                if currState[j] == i:
                    print('Q', end= ' ')
                else:
                    print('.', end= ' ')
            print()
