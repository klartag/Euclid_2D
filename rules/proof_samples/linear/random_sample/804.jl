Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
F == projection(E, h)
j == Line(E, F)
G == line_intersection(f, j)
H == line_intersection(g, i)
d == Circle(D, A, F)
e == Circle(G, E, D)
I in j, d
J in e, c

Need to prove:
concyclic(C, H, I, J)

Proof:
