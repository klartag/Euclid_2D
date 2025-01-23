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
j == Line(E, A)
c == Circle(C, D, B)
F == projection(D, f)
k == Line(F, D)
G in j, c
H in k, c
I == projection(H, i)

Need to prove:
concyclic(A, F, G, I)

Proof:
