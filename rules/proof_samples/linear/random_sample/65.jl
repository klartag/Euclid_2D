Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d, e)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == center(c)
d == Circle(A, E, D)
e == Circle(C, E, B)
F == center(d)
G == center(e)
H == midpoint(D, G)
I == midpoint(C, F)

Need to prove:
concyclic(A, B, H, I)

Proof:
