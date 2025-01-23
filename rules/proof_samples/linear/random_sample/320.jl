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
E == line_intersection(g, i)
F == center(c)
G == projection(F, g)
j == Line(F, G)
d == Circle(F, E, C)
H == projection(C, f)
I in j, d

Need to prove:
concyclic(C, G, H, I)

Proof:
