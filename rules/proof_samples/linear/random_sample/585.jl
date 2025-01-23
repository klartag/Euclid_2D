Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
c, d, e, k: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
distinct(c, d, e, k)
A in c
B in c
C in c
f == Line(B, C)
D == center(c)
g == parallel_line(D, f)
d == Circle(A, B, D)
E == projection(D, f)
h == Line(E, D)
e == Circle(E, A, C)
F in h, e
G in g, d
k == Circle(F, D, G)
H == center(d)
I == center(k)

Need to prove:
concyclic(A, D, H, I)

Proof:
