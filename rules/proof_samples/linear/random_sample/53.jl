Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
distinct(c, d, e)
f == Line(C, A)
D == midpoint(B, C)
c == Circle(A, B, D)
d == Circle(C, D, A)
e == Circle(C, A, B)
E == center(e)
F in f, c
G == midpoint(D, C)
H == center(d)
g == Line(H, E)
I == line_intersection(f, g)

Need to prove:
concyclic(B, F, G, I)

Proof:
