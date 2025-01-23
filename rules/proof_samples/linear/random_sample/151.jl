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
f == Line(A, B)
g == internal_angle_bisector(D, A, C)
E in g, c
h == internal_angle_bisector(C, E, D)
F == projection(B, h)
i == Line(F, B)
G == line_intersection(h, f)
H == center(c)
I in i, c

Need to prove:
concyclic(A, G, H, I)

Proof:
