Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E == projection(D, g)
F == projection(D, f)
k == Line(E, F)
G == line_intersection(k, j)
c == Circle(G, F, A)
l == parallel_line(A, i)
H == midpoint(G, D)
I in l, c
J == midpoint(F, I)

Need to prove:
concyclic(D, H, I, J)

Proof:
