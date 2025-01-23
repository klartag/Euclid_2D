Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E == projection(D, g)
F == projection(D, f)
G == projection(C, i)
H == projection(E, i)
I == projection(G, h)

Need to prove:
concyclic(D, F, H, I)

Proof:
