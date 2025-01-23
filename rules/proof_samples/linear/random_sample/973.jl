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
h == external_angle_bisector(B, D, A)
E in h, c
F == midpoint(D, A)
i == external_angle_bisector(F, A, C)
G in i, c
H == projection(E, g)

Need to prove:
collinear(E, G, H)

Proof:
