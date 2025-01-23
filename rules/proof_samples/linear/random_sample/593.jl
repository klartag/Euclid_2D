Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l, m: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l, m)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
k == internal_angle_bisector(A, C, B)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
c == Circle(F, E, G)
l == parallel_line(B, k)
H == projection(E, l)
m == external_angle_bisector(C, E, H)
I in m, c

Need to prove:
collinear(C, I, D)

Proof:
