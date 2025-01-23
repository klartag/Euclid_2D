Assumptions:
A, B, C, D, E, F, G, H, I: Point
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
A in c
B in c
C == center(c)
D == midpoint(C, A)
E == midpoint(B, C)
F == midpoint(B, E)
G == midpoint(A, D)
H == midpoint(F, D)
I == midpoint(E, G)

Need to prove:
concyclic(D, E, H, I)

Proof:
