Assumptions:
A, B, C, D, E, F: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h)
distinct(c, d)
A in c
B in c
C in c
f == Line(C, A)
g == parallel_line(B, f)
D in g, c
E == center(c)
d == Circle(E, D, A)
h == Line(C, D)
F in h, d

Need to prove:
concyclic(B, C, E, F)

Proof:
