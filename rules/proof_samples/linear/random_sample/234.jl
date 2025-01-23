Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
c == Circle(C, A, B)
D == center(c)
E == projection(D, f)
g == Line(D, E)
h == external_angle_bisector(D, B, A)
F in h, c
d == Circle(D, B, F)
i == Line(F, E)
G in i, c
H in g, d

Need to prove:
concyclic(A, E, G, H)

Proof:
