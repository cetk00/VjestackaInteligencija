def cspBasic(problem, assignment):
    if problem.is_complete(assignment):
        return True

    #izbor promjenljive
    X = assignment.index(0)
    #provjera domena
    D = range(1, problem.n)

    for v in D:
        assignment[X] = v
        if problem.is_valid(assignment, X):
            success = cspBasic(problem, assignment)
            if success:
                return True
        assignment[X] = 0

    return False

def cspForwardCheck(problem, assignment, domains):
    if problem.is_complete(assignment):
        return True

    X = assignment.index(0)
    D = list(domains[X])

    for v in D:
        assignment[X] = v
        newDomains = problem.forwardCheck(assignment, domains, X, v)

        if all([len(newDomains[Y]) > 0 for Y in range(len(assignment)) if assignment[Y] == 0]):
            success = cspForwardCheck(problem, assignment, newDomains)
            if success:
                return True
        assignment[X] = 0

    return False

def cspForwardCheckMRV(problem, assignment, domains):
    if problem.is_complete(assignment):
        return True

    minLen = problem.n + 1
    D = {}
    X = None
    for Y, E in enumerate(domains):
        if assignment[Y] == 0 and len(E) < minLen:
            minLen = len(E)
            X = Y
            D = E

    for v in D:
        assignment[X] = v
        newDomains = problem.forwardCheck(assignment, domains, X, v)

        if all([len(newDomains[Y]) > 0 for Y in range(len(assignment)) if assignment[Y] == 0]):
            success = cspForwardCheckMRV(problem, assignment, newDomains)
            if success:
                return True

        assignment[X] = 0

    return False