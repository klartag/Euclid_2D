Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
c == Circle(C, A, B)
D == projection(C, h)
i == Line(D, C)
d == Circle(A, B, D)
E == midpoint(C, A)
F in i, c
e == Circle(F, D, A)
j == Line(D, E)
G == center(d)
H in g, e
I == line_intersection(j, f)

Need to prove:
concyclic(E, G, H, I)

Proof:
