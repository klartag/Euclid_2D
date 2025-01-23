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
c == Circle(C, D, B)
E == midpoint(B, A)
j == Line(D, E)
F in f, c
G == projection(B, i)
k == Line(G, B)
H == line_intersection(j, k)
l == Line(F, G)
I in l, c

Need to prove:
collinear(C, H, I)

Proof:
