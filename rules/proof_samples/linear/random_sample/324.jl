Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
F == midpoint(B, C)
G == midpoint(C, A)
H == midpoint(B, A)
c == Circle(H, G, E)
h == Line(F, E)
I == center(c)
i == Line(H, I)
J == line_intersection(i, h)

Need to prove:
concyclic(D, F, I, J)

Proof:
