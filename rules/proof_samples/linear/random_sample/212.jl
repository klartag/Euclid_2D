Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == center(c)
h == Line(C, A)
d == Circle(A, E, D)
F == midpoint(E, D)
G == midpoint(D, A)
i == parallel_line(G, f)
j == internal_angle_bisector(B, E, F)
H == line_intersection(i, j)
I in h, d

Need to prove:
collinear(I, B, H)

Proof:
