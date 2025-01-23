Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(C, A)
E == center(c)
j == Line(E, A)
k == internal_angle_bisector(A, E, C)
d == Circle(E, D, C)
F in k, d
G == line_intersection(g, k)
H == projection(F, i)
I in j, d
J == projection(G, j)

Need to prove:
concyclic(F, H, I, J)

Proof:
