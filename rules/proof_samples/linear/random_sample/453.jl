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
j == internal_angle_bisector(A, C, B)
E == center(c)
F == line_intersection(g, i)
k == Line(E, F)
G == line_intersection(j, k)

Need to prove:
concyclic(A, B, C, G)

Proof:
