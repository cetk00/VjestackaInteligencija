class SlidingPuzzle3x3:
    
    def __init__(self, start, target):
        self.start = start
        self.target = target
    
    def find_blank(self, curr_state):
        return 45 - sum(curr_state) # self.n * (self.n + 1) // 2
    
    def get_actions(self, curr_state):
        actions = []
        pos_blank = self.find_blank(curr_state)
        if pos_blank % 3 != 0:
            actions.append('L')
        if pos_blank % 3 != 1:
            actions.append('R')
        if pos_blank < 7:
            actions.append('U')
        if pos_blank > 3:
            actions.append('D')
        return actions
    
    def get_successor(self, curr_state, curr_action):
        pos_blank = self.find_blank(curr_state)
        pos_piece = -1
        if curr_action == 'U':
            pos_piece = pos_blank + 3
        elif curr_action == 'D':
            pos_piece = pos_blank - 3
        elif curr_action == 'L':
            pos_piece = pos_blank + 1
        else:
            pos_piece = pos_blank - 1
        idx_piece = curr_state.index(pos_piece)
        new_state = curr_state[:idx_piece] + (pos_blank,) + curr_state[idx_piece+1:]
        return new_state
    
    def is_goal(self, curr_state):
        return curr_state == self.target
    
    def h(self, curr_state):
        cnt = 0
        for p1, p2 in zip(curr_state, self.target):
            if p1 != p2:
                cnt += 1
        return cnt
    

# za vjezbu: generalizacija n x n

