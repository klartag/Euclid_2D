Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
d == Circle(B, C, D)
E == center(c)
h == internal_angle_bisector(A, E, B)
F in h
i == Line(D, F)
G in i, d

Need to prove:
concyclic(C, E, F, G)

Proof:
