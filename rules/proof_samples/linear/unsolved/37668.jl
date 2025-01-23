Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E == projection(D, f)
F == projection(D, g)
G == projection(E, i)
k == Line(G, E)
H == midpoint(C, A)
I == line_intersection(j, k)
J == line_intersection(k, h)

Need to prove:
concyclic(F, H, I, J)

Proof:
