Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
k == internal_angle_bisector(G, A, F)
c == Circle(C, A, F)
H in k, c
l == internal_angle_bisector(D, C, G)

Need to prove:
H in l

Proof:
