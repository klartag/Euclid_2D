Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(B, E)
j == Line(C, F)
c == Circle(F, A, E)
G == center(c)
H == projection(G, j)
k == Line(G, H)
I == line_intersection(k, i)
J == midpoint(F, D)

Need to prove:
concyclic(F, H, I, J)

Proof:
