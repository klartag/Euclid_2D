Assumptions:
A, B, C, D, E, F, G, H, I, J, K, L: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K, L)
distinct(f, g, h, i, j)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, A)
H == midpoint(F, C)
I == midpoint(C, A)
J == midpoint(B, A)
c == Circle(I, G, J)
j == Line(J, H)
K == center(c)
L == midpoint(H, K)

Need to prove:
L in j

Proof:
