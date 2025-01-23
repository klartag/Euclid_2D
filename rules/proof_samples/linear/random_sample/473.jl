Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
A in c
B in c
C in c
f == Line(A, B)
g == Line(B, C)
D == center(c)
E == projection(D, f)
F == projection(A, g)
h == external_angle_bisector(A, E, F)
d == Circle(E, F, A)
G == line_intersection(h, g)
H in d, c

Need to prove:
concyclic(C, E, G, H)

Proof:
