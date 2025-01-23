Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k, l: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k, l)
distinct(c, d, e)
f == Line(B, A)
B in g # (defining g)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
k == internal_angle_bisector(A, C, B)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
c == Circle(E, B, G)
l == Line(E, F)
H == line_intersection(l, j)
I in k, c
d == Circle(H, D, A)
e == Circle(E, H, I)
J in d, e

Need to prove:
concyclic(D, F, G, J)

Proof:
