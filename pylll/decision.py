from functools import reduce
import operator


def lll_decision(instance, n, eval_iter=20, need_dependency=False):
    """n: the variable numbers"""
    num_clauses = len(instance)
    # initial the probability for each clause (event)
    event_prob = [2 ** (-len(clause)) for clause in instance]
    # dependency analysis
    occurence = [[] for i in range(n + 1)]  # j in occurence[i] means varible x_i is in j-th clauses
    dependency = [[] for i in range(num_clauses)]
    for i in range(num_clauses):
        clause_len = len(instance[i])
        for j in range(clause_len):
            occurence[abs(instance[i][j])].append(i)

    for i in range(1, n + 1):
        len_i = len(occurence[i])
        if len_i <= 1:
            continue
        for j in range(len_i):
            for l in range(j + 1, len_i):
                dependency[occurence[i][j]].append(occurence[i][l])
                dependency[occurence[i][l]].append(occurence[i][j])

    for i in range(num_clauses):
        dependency[i] = set(dependency[i])
    
    satisfiable = True
    # initial alphas
    alphas = [x for x in event_prob]
    # constraint propagation
    for _ in range(eval_iter):
        if max(alphas) > 1:
            satisfiable = False
            break
        update_alphas = [
            event_prob[i] / reduce(operator.mul, [1 - alphas[j] for j in dependency[i]]) if dependency[i] else event_prob[i] for i in range(num_clauses) 
        ]
        alphas = update_alphas

    if need_dependency:
        return satisfiable, dependency
    else:
        return satisfiable
