Assumptions:
A, B, C, D, E, F: Point
f, g, h, i: Line
c: Circle
distinct(A, B, C, D, E, F)
distinct(f, g, h, i)
f == external_angle_bisector(C, A, B)
c == Circle(C, A, B)
D in f, c
g == external_angle_bisector(C, D, B)
E == center(c)
F == projection(C, g)
h == Line(C, F)
i == parallel_line(E, h)

Need to prove:
concurrent(f, g, i)

Proof:
