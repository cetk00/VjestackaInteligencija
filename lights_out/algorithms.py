from collections import deque

def bfs(problem):
    parent = {problem.start: None}      
    q = deque([problem.start])

    while q:
        state = q.popleft()

        if problem.is_goal(state):
            return recon_path(parent, state)

        for action in problem.get_actions(state):
            succ = problem.get_successor(state, action)
            if succ not in parent:
                parent[succ] = (state, action)
                q.append(succ)

    return None


def recon_path(parent, state):
    path = []
    while parent[state] is not None:
        state, action = parent[state]
        path.append(action)
    return path[::-1]