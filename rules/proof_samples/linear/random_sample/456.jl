Assumptions:
A, B, C, D, E, F, G: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == midpoint(D, B)
h == internal_angle_bisector(D, E, C)
F == line_intersection(f, h)
d == Circle(E, A, F)
G == center(d)

Need to prove:
concyclic(A, C, E, G)

Proof:
