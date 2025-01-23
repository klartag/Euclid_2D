Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k)
A in c
B in c
C in c
f == Line(A, B)
g == Line(B, C)
h == Line(C, A)
D == center(c)
E == projection(D, f)
i == Line(D, E)
F == line_intersection(i, g)
j == Line(A, F)
G in j, c
k == Line(G, B)

Need to prove:
concurrent(h, i, k)

Proof:
