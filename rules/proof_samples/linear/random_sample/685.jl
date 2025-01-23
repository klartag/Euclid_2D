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
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(B, C)
H == midpoint(B, A)
c == Circle(F, A, C)
I in c
J == midpoint(B, I)

Need to prove:
concyclic(E, G, H, J)

Proof:
