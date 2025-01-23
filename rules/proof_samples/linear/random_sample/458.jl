Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(C, D, B)
d == Circle(D, A, E)
F == center(d)
G == center(c)
H == midpoint(F, G)
I == midpoint(C, A)
J == projection(H, i)

Need to prove:
collinear(J, I, H)

Proof:
