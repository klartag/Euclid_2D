Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == Line(C, A)
k == Line(B, D)
E == midpoint(D, C)
c == Circle(B, D, E)
l == parallel_line(E, i)
F in l, c
G == line_intersection(j, k)
H == midpoint(B, G)
I == midpoint(G, F)

Need to prove:
concyclic(D, E, H, I)

Proof:
