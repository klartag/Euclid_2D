Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == Line(B, A)
D == midpoint(C, A)
E == projection(C, f)
g == internal_angle_bisector(E, D, A)
F == projection(B, g)
c == Circle(F, D, A)
G == center(c)

Need to prove:
collinear(D, G, A)

Proof:
