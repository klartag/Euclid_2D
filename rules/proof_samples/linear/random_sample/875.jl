Assumptions:
A, B, C, D, E, F: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == Line(C, A)
E == projection(C, i)
c == Circle(E, A, C)
F in g, c
k == Line(F, E)
l == Line(B, D)

Need to prove:
concurrent(j, k, l)

Proof:
