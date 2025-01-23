Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h: Line
c, d, e, k: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h)
distinct(c, d, e, k)
A in c
B in c
C in c
f == Line(B, C)
g == Line(C, A)
D == center(c)
h == internal_angle_bisector(A, D, B)
d == Circle(C, B, D)
E == midpoint(A, B)
e == Circle(B, E, D)
F == line_intersection(g, h)
G in f, e
H == line_intersection(h, f)
I == center(d)
k == Circle(H, I, G)
J in k, e

Need to prove:
concyclic(A, E, F, J)

Proof:
