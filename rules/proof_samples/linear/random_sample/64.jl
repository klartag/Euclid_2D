Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
A in f # (defining f)
g == Line(B, C)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
j == internal_angle_bisector(A, C, B)
D == line_intersection(h, i)
E == projection(D, g)
F == projection(D, f)
G == projection(E, i)
c == Circle(A, F, G)
H in i, c
I == projection(H, j)

Need to prove:
concyclic(B, E, H, I)

Proof:
