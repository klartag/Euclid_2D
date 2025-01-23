Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(C, A)
F == projection(E, f)
j == Line(E, F)
k == parallel_line(D, j)
G == line_intersection(f, k)
c == Circle(D, B, G)
H in h, c

Need to prove:
collinear(G, H, E)

Proof:
