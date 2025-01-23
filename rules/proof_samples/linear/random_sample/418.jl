Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(C, A)
g == internal_angle_bisector(C, A, B)
c == Circle(C, A, B)
D in g, c
d == Circle(B, C, D)
E == projection(D, f)
h == Line(E, D)
F in h, d
i == Line(A, F)
j == Line(B, F)
G == projection(D, i)
k == Line(D, G)

Need to prove:
concurrent(f, j, k)

Proof:
