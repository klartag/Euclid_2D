Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l, m: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l, m)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
j == internal_angle_bisector(D, A, C)
E == center(c)
F == line_intersection(g, i)
k == Line(B, E)
G in j, c
d == Circle(D, F, C)
H == center(d)
l == parallel_line(G, k)
m == Line(D, E)
I == line_intersection(l, m)

Need to prove:
concyclic(D, G, H, I)

Proof:
