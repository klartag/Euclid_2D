Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(B, D)
F == midpoint(C, E)
G == projection(C, f)
j == Line(C, G)
c == Circle(A, F, G)
H in j, c
k == Line(H, F)
I == line_intersection(k, f)

Need to prove:
concyclic(A, E, H, I)

Proof:
