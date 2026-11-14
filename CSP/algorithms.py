def cspBasic(problem, assignment):
    if problem.isComplete(assignment):
        return True

    #izbor promjenljive
    X = assignment.index(None)
    #provjera domena
    D = set(range(problem.n))

    for v in D:
        assignment[X] = v
        if problem.isValid(assignment):
            success = cspBasic(problem, assignment)
            if success:
                return True
        assignment[X] = None

    return False

def cspForwardCheck(problem, assignment, domains):
    if problem.isComplete(assignment):
        return True

    X = assignment.index(None)
    D = set(range(problem.n))

    for v in D:
        assignment[X] = v
        newDomains = problem.forwardCheck(assignment, domains, X, v)

        if all([len(newDomains[Y]) > 0 for Y in range(problem.n) if assignment[Y] is None]):
            success = cspForwardCheck(problem, assignment, newDomains)
            if success:
                return True
        assignment[X] = None

    return False

#minimum remaining values heuristika

def cspForwardCheckMRV(problem, assignment, domains):
    if problem.isComplete(assignment):
        return True

    minLen = problem.n + 1
    D = {}
    X = None
    for Y, E in enumerate(domains):
        if assignment[Y] is None and len(E) < minLen:
            minLen = len(E)
            X = Y
            D = E

    for v in D:
        assignment[X] = v
        newDomains = problem.forwardCheck(assignment, domains, X, v)

        if all([len(newDomains[Y]) > 0 for Y in range(problem.n) if assignment[Y] is None]):
            success = cspForwardCheckMRV(problem, assignment, newDomains)
            if success:
                return True

        assignment[X] = None

    return False

