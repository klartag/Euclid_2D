Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
j == external_angle_bisector(D, A, C)
E == line_intersection(g, i)
F == center(c)
G in j, c
k == Line(E, F)

Need to prove:
G in k

Proof:
