Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == midpoint(B, D)
F == midpoint(C, A)
G == midpoint(E, F)
H == projection(G, f)
j == Line(G, H)

Need to prove:
concurrent(g, i, j)

Proof:
