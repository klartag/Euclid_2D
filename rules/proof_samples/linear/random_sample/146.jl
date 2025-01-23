Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == projection(B, h)
j == Line(E, A)
F == line_intersection(j, g)
c == Circle(E, A, D)
d == Circle(F, A, B)
G in c, d
H == midpoint(B, C)
k == Line(H, G)

Need to prove:
D in k

Proof:
