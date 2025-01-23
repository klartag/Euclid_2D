Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(C, A)
D == midpoint(B, C)
h == parallel_line(D, f)
c == Circle(D, B, A)
E in h, c
F in g, c
G == center(c)
H == midpoint(E, F)
i == Line(E, F)
d == Circle(F, B, C)
I in i, d

Need to prove:
concyclic(B, G, H, I)

Proof:
