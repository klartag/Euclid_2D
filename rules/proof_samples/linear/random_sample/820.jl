Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
distinct(c, d)
A in c
B in c
C in c
D in c
f == Line(A, B)
g == Line(C, D)
h == Line(C, A)
i == Line(D, B)
E == line_intersection(h, i)
F == center(c)
j == Line(E, F)
d == Circle(A, F, C)
G == line_intersection(f, g)
H in j, d

Need to prove:
concyclic(A, D, G, H)

Proof:
