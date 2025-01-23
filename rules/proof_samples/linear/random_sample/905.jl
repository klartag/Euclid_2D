Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E == projection(D, f)
k == parallel_line(E, j)
F == projection(E, j)
l == Line(F, E)
G == line_intersection(i, k)
c == Circle(D, F, B)
H == line_intersection(g, l)
I in g, c

Need to prove:
concyclic(E, G, H, I)

Proof:
