Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == Line(B, A)
c == Circle(C, A, B)
D in f
g == Line(C, D)
E == midpoint(D, A)
F in g, c
G == midpoint(F, D)

Need to prove:
concyclic(B, C, E, G)

Proof:
