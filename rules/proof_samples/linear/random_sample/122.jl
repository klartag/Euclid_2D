Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k, l, m: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k, l, m)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
j == external_angle_bisector(B, D, A)
E == line_intersection(g, i)
F == midpoint(C, A)
k == internal_angle_bisector(B, D, A)
l == external_angle_bisector(B, C, F)
G in k, c
m == Line(E, G)

Need to prove:
concurrent(j, l, m)

Proof:
