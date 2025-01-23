Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
j == external_angle_bisector(B, C, D)
E == line_intersection(i, j)
d == Circle(E, D, C)
k == internal_angle_bisector(C, D, A)
F in k, d
G in g, d
H == center(d)

Need to prove:
collinear(G, F, H)

Proof:
