Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
A in c
B in c
C in c
f == Line(B, C)
g == parallel_line(A, f)
D in g, c
h == internal_angle_bisector(D, C, A)
E in h, c
i == internal_angle_bisector(C, A, B)
F == center(c)
G in i, c

Need to prove:
collinear(G, F, E)

Proof:
