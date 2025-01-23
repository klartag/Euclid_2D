Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(F, B)
I == midpoint(F, C)
c == Circle(C, I, H)
J in f, c
d == Circle(A, F, B)
K == center(d)

Need to prove:
concyclic(D, G, J, K)

Proof:
