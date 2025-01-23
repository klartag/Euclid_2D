Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
f == internal_angle_bisector(A, B, C)
D == midpoint(B, A)
E == projection(A, f)
g == Line(E, A)
F == midpoint(E, D)
G == midpoint(C, A)
H == midpoint(E, A)
c == Circle(G, F, H)
I in g, c

Need to prove:
concyclic(A, D, G, I)

Proof:
