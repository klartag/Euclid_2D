Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E == projection(D, f)
F == projection(D, g)
G == midpoint(E, F)
c == Circle(D, C, A)
j == Line(F, B)
H in f, c
I == line_intersection(j, h)

Need to prove:
collinear(H, I, G)

Proof:
