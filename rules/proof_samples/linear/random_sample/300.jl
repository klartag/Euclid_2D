Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == midpoint(B, A)
F == projection(E, i)
G == midpoint(E, A)
d == Circle(F, B, G)
H in i, d

Need to prove:
H in g

Proof:
