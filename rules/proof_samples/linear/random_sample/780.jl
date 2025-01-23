Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == midpoint(B, A)
d == Circle(C, B, E)
e == Circle(E, D, A)
F in d, e
G == projection(F, h)

Need to prove:
concyclic(C, D, E, G)

Proof:
