Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
c == Circle(C, A, F)
H == center(c)
d == Circle(E, F, H)
I == midpoint(D, G)
J in j, d
e == Circle(A, J, I)
K in d, e

Need to prove:
false() # collinear(F, K, E)

Proof:
