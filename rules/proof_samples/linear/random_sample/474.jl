Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
F == line_intersection(g, i)
d == Circle(A, E, F)
j == Line(B, D)
G in h, d
H in j
k == Line(H, G)
I in k, d

Need to prove:
concyclic(A, B, H, I)

Proof:
