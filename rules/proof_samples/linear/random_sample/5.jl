Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k, l)
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
k == Line(B, F)
H in k, c
l == Line(E, F)
I == midpoint(B, F)
J == line_intersection(l, i)

Need to prove:
concyclic(E, H, I, J)

Proof:
