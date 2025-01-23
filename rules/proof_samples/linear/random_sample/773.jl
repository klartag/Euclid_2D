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
E == midpoint(D, C)
c == Circle(C, B, E)
d == Circle(D, E, B)
F in i, d
j == Line(C, A)
G == center(d)
H in j, c

Need to prove:
concyclic(E, F, G, H)

Proof:
