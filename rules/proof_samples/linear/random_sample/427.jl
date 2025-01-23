Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
distinct(c, d)
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
c == Circle(I, G, A)
d == Circle(H, I, E)
J in d, c

Need to prove:
false() # collinear(B, J, E)

Proof:
