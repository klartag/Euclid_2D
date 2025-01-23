Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
f == Line(B, C)
g == parallel_line(A, f)
c == Circle(C, A, B)
D == projection(B, g)
h == Line(D, B)
E in g, c
F == midpoint(E, D)
i == parallel_line(A, h)
G == line_intersection(i, f)
H == midpoint(G, C)
I == midpoint(F, C)

Need to prove:
collinear(E, I, H)

Proof:
