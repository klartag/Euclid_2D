Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E == projection(D, f)
F == projection(D, g)
c == Circle(E, A, F)
G in f, c
H == center(c)
I == line_intersection(f, h)
d == Circle(I, G, F)
J in h, d

Need to prove:
concyclic(D, F, H, J)

Proof:
