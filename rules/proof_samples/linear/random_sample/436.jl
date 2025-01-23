Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
c == Circle(C, A, B)
D == center(c)
f == internal_angle_bisector(C, B, D)
d == Circle(C, B, D)
g == internal_angle_bisector(C, A, B)
E in g, c
F == center(d)
G == projection(E, f)
h == Line(G, D)
H in h, d

Need to prove:
concyclic(B, E, F, H)

Proof:
