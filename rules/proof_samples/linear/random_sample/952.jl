Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d, e, k: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d, e, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(A, B, D)
E in c
d == Circle(A, E, B)
F in g, d
G == midpoint(C, A)
e == Circle(C, G, F)
H == center(e)
k == Circle(G, A, D)
I in e, k

Need to prove:
concyclic(C, D, H, I)

Proof:
