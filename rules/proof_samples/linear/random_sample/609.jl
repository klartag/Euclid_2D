Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
F == center(c)
j == internal_angle_bisector(E, D, C)
k == internal_angle_bisector(A, E, B)
G == line_intersection(j, k)
H in f
l == external_angle_bisector(D, A, H)
I in l, c

Need to prove:
concyclic(D, F, G, I)

Proof:
