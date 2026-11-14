class LightsOut:

    def __init__(self, start, m, n):
        self.start = start
        self.target = tuple((-1,) * n for _ in range(m))
        self.m = m
        self.n = n

    def get_actions(self, curr_state):
        return [(i, j) for i in range(self.m) for j in range(self.n)]

    def get_successor(self, curr_state, curr_action):
        i, j = curr_action
        s = [list(row) for row in curr_state]
        for di, dj in ((0,0), (1,0), (-1,0), (0,1), (0,-1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < self.m and 0 <= nj < self.n:
                s[ni][nj] *= -1
        return tuple(tuple(row) for row in s)

    def is_goal(self, curr_state):
        return curr_state == self.target