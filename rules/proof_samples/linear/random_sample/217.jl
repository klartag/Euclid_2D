Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E == projection(D, g)
F == projection(D, f)
j == Line(E, F)
k == parallel_line(A, j)
c == Circle(A, B, D)
G in k, c

Need to prove:
collinear(G, C, D)

Proof:
