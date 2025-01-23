Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
F == line_intersection(g, i)
d == Circle(B, D, F)
e == Circle(E, A, C)
G in d, e
H == midpoint(G, E)

Need to prove:
false() # concyclic(C, D, G, H)

Proof:
