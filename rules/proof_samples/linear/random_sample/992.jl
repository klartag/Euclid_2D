Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == external_angle_bisector(C, A, B)
g == internal_angle_bisector(A, C, B)
h == internal_angle_bisector(A, B, C)
i == internal_angle_bisector(C, A, B)
c == Circle(C, A, B)
D in h, c
j == parallel_line(D, g)
F == projection(E, j)
k == Line(E, F)
G == line_intersection(k, i)
d == Circle(G, A, F)
H in f, d

Need to prove:
concyclic(A, B, C, H)

Proof:
