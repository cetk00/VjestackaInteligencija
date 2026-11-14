from lights_out import LightsOut
from algorithms import bfs

start =(
    (-1, -1, -1, -1, 1),
    (-1, -1, -1, 1, 1),
    (-1, -1, 1, 1, 1),
    (-1, 1, -1, -1, 1),
    (-1, -1, 1, 1, -1)
)
lo = LightsOut(start, 5, 5)
print(bfs(lo))