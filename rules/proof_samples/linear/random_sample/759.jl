Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
f == Line(C, A)
g == parallel_line(B, f)
c == Circle(C, A, B)
D in g, c
E == midpoint(D, C)
h == Line(B, E)
F in h, c
G == midpoint(D, A)

Need to prove:
concyclic(A, E, F, G)

Proof:
