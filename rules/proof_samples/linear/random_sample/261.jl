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
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
k == parallel_line(G, h)
c == Circle(A, B, E)
H == projection(C, k)
I == center(c)
J == midpoint(H, E)

Need to prove:
concyclic(E, F, I, J)

Proof:
