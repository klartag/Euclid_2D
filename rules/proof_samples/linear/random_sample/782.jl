Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
k == internal_angle_bisector(A, C, B)
D == line_intersection(j, i)
E == projection(D, h)
F == projection(D, f)
G in h
H == projection(G, k)
l == Line(G, H)
I == line_intersection(l, g)
c == Circle(F, E, G)
J in f, c

Need to prove:
concyclic(B, D, I, J)

Proof:
