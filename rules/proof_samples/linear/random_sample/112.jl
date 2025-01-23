Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == Line(B, A)
c == Circle(C, A, B)
D == center(c)
g == external_angle_bisector(A, D, B)
E == projection(C, g)
F == projection(E, f)
G == midpoint(C, F)

Need to prove:
collinear(G, F, E)

Proof:
