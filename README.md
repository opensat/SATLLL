# PyLLL

A Python tool that implements Lovasz Local Lemma's application on The Boolean Satisfiability (SAT) problem, which includes:
- an instance geneartor under LLL constrain
- an algorithm which solving a decision problem that if a SAT instance in the  LLL condition
- a solver for the instances in the local lemma regime, which contains two part:
  - the algorithmic LLL, which provides efficient algorithm to find a solution
  - the partial rejrection sampling, which samples a uniform random solution from all solutions