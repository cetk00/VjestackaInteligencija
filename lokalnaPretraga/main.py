from nqueens import NQueens
from algorithms import hillClimbing, simulatedAnnealing

nq = NQueens(8)
#print(nq.start)
#actions = nq.getActions(nq.start)
#print(actions)
#print(nq.getSuccessor(nq.start, actions[0]))
#print(nq.score(nq.start))

state = simulatedAnnealing(nq) #hillClimbing(nq)
print(nq.score(state))
nq.printState(state)