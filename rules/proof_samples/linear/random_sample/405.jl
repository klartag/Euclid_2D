Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
c == Circle(C, A, B)
D == midpoint(B, A)
f == internal_angle_bisector(C, A, D)
E == center(c)
g == internal_angle_bisector(B, E, C)
F in f, c
G == line_intersection(f, g)

Need to prove:
false() # collinear(C, F, G)

Proof:
