Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == internal_angle_bisector(B, C, D)
c == Circle(C, D, B)
E in j, c
F == center(c)
G == midpoint(C, A)
k == Line(F, G)
H == midpoint(E, F)

Need to prove:
H in k

Proof:
