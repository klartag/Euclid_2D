Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
distinct(c, d)
A in c
B in c
C in c
f == Line(A, B)
D == midpoint(C, A)
g == Line(C, A)
E == center(c)
d == Circle(E, D, A)
F == midpoint(C, D)
G == midpoint(F, D)
H in f, d
I == midpoint(B, G)
h == parallel_line(I, g)

Need to prove:
H in h

Proof:
