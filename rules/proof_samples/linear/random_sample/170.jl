Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(A, B, D)
E == midpoint(C, A)
j == parallel_line(E, f)
F == midpoint(B, C)
d == Circle(F, D, E)
G in c, d
k == Line(A, G)

Need to prove:
concurrent(g, j, k)

Proof:
