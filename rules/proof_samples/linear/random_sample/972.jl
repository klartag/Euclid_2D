Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(C, D, B)
E in c
F == midpoint(D, E)
G == midpoint(C, A)
H == center(c)
I in c
J == midpoint(I, D)

Need to prove:
concyclic(F, G, H, J)

Proof:
