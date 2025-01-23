Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f: Line
c, d, e, g: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(c, d, e, g)
A in c
B in c
C in c
D in c
E == midpoint(D, B)
d == Circle(A, B, E)
e == Circle(E, D, A)
f == internal_angle_bisector(A, C, B)
F == center(d)
G in f, c
g == Circle(A, F, G)
H == center(c)
I == center(e)
J == center(g)

Need to prove:
concyclic(F, H, I, J)

Proof:
