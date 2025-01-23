Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
i == internal_angle_bisector(C, A, B)
j == internal_angle_bisector(A, B, C)
D == line_intersection(j, i)
E == projection(D, g)
F == projection(D, h)
G == midpoint(C, A)
H == projection(G, i)
k == Line(G, H)
I == line_intersection(k, f)
c == Circle(D, I, B)
J in g, c

Need to prove:
concyclic(E, F, G, J)

Proof:
