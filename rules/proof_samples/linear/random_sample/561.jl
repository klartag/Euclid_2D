Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j: Line
c, d, e, k: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j)
distinct(c, d, e, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
d == Circle(A, B, D)
j == parallel_line(E, i)
F == line_intersection(g, j)
e == Circle(E, B, D)
G in j, e
H == line_intersection(f, j)
I == midpoint(H, G)
k == Circle(F, G, B)
J in k, d

Need to prove:
concyclic(A, E, I, J)

Proof:
