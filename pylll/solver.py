# A solver based on Algorithmic Lovász local lemma: https://en.wikipedia.org/wiki/Algorithmic_Lov%C3%A1sz_local_lemma
# and 
import random
from pylll.decision import lll_decision

def is_satisfied(clause, assignment):
    for literal in clause:
        if literal * assignment[abs(literal) - 1] > 0:
            return True
    return False


# http://tcs.nju.edu.cn/slides/random2015/LLL.pdf


def boundary(R, dependency):
    boundary = set()
    for idx in R:
        neighbors = dependency[idx]
        for neighbor in neighbors:
            if neighbor not in R:
                boundary.add(neighbor)
    return boundary

def vars_related(event_idx, S_idx, instance):
    vars_event = set([abs(x) for x in instance[event_idx]])
    vars_S = set([abs(x) for idx in S_idx for x in instance[idx]])
    if vars_event.intersection(vars_S):
        return True
    else:
        return False



def lll_solver(instance, n, sample=False):
    if not sample:
        if lll_decision(instance, n):
                assignment = [1 if random.random() > 0.5 else -1 for x in range(1, n + 1)]
                solved = False
                while not solved:
                    solved = True
                    for clause in instance:
                        if is_satisfied(clause, assignment):
                            pass
                        else:
                            solved = False
                            literal = random.choice(clause)
                            assignment[abs(literal) - 1] = -assignment[abs(literal) - 1]
                            break
                return assignment
        else:
            return None
    else:
        satisfiable, dependency = lll_decision(instance, n, need_dependency=True)
        if satisfiable:
            assignment = [1 if random.random() > 0.5 else -1 for x in range(1, n + 1)]
            solved = False
            while not solved:
                solved = True
                R = set()
                # init resampled set
                for idx, clause in enumerate(instance) :
                    if is_satisfied(clause, assignment):
                        pass
                    else:
                        solved = False
                        R.add(idx)
                N = set()
                # update resampled set
                diff = boundary(R, dependency) - N
                while diff:
                    for event_idx in diff:
                        #
                        if vars_related(event_idx, R, instance):
                            R.add(event_idx)
                        else:
                            N.add(event_idx)
                    diff = boundary(R, dependency) - N
                # resampled all variables in R
                vars = set([abs(x) for idx in R for x in instance[idx]])
                # print(f'R: {R}')
                for var in vars:
                    var_idx = var - 1
                    assignment[var_idx] = assignment[var_idx] if random.random() > 0.5 else - assignment[var_idx]
            return assignment
        else:
            return None