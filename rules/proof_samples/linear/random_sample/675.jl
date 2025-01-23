Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k, l: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k, l)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
c == Circle(G, F, E)
k == parallel_line(G, g)
H in k, c
l == internal_angle_bisector(H, E, G)
d == Circle(B, H, E)
I == center(d)
J in l, d

Need to prove:
collinear(J, I, B)

Proof:
