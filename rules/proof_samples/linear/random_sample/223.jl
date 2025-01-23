Assumptions:
A, B, C, D, E: Point
f, g, h: Line
c: Circle
distinct(A, B, C, D, E)
distinct(f, g, h)
A in c
B in c
B in f # (defining f)
g == Line(A, B)
C == center(c)
D == projection(C, g)
h == Line(C, D)
E == line_intersection(h, f)

Need to prove:
E in c

Proof:
