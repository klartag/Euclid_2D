Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E == projection(D, g)
F == projection(D, f)
c == Circle(F, C, E)
d == Circle(D, C, A)
G in d, c
H in f, d

Need to prove:
false() # concyclic(B, E, G, H)

Proof:
