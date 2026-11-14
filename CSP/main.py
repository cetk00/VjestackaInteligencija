from nqueens import NQueens
from algorithms import cspBasic, cspForwardCheckMRV, cspForwardCheck
import time

n = 8
nq = NQueens(n)
assignment = [None for _ in range(n)]
domains = [set(range(n)) for _ in range(n)]

# t0 = time.perf_counter()
# cspBasic(nq, assignment)
# t1 = time.perf_counter()
# print(t1 - t0)
# print(assignment)

# t0 = time.perf_counter()
# cspForwardCheck(nq, assignment, domains)
# t1 = time.perf_counter()
# print(t1 - t0)
# print(assignment)

t0 = time.perf_counter()
cspForwardCheckMRV(nq, assignment, domains)
t1 = time.perf_counter()
print(t1 - t0)
print(assignment)
# assignment[0] = 1
# print(nq.forward_check(assignment, domains, 0, 1))