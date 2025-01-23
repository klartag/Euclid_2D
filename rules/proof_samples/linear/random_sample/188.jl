Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
f == Line(B, A)
D == midpoint(B, C)
E == projection(C, f)
g == external_angle_bisector(E, D, B)
F == projection(B, g)
G == midpoint(C, A)
c == Circle(F, G, B)
H == center(c)

Need to prove:
collinear(B, G, H)

Proof:
