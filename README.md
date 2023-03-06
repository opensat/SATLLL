<h1 align="center">SATLLL</h1>

<h2 align="center">What is SATLLL</h2>

A Python tool that implements Lovasz Local Lemma's application on The Boolean Satisfiability (SAT) problem, which includes:
- an **instance geneartor** which generate instance in the local lemma regime (which will be satisfiable)
- an **algorithm (decision procedure)** which solves a decision problem that if a SAT instance is in the local lemma regime
- a **solver** for the instances in the local lemma regime, which contains two part:
  - the algorithmic LLL, which provides efficient algorithm to **search** a solution
  - the partial rejrection sampling, which **samples** a uniform random solution from all solutions

<h2 align="center">Installation</h2>

Install SATLLL by using `pip`，which requires **Python >= 3.5** :
```bash
pip install satlll 
```

<h2 align="center">Demo</h2>

```Python
import time

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
    satisfiable = lll_decision(sat_instance, n)
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
```