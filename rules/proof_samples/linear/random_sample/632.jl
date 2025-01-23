Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d, e)
f == Line(B, C)
D == midpoint(B, A)
c == Circle(C, B, D)
g == parallel_line(D, f)
E == midpoint(B, C)
d == Circle(C, D, E)
F == center(d)
G == projection(F, f)
e == Circle(A, B, E)
H in g, c
I in e, c

Need to prove:
concyclic(E, G, H, I)

Proof:
