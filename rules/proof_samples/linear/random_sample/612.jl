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
G == midpoint(C, A)
c == Circle(G, F, D)
H in i, c
I == midpoint(F, B)

Need to prove:
concyclic(A, E, H, I)

Proof:
