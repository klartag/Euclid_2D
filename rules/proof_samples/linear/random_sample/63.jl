Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(C, F)
G == projection(E, i)
j == Line(E, G)
c == Circle(C, A, F)
d == Circle(D, C, E)
H == center(c)
I in j, d
J == midpoint(I, A)
K == midpoint(H, F)

Need to prove:
collinear(K, J, F)

Proof:
