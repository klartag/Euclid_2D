Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(F, C)
c == Circle(F, D, B)
G in h, c

Need to prove:
concyclic(A, E, F, G)

Proof:
