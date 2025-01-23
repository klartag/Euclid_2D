Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
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
c == Circle(B, F, D)
H == center(c)
d == Circle(A, G, F)
I == center(d)
e == Circle(E, D, B)
J == center(e)

Need to prove:
concyclic(D, H, I, J)

Proof:
