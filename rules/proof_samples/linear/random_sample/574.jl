Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
c == Circle(C, A, B)
f == internal_angle_bisector(A, B, C)
D in f, c
g == internal_angle_bisector(A, C, B)
E == projection(D, g)
h == Line(D, E)
F in h, c
G == midpoint(F, A)
H == line_intersection(g, f)

Need to prove:
collinear(H, F, G)

Proof:
