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
c == Circle(C, D, B)
E == center(c)
F == midpoint(C, A)
d == Circle(F, B, C)
j == Line(E, C)
G == projection(F, h)
k == Line(F, G)
H in j, d

Need to prove:
H in k

Proof:
