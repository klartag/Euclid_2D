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
d == Circle(A, B, D)
E == projection(A, h)
j == Line(A, E)
k == Line(B, D)
F in j, d
G in h, c
H == line_intersection(j, k)

Need to prove:
concyclic(D, F, G, H)

Proof:
