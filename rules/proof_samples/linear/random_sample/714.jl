Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == center(c)
F == midpoint(D, A)
G == midpoint(C, A)
d == Circle(F, E, G)
H == center(d)
I == midpoint(B, E)

Need to prove:
concyclic(C, D, H, I)

Proof:
