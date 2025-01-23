Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == midpoint(B, A)
F == midpoint(A, E)
G == midpoint(B, E)
H == midpoint(G, A)
I == midpoint(F, B)

Need to prove:
concyclic(C, D, H, I)

Proof:
