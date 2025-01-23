Assumptions:
A, B, C, D, E, F, G: Point
f, g: Line
c: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g)
f == Line(B, A)
D == midpoint(C, A)
g == parallel_line(C, f)
c == Circle(A, B, D)
E == center(c)
F == projection(E, g)
G == midpoint(B, C)

Need to prove:
concyclic(C, D, F, G)

Proof:
