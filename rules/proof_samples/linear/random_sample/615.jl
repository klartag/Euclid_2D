Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == projection(B, i)
c == Circle(C, A, B)
F in h, c
G == center(c)
H == midpoint(B, A)
d == Circle(D, E, C)
I in c, d

Need to prove:
concyclic(F, G, H, I)

Proof:
