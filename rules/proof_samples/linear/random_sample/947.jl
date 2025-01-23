Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(C, D, B)
E == projection(B, i)
F in i, c
d == Circle(E, B, D)
e == Circle(C, F, A)
G == center(e)
H == center(d)

Need to prove:
concyclic(A, E, G, H)

Proof:
