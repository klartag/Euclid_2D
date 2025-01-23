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
E in h, c
F in g, c
d == Circle(F, E, C)
H == center(d)
e == Circle(F, A, B)
k == Circle(G, F, H)
I in k, e

Need to prove:
false() # concyclic(C, D, H, I)

Proof:
