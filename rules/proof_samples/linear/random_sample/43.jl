Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == external_angle_bisector(A, C, B)
E == center(c)
F in i, c
j == Line(E, F)
G == line_intersection(g, j)

Need to prove:
collinear(G, D, A)

Proof:
