Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(D, C, A)
E in g, c
j == Line(E, A)
F == midpoint(D, C)
G == projection(A, g)
k == Line(D, G)
l == Line(B, F)

Need to prove:
concurrent(j, k, l)

Proof:
