Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
i == internal_angle_bisector(A, B, C)
E == line_intersection(h, i)
j == internal_angle_bisector(D, A, B)
d == Circle(A, E, B)
e == Circle(E, B, C)
F in j, d
G == center(e)

Need to prove:
concyclic(D, E, F, G)

Proof:
