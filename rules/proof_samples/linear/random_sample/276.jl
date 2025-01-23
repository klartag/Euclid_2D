Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D in h
E == midpoint(D, C)
j == Line(E, A)
F == midpoint(C, E)
G == projection(C, j)
c == Circle(G, A, B)
H in i, c
I == center(c)

Need to prove:
concyclic(F, G, H, I)

Proof:
