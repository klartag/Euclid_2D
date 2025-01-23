Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E == projection(D, g)
F == projection(D, f)
c == Circle(F, C, E)
d == Circle(C, D, B)
G in g, d
H in f, c
I == center(d)

Need to prove:
concyclic(A, G, H, I)

Proof:
