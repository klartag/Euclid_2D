Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == projection(C, i)
j == Line(C, E)
c == Circle(C, B, E)
F in f, c
G == center(c)
H == projection(G, f)
k == Line(G, H)
d == Circle(F, D, A)
I == line_intersection(k, j)
J in d, c

Need to prove:
concyclic(F, H, I, J)

Proof:
