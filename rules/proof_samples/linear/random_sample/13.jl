Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(A, B, D)
j == internal_angle_bisector(B, C, D)
k == external_angle_bisector(A, B, C)
E == projection(A, j)
F in k, c
G == projection(E, k)
l == parallel_line(E, f)
H == line_intersection(i, l)

Need to prove:
concyclic(A, F, G, H)

Proof:
