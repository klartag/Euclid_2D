Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
j == internal_angle_bisector(D, E, C)
F == center(c)
F in k # (defining k)
G == line_intersection(k, j)

Need to prove:
collinear(G, C, F)

Proof:
