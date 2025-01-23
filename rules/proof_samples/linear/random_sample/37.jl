Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
f == Line(C, A)
D == midpoint(B, C)
E == midpoint(B, A)
c == Circle(E, D, B)
g == external_angle_bisector(E, B, C)
F in g, c
G == center(c)
H == projection(G, f)

Need to prove:
collinear(H, G, F)

Proof:
