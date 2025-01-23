Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d)
A in c
B in c
C in c
f == Line(C, A)
D == midpoint(C, A)
E == projection(B, f)
g == Line(E, B)
F == midpoint(E, B)
G == midpoint(F, E)
H in g, c
d == Circle(F, A, C)
I == center(d)

Need to prove:
concyclic(D, G, H, I)

Proof:
