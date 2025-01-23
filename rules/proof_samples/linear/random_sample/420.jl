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
i == parallel_line(A, g)
D == line_intersection(h, i)
j == internal_angle_bisector(B, A, D)
E == line_intersection(j, h)
c == Circle(A, E, B)
k == parallel_line(C, j)
d == Circle(E, B, C)
F == center(c)
G in i, c
H in k, d

Need to prove:
concyclic(D, F, G, H)

Proof:
