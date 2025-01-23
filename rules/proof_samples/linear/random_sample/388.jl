Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == Line(C, A)
c == Circle(C, A, B)
D == center(c)
h == external_angle_bisector(B, D, C)
E == line_intersection(h, g)
F == projection(B, h)
G == line_intersection(h, f)
d == Circle(G, D, B)
H in d, c

Need to prove:
concyclic(B, E, F, H)

Proof:
