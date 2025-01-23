Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == Line(C, A)
c == Circle(C, D, B)
k == Line(B, D)
E == midpoint(A, D)
F == line_intersection(j, k)
G == center(c)
l == parallel_line(E, j)
H == line_intersection(h, l)

Need to prove:
concyclic(D, F, G, H)

Proof:
