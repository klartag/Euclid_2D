Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E in g
F == center(c)
j == Line(B, F)
G == line_intersection(j, i)
d == Circle(B, E, G)
k == Line(E, F)
H in k, d

Need to prove:
concyclic(A, F, G, H)

Proof:
