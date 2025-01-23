Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
D == midpoint(B, C)
E == projection(D, g)
c == Circle(E, A, D)
F in f, c
h == external_angle_bisector(C, E, D)
i == external_angle_bisector(C, F, A)
d == Circle(C, E, D)
G == center(d)
H == projection(C, h)
I in i, c

Need to prove:
concyclic(F, G, H, I)

Proof:
