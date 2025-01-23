Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(C, A, B)
j == Line(C, A)
k == parallel_line(B, j)
E in k, c
d == Circle(B, E, D)
F == center(c)
G == projection(F, j)
H in i, d

Need to prove:
concyclic(A, E, G, H)

Proof:
