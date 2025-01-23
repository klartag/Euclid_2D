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
c == Circle(C, D, B)
E == midpoint(C, A)
F == projection(D, f)
d == Circle(B, E, F)
G in d, c
H in i, c
I == midpoint(B, H)

Need to prove:
concyclic(E, G, H, I)

Proof:
