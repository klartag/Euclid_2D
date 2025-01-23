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
E == center(c)
h == external_angle_bisector(E, D, C)
i == external_angle_bisector(B, E, A)
F in h, c
G in i
H == midpoint(G, E)

Need to prove:
collinear(H, G, F)

Proof:
