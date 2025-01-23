Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == center(c)
F == projection(E, f)
i == Line(E, F)
G == midpoint(D, C)
H == line_intersection(h, i)
d == Circle(G, H, D)
I in d, c

Need to prove:
concyclic(B, F, G, I)

Proof:
