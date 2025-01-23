Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
E == center(c)
i == internal_angle_bisector(C, D, E)
F in i, c
G == projection(F, g)
d == Circle(G, E, F)
e == Circle(D, E, B)
H in e, d

Need to prove:
collinear(H, D, A)

Proof:
