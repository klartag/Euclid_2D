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
j == internal_angle_bisector(B, C, D)
E in j, c
k == Line(A, E)
F == line_intersection(g, i)
l == parallel_line(B, j)
G == midpoint(B, A)
m == Line(F, G)

Need to prove:
concurrent(k, l, m)

Proof:
