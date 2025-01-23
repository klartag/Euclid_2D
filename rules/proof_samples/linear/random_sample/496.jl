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
E == midpoint(A, D)
F == midpoint(B, C)
G == projection(E, h)
H == projection(F, f)
c == Circle(H, D, F)
I in h, c
J in f, c

Need to prove:
concyclic(B, G, I, J)

Proof:
