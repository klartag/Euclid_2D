Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
f == Line(B, A)
D == projection(C, f)
E == midpoint(C, A)
F == midpoint(D, A)
c == Circle(F, A, E)
G == center(c)
H == midpoint(E, B)
g == Line(E, B)
I in g, c

Need to prove:
concyclic(F, G, H, I)

Proof:
