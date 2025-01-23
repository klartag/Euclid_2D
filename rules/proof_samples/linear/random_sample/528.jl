Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(B, A)
c == Circle(C, A, B)
D == center(c)
g == external_angle_bisector(A, C, D)
E == midpoint(B, C)
F in g, c
G == projection(F, f)
h == Line(F, G)
H == projection(D, h)

Need to prove:
concyclic(B, E, F, H)

Proof:
