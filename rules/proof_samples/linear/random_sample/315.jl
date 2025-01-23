Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d)
c == Circle(C, A, B)
D == midpoint(B, A)
f == external_angle_bisector(B, D, C)
d == Circle(C, B, D)
g == external_angle_bisector(C, D, A)
E == center(d)
F in g, d
G == center(c)
H in f, d
I == midpoint(H, E)

Need to prove:
collinear(G, I, F)

Proof:
