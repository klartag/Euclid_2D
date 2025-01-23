Assumptions:
A, B, C, D, E, F: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F)
distinct(f, g)
distinct(c, d)
f == external_angle_bisector(A, C, B)
g == internal_angle_bisector(A, B, C)
D == line_intersection(f, g)
c == Circle(D, B, A)
E == center(c)
d == Circle(E, C, A)
F in d, c

Need to prove:
false() # collinear(A, F, B)

Proof:
