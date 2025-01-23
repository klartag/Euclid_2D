Assumptions:
A, B, C, D, E, F: Point
f: Line
c: Circle
distinct(A, B, C, D, E, F)
A in c
B in c
C == center(c)
D == midpoint(A, B)
E == midpoint(A, D)
E in f # (defining f)
F == projection(C, f)

Need to prove:
concyclic(C, D, E, F)

Proof:
