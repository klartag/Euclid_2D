Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == projection(B, g)
i == Line(E, B)
j == parallel_line(E, h)
F in i, c
G == projection(F, j)
k == Line(F, G)

Need to prove:
concurrent(g, h, k)

Proof:
