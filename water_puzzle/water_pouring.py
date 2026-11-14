class WaterPouring:
    def __init__(self, cap, start, target, tap = True):
        self.cap = cap
        self.start = start
        self.target = target
        self.tap = tap
        self.n = len(cap)

    def get_actions(self, curr_state):
        actions = []
        #8 5 3
        for i in range(self.n):
            if self.tap:
                if curr_state[i] < self.cap[i]:
                    actions.append(('fill', i))
                if curr_state[i] > 0:
                    actions.append(('empty', i))
            for j in range(self.n):
                if i != j and curr_state[i] > 0 and curr_state[j] < self.cap[j]:
                    actions.append(('pour', i, j))
        return actions

    def get_successor(self, curr_state, curr_action):
        s = list(curr_state)
        kind = curr_action[0]
        if kind == 'fill':
            s[curr_action[1]] = self.cap[curr_action[1]]
        elif kind == 'empty':
            s[curr_action[1]] = 0
        else:
            i, j = curr_action[1], curr_action[2]
            amount = min(s[i], self.cap[j] - s[j])
            s[i] -= amount
            s[j] += amount
        return tuple(s)

    def is_goal(self, curr_state):
        return all(t is None or t == c for t, c in zip(self.target, curr_state))