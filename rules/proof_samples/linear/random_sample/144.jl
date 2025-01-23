Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d)
f == Line(C, A)
c == Circle(C, A, B)
D == center(c)
E == midpoint(C, D)
g == internal_angle_bisector(C, D, A)
d == Circle(A, C, D)
F in g
G == projection(F, f)
H == center(d)

Need to prove:
concyclic(C, E, G, H)

Proof:
