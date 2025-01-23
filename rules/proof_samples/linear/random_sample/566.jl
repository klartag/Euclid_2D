Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(C, A)
H == midpoint(B, A)
c == Circle(D, B, F)
j == internal_angle_bisector(G, D, C)
I in j, c
G in k # (defining k)
J == projection(I, k)

Need to prove:
concyclic(G, H, I, J)

Proof:
