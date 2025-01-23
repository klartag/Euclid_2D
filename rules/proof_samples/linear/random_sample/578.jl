Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i)
f == Line(C, A)
g == parallel_line(B, f)
D in f
h == external_angle_bisector(C, A, B)
c == Circle(D, B, A)
E in g, c
i == internal_angle_bisector(E, D, A)
F == projection(E, i)
G in h, c

Need to prove:
collinear(G, E, F)

Proof:
