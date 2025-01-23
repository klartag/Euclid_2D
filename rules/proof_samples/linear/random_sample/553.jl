Assumptions:
A, B, C, D, E, F, G, H, I: Point
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
c == Circle(C, A, B)
D == center(c)
E == midpoint(D, A)
F == midpoint(C, A)
G == midpoint(E, A)
H == midpoint(F, C)
I == midpoint(C, E)

Need to prove:
concyclic(A, G, H, I)

Proof:
