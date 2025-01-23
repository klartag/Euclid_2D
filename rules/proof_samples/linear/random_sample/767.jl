Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k, l, m: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
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
l == Line(F, G)
m == Line(G, E)
H == line_intersection(i, l)
I == line_intersection(m, j)
c == Circle(H, C, A)
J in k, c

Need to prove:
concyclic(B, C, I, J)

Proof:
