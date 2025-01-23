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
j == internal_angle_bisector(B, C, D)
k == external_angle_bisector(C, D, A)
E == line_intersection(j, i)
F == line_intersection(k, f)
c == Circle(E, A, B)
d == Circle(F, D, A)
G in c, d
H in h, d
I == line_intersection(k, g)

Need to prove:
concyclic(C, G, H, I)

Proof:
