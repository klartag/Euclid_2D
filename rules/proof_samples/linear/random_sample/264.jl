Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
c == Circle(E, F, G)
d == Circle(G, A, B)
H == center(c)
I == center(d)
k == external_angle_bisector(A, H, F)
l == parallel_line(I, h)

Need to prove:
concurrent(j, k, l)

Proof:
