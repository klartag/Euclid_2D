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
j == internal_angle_bisector(A, B, C)
E == projection(D, j)
k == Line(D, E)
F == line_intersection(k, g)
c == Circle(C, A, F)
G == line_intersection(j, h)
d == Circle(G, F, E)
H in c, d

Need to prove:
concyclic(A, B, E, H)

Proof:
