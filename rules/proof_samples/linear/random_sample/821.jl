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
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
d == Circle(E, B, D)
F in h, d
G == center(c)
H == projection(F, g)
I == projection(E, f)

Need to prove:
concyclic(B, G, H, I)

Proof:
