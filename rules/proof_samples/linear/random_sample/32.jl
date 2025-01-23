Assumptions:
A, B, C, D, E: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E)
distinct(f, g, h, i)
f == Line(B, C)
g == parallel_line(A, f)
c == Circle(C, A, B)
D in g, c
h == external_angle_bisector(D, C, A)
i == internal_angle_bisector(C, A, B)
E == line_intersection(h, i)

Need to prove:
E in c

Proof:
