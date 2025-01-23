Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k)
f == Line(B, C)
g == Line(C, A)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E == projection(D, f)
F == projection(D, g)
c == Circle(E, A, F)
j == external_angle_bisector(E, C, A)
G == projection(A, j)
k == Line(D, E)
H in k, c
I == midpoint(G, H)

Need to prove:
collinear(H, I, A)

Proof:
