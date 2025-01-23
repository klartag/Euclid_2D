Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
k == Line(C, F)
G == line_intersection(i, j)
c == Circle(C, A, B)
H in k, c
d == Circle(H, G, E)
I in k, d
J in c
e == Circle(D, I, J)
K in c, e

Need to prove:
false() # concyclic(E, F, H, K)

Proof:
