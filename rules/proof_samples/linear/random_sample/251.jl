Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(B, C)
I == midpoint(G, H)
J == midpoint(E, G)
c == Circle(I, G, J)
K == center(c)

Need to prove:
collinear(G, K, H)

Proof:
