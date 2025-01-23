Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
j == Line(B, D)
E == center(c)
F == line_intersection(g, i)
k == internal_angle_bisector(B, F, A)
G == midpoint(B, F)
H == line_intersection(j, k)
I == midpoint(E, F)

Need to prove:
concyclic(C, G, H, I)

Proof:
