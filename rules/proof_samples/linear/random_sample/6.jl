Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d)
f == Line(C, A)
c == Circle(C, A, B)
g == internal_angle_bisector(A, B, C)
D in g, c
d == Circle(B, D, A)
E == projection(D, f)
F == center(d)
G == midpoint(E, F)

Need to prove:
collinear(D, F, G)

Proof:
