Assumptions:
A, B, C, D, E, F: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h)
A in c
B in c
C in c
f == external_angle_bisector(A, C, B)
D in f, c
E == center(c)
g == external_angle_bisector(A, B, E)
h == internal_angle_bisector(B, E, D)
F == projection(D, g)

Need to prove:
F in h

Proof:
