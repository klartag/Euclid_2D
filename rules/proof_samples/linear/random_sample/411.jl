Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
j == internal_angle_bisector(C, D, A)
F == projection(A, j)
G == projection(E, i)
H == projection(E, g)

Need to prove:
collinear(H, F, G)

Proof:
