Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
F == projection(E, h)
G == line_intersection(g, i)
j == internal_angle_bisector(A, C, G)
H in j, c
I == midpoint(F, H)

Need to prove:
collinear(E, I, G)

Proof:
