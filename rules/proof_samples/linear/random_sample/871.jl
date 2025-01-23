Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D == midpoint(B, A)
E == midpoint(B, C)
F == center(c)
d == Circle(D, C, E)
G in c, d
H in f, d
I == midpoint(F, B)
J == projection(I, g)

Need to prove:
concyclic(G, H, I, J)

Proof:
