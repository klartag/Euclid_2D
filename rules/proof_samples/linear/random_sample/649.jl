Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
j == internal_angle_bisector(D, E, C)
F == projection(C, j)
d == Circle(E, D, C)
G == projection(E, g)
H in i, d
e == Circle(B, F, G)
I in e, c

Need to prove:
concyclic(C, G, H, I)

Proof:
