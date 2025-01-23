Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
B in f # (defining f)
g == internal_angle_bisector(C, A, B)
h == internal_angle_bisector(A, B, C)
i == internal_angle_bisector(A, C, B)
D == line_intersection(h, g)
E == projection(D, f)
F == projection(E, h)
c == Circle(F, B, C)
G in i, c

Need to prove:
concyclic(D, E, F, G)

Proof:
