Assumptions:
A, B, C, D, E, F: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h)
distinct(c, d)
A in c
B in c
C in c
f == Line(B, C)
D == midpoint(C, A)
E == center(c)
g == internal_angle_bisector(C, E, B)
h == parallel_line(A, f)
d == Circle(A, E, D)
F in g, d

Need to prove:
F in h

Proof:
