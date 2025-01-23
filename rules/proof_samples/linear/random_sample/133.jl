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
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
F == midpoint(B, C)
d == Circle(B, E, F)
G == line_intersection(g, i)
H == center(d)
I == midpoint(G, B)
J in f, d

Need to prove:
concyclic(F, H, I, J)

Proof:
