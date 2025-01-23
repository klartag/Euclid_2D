Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == projection(B, h)
F == center(c)
j == parallel_line(F, g)
k == Line(E, F)
G == projection(B, j)
l == Line(B, G)

Need to prove:
concurrent(i, k, l)

Proof:
