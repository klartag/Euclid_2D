Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E == projection(D, f)
F == projection(D, g)
c == Circle(C, D, F)
k == internal_angle_bisector(B, E, F)
G in i, c
H == line_intersection(j, k)
l == internal_angle_bisector(G, E, F)
I == line_intersection(l, i)

Need to prove:
concyclic(E, F, H, I)

Proof:
