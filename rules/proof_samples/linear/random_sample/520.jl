Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == midpoint(B, A)
F in f
G == midpoint(E, F)
H == projection(G, i)
I == line_intersection(g, i)

Need to prove:
concyclic(E, G, H, I)

Proof:
