Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(c, d)
c == Circle(C, A, B)
D == midpoint(C, A)
E == center(c)
F == midpoint(B, A)
d == Circle(A, E, D)
G == midpoint(E, F)
H == center(d)
I in d
J == midpoint(I, E)

Need to prove:
concyclic(E, G, H, J)

Proof:
