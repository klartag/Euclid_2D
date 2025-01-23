Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
f == Line(C, A)
g == internal_angle_bisector(C, A, B)
D == midpoint(B, A)
E == projection(D, g)
E in h # (defining h)
F == line_intersection(h, f)
c == Circle(A, F, B)
G == midpoint(D, A)
H in h, c

Need to prove:
concyclic(B, E, G, H)

Proof:
