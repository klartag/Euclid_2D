Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E == projection(D, g)
F == projection(D, f)
c == Circle(E, D, B)
k == Line(E, F)
G == line_intersection(j, k)
H == line_intersection(k, h)
I in j, c
J in h, c

Need to prove:
concyclic(G, H, I, J)

Proof:
