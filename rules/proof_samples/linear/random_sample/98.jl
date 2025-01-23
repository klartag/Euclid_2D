Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
E == midpoint(B, D)
d == Circle(E, A, D)
i == parallel_line(E, g)
F in i, d
G == line_intersection(i, h)
H == center(c)

Need to prove:
concyclic(A, F, G, H)

Proof:
