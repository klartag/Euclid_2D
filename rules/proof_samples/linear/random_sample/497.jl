Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == internal_angle_bisector(A, B, C)
d == Circle(D, C, A)
E == projection(C, h)
i == Line(E, C)
F in i, d
G == center(d)
H == midpoint(D, B)

Need to prove:
collinear(F, H, G)

Proof:
