Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
F == projection(E, h)
d == Circle(A, B, D)
G == projection(A, h)
H == center(d)
I == projection(H, f)
e == Circle(F, E, C)
J in d, e

Need to prove:
concyclic(A, G, I, J)

Proof:
