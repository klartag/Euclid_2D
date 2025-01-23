Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == midpoint(D, C)
F == midpoint(D, E)
F in j # (defining j)
G == line_intersection(g, i)
H == projection(D, j)
k == Line(H, D)
d == Circle(H, E, F)
I in k, d
l == internal_angle_bisector(H, I, C)

Need to prove:
G in l

Proof:
