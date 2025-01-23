Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == center(c)
F == projection(C, h)
i == Line(F, C)
j == Line(E, A)
G == projection(B, i)
k == Line(G, B)
H == line_intersection(k, j)
d == Circle(B, F, D)
e == Circle(E, H, B)
I in d, e

Need to prove:
concyclic(A, C, F, I)

Proof:
