Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
F == midpoint(E, B)
G == projection(F, f)
H == center(c)
j == Line(E, H)
d == Circle(H, G, A)
I in c, d
J == line_intersection(j, f)

Need to prove:
concyclic(D, E, I, J)

Proof:
