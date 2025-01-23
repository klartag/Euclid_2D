Assumptions:
A, B, C, D, E, F, G, H, I: Point
f: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
f == Line(B, A)
D == midpoint(B, A)
E == midpoint(C, A)
F == midpoint(B, C)
c == Circle(E, F, D)
G in f, c
H == midpoint(C, G)
I == projection(F, f)

Need to prove:
concyclic(F, G, H, I)

Proof:
