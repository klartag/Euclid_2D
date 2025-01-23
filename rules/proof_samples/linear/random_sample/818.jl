Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
c == Circle(B, C, E)
G == midpoint(F, C)
H == midpoint(B, A)
I == center(c)

Need to prove:
concyclic(D, G, H, I)

Proof:
