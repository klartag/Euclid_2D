Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
c == Circle(C, A, B)
D == center(c)
E == projection(D, h)
i == Line(D, E)
F == line_intersection(i, g)
G == midpoint(D, C)
H == midpoint(D, F)
I == line_intersection(i, f)

Need to prove:
concyclic(C, G, H, I)

Proof:
