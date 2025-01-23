Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == midpoint(B, A)
F == projection(C, f)
i == Line(F, C)
j == parallel_line(E, i)
G == line_intersection(j, h)

Need to prove:
collinear(C, G, B)

Proof:
