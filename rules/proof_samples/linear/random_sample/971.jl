Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(A, B, D)
E == midpoint(B, D)
F in h, c
G == center(c)
j == Line(C, A)
d == Circle(E, G, B)
H in j, d

Need to prove:
concyclic(A, F, G, H)

Proof:
