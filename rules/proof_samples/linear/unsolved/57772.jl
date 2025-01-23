Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
c == Circle(A, B, D)
E == center(c)
F in g, c
G == midpoint(A, F)
H == projection(E, f)

Need to prove:
concyclic(B, F, G, H)

Proof:
