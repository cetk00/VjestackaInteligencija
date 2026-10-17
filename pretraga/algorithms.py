from node import Node
from queue import Queue, PriorityQueue


def dfs(problem):
    
    s = [Node(problem.start)]
    visited = set([problem.start])
    
    while len(s) > 0:
        
        curr_node = s[-1]
        s.pop()
        
        if problem.is_goal(curr_node.curr_state):
            return curr_node.recon_path()
        
        for succ_node in curr_node.expand(problem):
            if succ_node.curr_state not in visited:
                s.append(succ_node)
                visited.add(succ_node.curr_state)
    
    return None


def bfs(problem):
    
    q = Queue()
    q.put(Node(problem.start))
    visited = set([problem.start])
    
    while not q.empty():
        
        curr_node = q.get()
        
        if problem.is_goal(curr_node.curr_state):
            return curr_node.recon_path()
        
        for succ_node in curr_node.expand(problem):
            if succ_node.curr_state not in visited:
                q.put(succ_node)
                visited.add(succ_node.curr_state)
    
    return None


# uniform-cost search
def ucs(problem):
    
    q = PriorityQueue()
    q.put(Node(problem.start))
    visited = set([problem.start])
    
    while not q.empty():
        
        curr_node = q.get()
        
        if problem.is_goal(curr_node.curr_state):
            return curr_node.recon_path()
        
        for succ_node in curr_node.expand(problem):
            if succ_node.curr_state not in visited:
                q.put(succ_node)
                visited.add(succ_node.curr_state)
    
    return None


# A*
def a_star(problem):
    
    q = PriorityQueue()
    q.put((0+problem.h(problem.start), Node(problem.start)))
    visited = set([problem.start])
    
    while not q.empty():
        
        _, curr_node = q.get()
        
        if problem.is_goal(curr_node.curr_state):
            return curr_node.recon_path()
        
        for succ_node in curr_node.expand(problem):
            if succ_node.curr_state not in visited:
                q.put((succ_node.cost + problem.h(succ_node.curr_state), succ_node))
                visited.add(succ_node.curr_state)
    
    return None