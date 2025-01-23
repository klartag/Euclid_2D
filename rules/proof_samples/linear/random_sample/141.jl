Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
f == Line(B, C)
c == Circle(C, A, B)
g == internal_angle_bisector(A, C, B)
D in g, c
E == projection(A, g)
F == projection(D, f)
G == midpoint(B, E)
H == midpoint(B, A)

Need to prove:
collinear(F, H, G)

Proof:
