Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
A in c
B in c
C in c
D in c
f == Line(C, A)
g == Line(D, B)
E == line_intersection(f, g)
h == internal_angle_bisector(D, C, B)
F == midpoint(C, A)
G == center(c)
H in h, c
I == projection(H, g)

Need to prove:
concyclic(E, F, G, I)

Proof:
