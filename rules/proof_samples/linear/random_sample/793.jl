Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == internal_angle_bisector(C, A, D)
E in h, c
F == center(c)
G == midpoint(B, A)
d == Circle(F, B, C)
i == Line(E, G)
H in i, d
e == Circle(H, C, E)
I == center(e)

Need to prove:
concyclic(B, C, F, I)

Proof:
