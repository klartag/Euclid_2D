Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d)
c == Circle(C, A, B)
D == center(c)
f == external_angle_bisector(D, A, B)
d == Circle(A, B, D)
E == center(d)
g == external_angle_bisector(A, B, D)
F == line_intersection(g, f)
G in f, d

Need to prove:
concyclic(B, E, F, G)

Proof:
