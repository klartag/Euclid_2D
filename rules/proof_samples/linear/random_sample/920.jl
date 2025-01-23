Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(B, C)
I == midpoint(B, A)
j == Line(I, E)
c == Circle(C, G, E)
J in j, c

Need to prove:
concyclic(B, E, H, J)

Proof:
