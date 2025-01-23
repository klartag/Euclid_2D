Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
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
c == Circle(C, A, B)
d == Circle(F, A, D)
k == external_angle_bisector(D, F, A)
G in c, d
H == line_intersection(k, j)

Need to prove:
concyclic(E, F, G, H)

Proof:
