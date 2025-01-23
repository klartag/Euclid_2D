Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k, l, m: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k, l, m)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
c == Circle(G, F, E)
k == internal_angle_bisector(D, G, B)
H in k, c
I == projection(C, f)
l == Line(I, C)
J == projection(D, l)
m == Line(J, D)

Need to prove:
H in m

Proof:
