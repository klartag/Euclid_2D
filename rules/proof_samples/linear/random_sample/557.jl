Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == projection(D, f)
j == Line(D, E)
F == line_intersection(j, g)
G == center(c)
H == line_intersection(g, i)
d == Circle(B, F, D)
I == center(d)

Need to prove:
concyclic(D, G, H, I)

Proof:
