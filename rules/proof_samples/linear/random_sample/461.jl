Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == internal_angle_bisector(C, A, B)
i == internal_angle_bisector(A, B, C)
D == line_intersection(h, i)
E == projection(D, g)
F == projection(D, f)
c == Circle(D, C, A)
G in i
d == Circle(G, D, F)
e == Circle(E, A, F)
H in d, e
I in g, c

Need to prove:
collinear(I, H, G)

Proof:
