Assumptions:
A, B, C, D, E, F: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(f, g)
distinct(c, d)
A in c
B in c
C in c
D == center(c)
f == internal_angle_bisector(C, D, A)
d == Circle(B, A, D)
g == internal_angle_bisector(B, D, C)
E == projection(C, f)
F in g, d

Need to prove:
collinear(F, E, C)

Proof:
