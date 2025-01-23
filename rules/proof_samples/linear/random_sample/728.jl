Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
c == Circle(D, C, A)
E == midpoint(B, C)
j == Line(D, E)
F in j, c
G == midpoint(A, F)
H == center(c)
k == parallel_line(B, j)
I == projection(H, i)
d == Circle(E, G, F)
J in c, d
K in k, d

Need to prove:
concyclic(D, I, J, K)

Proof:
