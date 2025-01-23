Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
f == Line(B, A)
g == Line(C, A)
D == projection(B, g)
E == projection(C, f)
F == midpoint(B, A)
G == midpoint(D, B)
H == midpoint(D, E)
c == Circle(E, C, F)
I in g, c

Need to prove:
collinear(I, H, G)

Proof:
