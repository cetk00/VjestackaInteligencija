import random
import math

def hillClimbing(problem):
    currState = problem.start
    currScore = problem.score(currState)

    while True:
        bestScore = float('-inf')
        bestSucc = None

        for a in problem.getActions(currState):
            succState = problem.getSuccessor(currState, a)
            succScore = problem.score(succState)
            if bestScore < succScore:
                bestScore = succScore
                bestSucc = succState

        if currScore < bestScore:
            currState = bestSucc
            currScore = bestScore
        else:
            break

    return currState


def temperatura(t, a = 30, b = 0.005, limit = 1e-6):
    T = a*math.exp(-b*t)
    if T < limit:
        return 0
    else:
        return T

def simulatedAnnealing(problem):
    currState = problem.start

    t = 0
    while True:
        actions = problem.getActions(currState)
        successors = [problem.getSuccessor(currState, action) for action in actions]
        #treba birati slucajnog susjeda, a ne najboljeg
        #tako se bolje pokriva prostor pretrage i izvlaci iz lokalnih maksimuma
        succState = random.choice(successors)

        currScore = problem.score(currState)
        succScore = problem.score(succState)

        delta = succScore - currScore
        if delta > 0:
            currState = succState
        else:
            T = temperatura(t)
            if T == 0:
                break
            p = math.exp(delta/T)
            if random.uniform(0, 1) <= p:
                currState = succState

        t += 1

    return currState
    
    
