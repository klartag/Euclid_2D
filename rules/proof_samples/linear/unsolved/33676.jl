Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, h)
F == projection(D, f)
c == Circle(A, E, F)
G in j, c
k == Line(E, G)
H == projection(F, j)
l == Line(F, H)

Need to prove:
concurrent(g, k, l)

Proof:
