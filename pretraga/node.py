class Node:
    
    def __init__(self, curr_state, prev_action=None, parent=None, cost=0):
        self.curr_state = curr_state
        self.prev_action = prev_action
        self.parent = parent
        self.cost = cost
    
    def expand(self, problem):
        actions = problem.get_actions(self.curr_state)
        return [Node(problem.get_successor(self.curr_state, a), a, self, self.cost + 1) for a in actions]
    
    def recon_path(self):
        actions = []
        curr_node = self
        while curr_node.parent is not None:
            actions.append(curr_node.prev_action)
            curr_node = curr_node.parent
        return actions[::-1]
    
    def __lt__(self, other_node):
        return self.cost < other_node.cost