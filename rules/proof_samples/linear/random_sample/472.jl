Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(B, C)
c == Circle(F, A, C)
d == Circle(B, C, E)
I == center(c)
J in d, c

Need to prove:
concyclic(G, H, I, J)

Proof:
