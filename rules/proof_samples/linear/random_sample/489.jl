Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == projection(A, h)
j == Line(E, A)
F == center(c)
k == parallel_line(F, g)
G == line_intersection(k, j)
H == line_intersection(g, i)

Need to prove:
concyclic(C, F, G, H)

Proof:
