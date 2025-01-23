Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h: Line
c, d, e, k: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h)
distinct(c, d, e, k)
f == Line(B, A)
g == Line(B, C)
c == Circle(C, A, B)
D == center(c)
E == projection(C, f)
F == projection(D, f)
h == Line(F, D)
G == line_intersection(h, g)
d == Circle(G, A, F)
H in d, c
e == Circle(E, C, A)
k == Circle(H, E, F)
I in e, k

Need to prove:
false() # concyclic(C, E, G, I)

Proof:
