Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
F == projection(E, i)
j == Line(E, F)
G == line_intersection(f, j)
d == Circle(B, E, G)
e == Circle(B, E, F)
H in c, e
I in g, d

Need to prove:
concyclic(C, F, H, I)

Proof:
