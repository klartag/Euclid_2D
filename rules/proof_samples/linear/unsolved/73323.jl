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
D in j
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
c == Circle(G, F, E)
k == external_angle_bisector(G, F, E)
l == external_angle_bisector(E, D, F)
H in k, c
I == line_intersection(h, l)
m == parallel_line(H, i)
J == line_intersection(h, m)

Need to prove:
concyclic(D, H, I, J)

Proof:
