Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == internal_angle_bisector(C, A, D)
E == midpoint(D, C)
i == internal_angle_bisector(B, D, A)
F in h, c
G == midpoint(E, F)
H in i, c

Need to prove:
collinear(H, F, G)

Proof:
