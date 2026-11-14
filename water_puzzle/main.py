from algorithms import bfs
from water_pouring import WaterPouring

wp = WaterPouring((8, 5, 3), (8, 0, 0), (4, 4, 0))

print(bfs(wp))