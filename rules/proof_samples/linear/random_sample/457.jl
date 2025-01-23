Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E in g
j == internal_angle_bisector(D, C, E)
F == projection(B, j)
k == Line(B, F)
G == midpoint(A, D)
H == line_intersection(i, k)
c == Circle(F, B, C)
d == Circle(G, F, H)
I in d, c
J == center(d)

Need to prove:
concyclic(A, G, I, J)

Proof:
