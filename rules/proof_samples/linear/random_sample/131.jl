Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
c == Circle(E, A, D)
G == midpoint(B, C)
d == Circle(C, D, F)
H == center(c)
I == center(d)

Need to prove:
concyclic(D, G, H, I)

Proof:
