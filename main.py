import time

import numpy as np
from pysat.formula import CNF
from pysat.solvers import Solver

from satlll import lll_generator
from satlll import lll_decision
from satlll import lll_solver


if __name__ == "__main__":
    # generator
    n = 500  # variable numbers
    sat_instance = lll_generator(n, 5)
    print(f"the size of SAT: {len(sat_instance)}")
    print("----------")

    # decision algorithm
    start_time = time.time()
    satisfiable = lll_decision(sat_instance, n, eval_iter=10)
    print(f"LLL satisfiable: {satisfiable}")
    print(f"desision time: {time.time() - start_time:.4f}")
    print("----------")

    # lll solver (search)
    start_time = time.time()
    model = lll_solver(sat_instance, n)
    if model:
        print(f"The SAT instance can be solved by algorithmic LLL")
    print(f"solving time: {time.time() - start_time:.4f}")
    print("----------")

    # lll solver (sample)
    start_time = time.time()
    model = lll_solver(sat_instance, n, sample=True)
    if model:
        print(f"The SAT instance can be solved by partial rejection sampling")
    print(f"solving time: {time.time() - start_time:.4f}")
    print("----------")

    # modern solver
    cnf = CNF(from_clauses=sat_instance)
    start_time = time.time()
    with Solver(bootstrap_with=cnf) as solver:
        print(f"The SAT instance can be solved: {solver.solve()}")
    print(f"solving time: {time.time() - start_time:.4f}")
