Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E == projection(D, g)
F == projection(D, f)
G == midpoint(E, F)
H == line_intersection(j, f)
c == Circle(D, H, G)
I == projection(F, j)
J in f, c

Need to prove:
concyclic(E, F, I, J)

Proof:
