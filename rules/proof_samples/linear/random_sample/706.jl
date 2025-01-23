Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
f == Line(C, A)
g == external_angle_bisector(A, C, B)
c == Circle(C, A, B)
D in g, c
E == projection(D, f)
h == Line(E, D)
F == projection(B, g)
i == Line(F, B)
G == line_intersection(h, i)

Need to prove:
concyclic(A, B, C, G)

Proof:
