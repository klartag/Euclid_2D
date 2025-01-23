Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
E == midpoint(B, A)
i == external_angle_bisector(D, C, E)
j == external_angle_bisector(C, D, E)
F == line_intersection(i, j)
G == midpoint(F, E)
k == Line(F, E)
H == projection(D, k)
I == line_intersection(g, k)
d == Circle(H, G, C)
J in c, d

Need to prove:
concyclic(A, G, I, J)

Proof:
