Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == Line(B, D)
k == parallel_line(C, j)
E == projection(A, k)
c == Circle(E, A, B)
F == center(c)

Need to prove:
collinear(B, F, D)

Proof:
