Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
distinct(c, d)
A in c
B in c
C in c
D in c
f == Line(C, A)
g == Line(D, B)
E == line_intersection(f, g)
F == midpoint(E, B)
G == midpoint(E, C)
d == Circle(G, F, A)

Need to prove:
D in d

Proof:
