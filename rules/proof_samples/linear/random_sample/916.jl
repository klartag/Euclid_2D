Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E == projection(D, f)
F == projection(D, g)
k == parallel_line(A, f)
c == Circle(F, A, D)
G in k, c
H in j, c
d == Circle(G, H, E)
I in j, d

Need to prove:
collinear(G, F, I)

Proof:
