Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
c == Circle(C, A, B)
g == external_angle_bisector(A, C, B)
D in g, c
h == internal_angle_bisector(C, A, D)
i == internal_angle_bisector(D, B, C)
j == internal_angle_bisector(B, D, A)
E == line_intersection(j, f)
F == line_intersection(h, i)
G == midpoint(B, F)
H == center(c)

Need to prove:
concyclic(B, E, G, H)

Proof:
