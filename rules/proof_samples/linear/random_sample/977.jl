Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l, m: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
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
k == internal_angle_bisector(A, F, G)
H in k, c
l == internal_angle_bisector(G, D, A)
I == projection(H, l)
m == Line(H, I)

Need to prove:
G in m

Proof:
