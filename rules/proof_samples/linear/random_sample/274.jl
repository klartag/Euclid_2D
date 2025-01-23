Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
A in c
B in c
C in c
D in c
f == Line(B, C)
g == Line(D, B)
E == projection(C, g)
F == midpoint(A, D)
G == midpoint(D, B)
H == center(c)
h == Line(H, C)
I == projection(E, f)
i == Line(E, I)
J == line_intersection(i, h)

Need to prove:
concyclic(D, F, G, J)

Proof:
