import time

import numpy as np
from pysat.formula import CNF
from pysat.solvers import Solver
from pylll.generator import lll_generator
from pylll.decision import lll_decision
from pylll.solver import lll_solver


def read_sat(sat_path):
    with open(sat_path) as f:
        sat_lines = f.readlines()
        header = sat_lines[0]
        header_info = header.replace("\n", "").split(" ")
        num_vars = int(header_info[-2])
        num_clauses = int(header_info[-1])

        sat = [
            [int(x) for x in line.replace(" 0\n", "").split(" ")]
            for line in sat_lines[1:]
        ]

        return sat, num_vars, num_clauses


if __name__ == "__main__":
    # generator
    n = 100  # variable numbers
    sat_instance = lll_generator(n, 8)
    print(f"the size of SAT: {len(sat_instance)}")

    print("----------")

    # decision algorithm
    satisfiable = lll_decision(sat_instance, n, 100)
    print(f"LLL satisfiable: {satisfiable}")

    print("----------")

    # lll solver
    start_time = time.time()
    model = lll_solver(sat_instance, n)
    if model:
        print(f"The SAT instance can be solved by algorithm LLL")
    print(f"solver time: {time.time() - start_time:.4f}")
    print("----------")

    # modern solver
    cnf = CNF(from_clauses=sat_instance)
    start_time = time.time()
    with Solver(bootstrap_with=cnf) as solver:
        print(f"The SAT instance can be solved: {solver.solve()}")
    print(f"solver time: {time.time() - start_time:.4f}")
