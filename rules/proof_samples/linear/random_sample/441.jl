Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
distinct(c, d, e)
f == Line(B, C)
g == Line(C, A)
c == Circle(C, A, B)
D == center(c)
d == Circle(B, C, D)
e == Circle(D, C, A)
E in g, d
h == internal_angle_bisector(B, C, E)
F in f, e
i == parallel_line(D, h)
j == external_angle_bisector(A, D, C)
k == parallel_line(F, j)
G == line_intersection(h, k)
H == line_intersection(f, i)

Need to prove:
collinear(G, H, E)

Proof:
