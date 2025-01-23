Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == internal_angle_bisector(D, A, B)
E == projection(D, h)
i == Line(E, D)
F in i, c
G == midpoint(C, A)

Need to prove:
concyclic(A, E, F, G)

Proof:
