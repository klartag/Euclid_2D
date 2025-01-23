Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
d == Circle(C, D, B)
E == line_intersection(g, i)
F == center(d)
G == midpoint(E, F)
j == parallel_line(F, g)
H == projection(C, j)
e == Circle(F, D, H)
k == external_angle_bisector(D, F, C)
I in k, e

Need to prove:
collinear(D, I, G)

Proof:
