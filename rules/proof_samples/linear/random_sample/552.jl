Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
h == Line(D, A)
E == projection(B, h)
i == Line(E, B)
F in i, c
G == center(c)
j == parallel_line(G, i)
H == line_intersection(g, j)
k == Line(D, F)
I == projection(A, k)

Need to prove:
collinear(A, H, I)

Proof:
