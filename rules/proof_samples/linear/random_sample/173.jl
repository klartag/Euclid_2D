Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k)
f == Line(B, A)
g == external_angle_bisector(C, A, B)
D == midpoint(C, A)
E == midpoint(D, B)
h == internal_angle_bisector(D, A, B)
i == parallel_line(E, f)
F == projection(E, g)
j == Line(F, E)
G == projection(D, j)
k == Line(G, D)

Need to prove:
concurrent(h, i, k)

Proof:
