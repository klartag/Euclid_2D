Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
c == Circle(G, F, E)
k == internal_angle_bisector(C, E, G)
H in k, c

Need to prove:
collinear(B, H, D)

Proof:
