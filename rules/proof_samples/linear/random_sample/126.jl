Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
k == internal_angle_bisector(A, C, B)
D == line_intersection(j, i)
E == projection(D, g)
F in h
G == projection(D, f)
c == Circle(F, E, G)
d == Circle(D, G, F)
l == internal_angle_bisector(C, F, E)
H in k, d
I in l, c

Need to prove:
collinear(H, D, I)

Proof:
