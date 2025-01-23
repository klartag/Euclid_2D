Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
G == midpoint(F, B)
H == midpoint(B, C)
I == midpoint(C, A)
J == midpoint(B, A)
c == Circle(D, J, I)
j == Line(G, H)
K in j, c

Need to prove:
false() # collinear(E, G, K)

Proof:
