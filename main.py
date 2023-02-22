import time

import numpy as np
from pysat.formula import CNF
from pysat.solvers import Solver

from pylll import lll_generator
from pylll import lll_decision
from pylll import lll_solver


if __name__ == "__main__":
    # generator
    n = 100  # variable numbers
    sat_instance = lll_generator(n, 8)
    print(f"the size of SAT: {len(sat_instance)}")

    print("----------")

    # decision algorithm
    satisfiable = lll_decision(sat_instance, n)
    print(f"LLL satisfiable: {satisfiable}")

    print("----------")

    # lll solver
    start_time = time.time()
    model = lll_solver(sat_instance, n)
    if model:
        print(f"The SAT instance can be solved by algorithm LLL")
    print(f"solving time: {time.time() - start_time:.4f}")
    print("----------")

    # modern solver
    cnf = CNF(from_clauses=sat_instance)
    start_time = time.time()
    with Solver(bootstrap_with=cnf) as solver:
        print(f"The SAT instance can be solved: {solver.solve()}")
    print(f"solving time: {time.time() - start_time:.4f}")
