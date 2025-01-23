Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k, l: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k, l)
distinct(c, d, e)
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
l == external_angle_bisector(A, B, C)
c == Circle(E, C, G)
d == Circle(D, F, B)
H == line_intersection(i, l)
e == Circle(D, A, G)
I in k, d
J in e, c

Need to prove:
concyclic(D, H, I, J)

Proof:
