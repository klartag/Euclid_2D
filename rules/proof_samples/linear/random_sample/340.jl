Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(B, E)
G == midpoint(E, C)
H == midpoint(F, B)
c == Circle(G, E, D)
I in i, c

Need to prove:
concyclic(B, D, H, I)

Proof:
