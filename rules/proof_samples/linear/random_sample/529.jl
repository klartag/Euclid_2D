Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
i == internal_angle_bisector(D, B, C)
E in i, c
F == projection(E, g)
j == Line(E, F)
G == center(c)
H == line_intersection(j, h)

Need to prove:
concyclic(B, D, G, H)

Proof:
