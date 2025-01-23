Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h)
f == Line(C, A)
c == Circle(C, A, B)
g == external_angle_bisector(C, A, B)
D == midpoint(B, C)
E == midpoint(C, A)
F == center(c)
G == projection(F, g)
H == midpoint(D, A)
I == projection(H, g)
h == Line(H, I)
J == line_intersection(f, h)

Need to prove:
concyclic(E, G, H, J)

Proof:
