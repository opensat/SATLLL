import random
from random import sample

# A random satisfiable k-sat instance generator based on lovasz local lemma.
# Noticed that the constrian is different with the original version and based on Theorem 1.3 in paper
# "Disproof of the neighborhood conjecture with implications to SAT"


def lll_generator(n, k):
    if n < k:
        print("n must be greater or equal to k for k-sat problem")
        return []

    d = int(2**k / (2.71829 * k))
    instance = []
    vars_quota = [d] * n

    valid_vars = [i for i in range(n) if vars_quota[i] > 0]
    while len(valid_vars) >= k:
        clause = sample(valid_vars, k)
        for x in clause:
            vars_quota[x] -= 1
        valid_vars = [i for i in range(n) if vars_quota[i] > 0]
        clause = [x + 1 for x in clause]
        clause = [x if random.random() > 0.5 else -x for x in clause]

        instance.append(clause)

    return instance
