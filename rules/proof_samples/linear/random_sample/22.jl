Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
H == midpoint(E, C)
k == Line(G, H)
c == Circle(E, B, H)
I in k, c

Need to prove:
concyclic(D, F, G, I)

Proof:
