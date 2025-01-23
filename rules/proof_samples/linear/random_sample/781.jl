Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d)
A in c
B in c
C in c
f == Line(A, B)
g == Line(C, A)
D == center(c)
E == projection(C, f)
F == projection(D, f)
h == Line(F, D)
d == Circle(F, E, C)
G == line_intersection(h, g)
H in c, d

Need to prove:
concyclic(B, F, G, H)

Proof:
