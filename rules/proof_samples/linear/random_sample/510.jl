Assumptions:
A, B, C, D, E, F: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h)
f == Line(B, C)
D == midpoint(B, A)
g == parallel_line(D, f)
E in g
h == Line(E, C)
c == Circle(A, E, D)
F in h, c

Need to prove:
concyclic(A, B, C, F)

Proof:
