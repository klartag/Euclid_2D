Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == center(c)
F == midpoint(A, E)
h == internal_angle_bisector(D, E, F)
i == internal_angle_bisector(B, E, A)
G == line_intersection(i, g)
H == projection(A, h)

Need to prove:
concyclic(D, E, G, H)

Proof:
