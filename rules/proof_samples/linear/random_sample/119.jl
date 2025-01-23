Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
A in c
B in c
C in c
D in c
f == Line(C, A)
g == external_angle_bisector(D, C, A)
h == internal_angle_bisector(C, D, A)
E in h, c
F == midpoint(B, E)
i == Line(B, E)
G == line_intersection(i, f)
H == line_intersection(h, g)
I == midpoint(H, E)

Need to prove:
concyclic(F, G, H, I)

Proof:
