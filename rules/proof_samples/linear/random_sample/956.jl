Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
c == Circle(G, A, B)
H == center(c)
d == Circle(E, D, B)
k == parallel_line(C, j)
I == center(d)
e == Circle(E, F, C)
J == line_intersection(f, k)
K == center(e)

Need to prove:
concyclic(H, I, J, K)

Proof:
