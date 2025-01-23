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
j == Line(B, D)
k == parallel_line(A, j)
E == line_intersection(k, h)
c == Circle(F, C, E)
G == center(c)
H == projection(G, f)

Need to prove:
collinear(H, G, D)

Proof:
