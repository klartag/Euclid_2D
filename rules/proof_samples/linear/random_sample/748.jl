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
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(D, C, A)
E == center(c)
F in g, c
j == Line(A, F)
k == Line(E, B)
d == Circle(E, F, D)
G == line_intersection(j, h)
H in k, d
I == center(d)

Need to prove:
concyclic(A, G, H, I)

Proof:
