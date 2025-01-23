Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(C, A)
c == Circle(C, D, B)
F in i, c
F in j # (defining j)
G in j, c
k == parallel_line(E, g)
H == line_intersection(k, j)

Need to prove:
concyclic(B, E, G, H)

Proof:
