Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, C)
H == midpoint(B, C)
I == midpoint(C, A)
J == midpoint(B, A)
c == Circle(G, H, K)
d == Circle(J, H, I)
L in c, d

Need to prove:
false() # concyclic(B, D, G, L)

Proof:
