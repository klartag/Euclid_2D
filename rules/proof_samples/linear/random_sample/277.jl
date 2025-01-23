Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(c, d, e)
A in c
B in c
C in c
D == midpoint(C, A)
E == midpoint(B, C)
F == midpoint(E, A)
G == midpoint(B, E)
d == Circle(E, G, F)
H == center(c)
e == Circle(G, D, C)
I in c, e
J in e, d

Need to prove:
concyclic(E, H, I, J)

Proof:
