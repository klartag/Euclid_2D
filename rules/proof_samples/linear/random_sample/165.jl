Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(C, D, B)
E == midpoint(B, C)
j == internal_angle_bisector(D, C, E)
F == center(c)
G == midpoint(C, A)
H in j, c

Need to prove:
collinear(H, F, G)

Proof:
