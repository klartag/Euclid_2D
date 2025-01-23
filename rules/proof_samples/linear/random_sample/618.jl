Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == center(c)
F == midpoint(B, A)
h == internal_angle_bisector(B, E, A)
d == Circle(E, D, B)
G == midpoint(F, A)
H in h, d
I == projection(E, g)
J == midpoint(D, I)

Need to prove:
collinear(J, H, G)

Proof:
