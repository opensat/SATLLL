from random import sample

from pysat.formula import CNF
from pysat.solvers import Solver

def hyperedge_generator (n, m, k):  # n vertex, m edges, k-uniform hypergraph. The method may have repeated edges.
    edge_set = []
    vertex = [(i + 1) for i in range(n)]
    for i in range(m):
        edge_set.append(sample(vertex, k))
    return edge_set

def sat_build (edge_set, n, k):
    sat = []
    var_num = 1  # t variables codes a vertex
    while (1 << var_num) < k: var_num += 1

    # Encode method
    # varible 1 .. var_num  -> vertex 1
    # ...
    # varible (n - 1) * var_num + 1 .. n * var_num -> vertex n
    # color of vertex 1 -> (var_num, ... , 1) in binary

    # eliminate illegal color
    for i in range(1, n + 1):
        for state in range(k, 1 << var_num):
            clause = []
            first_varible = (i - 1) * var_num + 1  # the first varible index of i-th vertex
            for j in range(0, var_num):
                if (state >> j) & 1:
                    clause.append(-(first_varible + j))
                else:
                    clause.append(first_varible + j)
            sat.append(clause)

    # for each edge, generate k clauses
    for edge in edge_set:
        for state in range(0, k):
            clause = []
            for i in edge:
                first_varible = (i - 1) * var_num + 1
                for j in range(0, var_num):
                    if (state >> j) & 1:
                        clause.append(-(first_varible + j))
                    else:
                        clause.append(first_varible + j)
            sat.append(clause)

    return sat, var_num

n = 100   # n vertices
k = 3     # k colors

edge_set = hyperedge_generator(n, 700, 3)
print("edge_set:")
print(edge_set)
print("-------")

# edge_set = [[1, 2, 3], [1, 3, 4], [3, 4, 5], [2, 5], [4, 5], [3, 5], [1, 5]]

sat_instance, var_num = sat_build(edge_set, n, k);
print("sat_build:")
print(sat_instance)
print("-------")
# print(sat)

answer = []
cnf = CNF(from_clauses=sat_instance)
with Solver(bootstrap_with=cnf) as solver:
    print(f'The SAT instance can be solved: {solver.solve()}')
    answer = solver.get_model()
    print(answer)

for i in range(1, n + 1):
    color = 0
    for j in range(0, var_num):
        result = answer[(i - 1) * var_num + j]
        if result > 0:
            color += 1 << j
    print("%d-th vertex is %d-th color" % (i, color))

