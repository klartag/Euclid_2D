Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == midpoint(B, A)
F == center(c)
G == midpoint(C, A)
H == midpoint(C, E)
i == Line(G, H)
j == internal_angle_bisector(A, F, D)

Need to prove:
concurrent(h, i, j)

Proof:
