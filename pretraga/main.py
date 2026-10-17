from sliding_puzzle import SlidingPuzzle3x3
from algorithms import dfs, bfs, ucs, a_star

sp = SlidingPuzzle3x3((4, 1, 2, 6, 9, 8, 7, 5), (1, 2, 3, 6, 9, 8, 7, 4))
# print(sp.start, sp.target)
# print(sp.get_actions(sp.start), sp.get_actions(sp.target))
# print(sp.get_successor(sp.start, 'U'), sp.get_successor(sp.start, 'R'))

print(dfs(sp))
print(bfs(sp))
print(ucs(sp))
print(a_star(sp))