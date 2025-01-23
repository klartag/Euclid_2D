Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
A in c
B in c
C in c
D in c
f == internal_angle_bisector(D, B, A)
E in f, c
g == internal_angle_bisector(D, E, A)
F == midpoint(B, C)
G == projection(C, g)
H == center(c)

Need to prove:
concyclic(C, F, G, H)

Proof:
