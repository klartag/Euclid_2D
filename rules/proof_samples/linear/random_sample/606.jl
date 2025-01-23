Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(D, C, A)
j == internal_angle_bisector(A, C, B)
d == Circle(C, A, B)
E == projection(B, j)
k == Line(B, E)
l == parallel_line(D, j)
F in j, d
G in l, c
H in k, d

Need to prove:
collinear(G, H, F)

Proof:
