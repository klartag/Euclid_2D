Assumptions:
A, B, C, D, E, F, I, M, X, Y: Point
g: Circle
distinct(A, B, C, D, E, F, I, M, X, Y)

g == Circle(A, B, C)
I == incenter(A, B, C)
M == midpoint(B, C)
D == projection(I, Line(B, C))

between(A, F, B)
between(A, E, C)
E, F in perpendicular_line(I, Line(A, I))

X in Circle(A, E, F), g
Y in Line(D, X), Line(A, M)

Need to prove:
Y in g

Proof:
