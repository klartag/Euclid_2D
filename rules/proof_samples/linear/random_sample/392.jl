Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
c, d, e, k: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
distinct(c, d, e, k)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == center(c)
d == Circle(B, E, D)
F == projection(A, g)
e == Circle(C, A, E)
G in d, e
H == midpoint(D, C)
k == Circle(H, C, G)
I in h, k

Need to prove:
concyclic(A, C, F, I)

Proof:
