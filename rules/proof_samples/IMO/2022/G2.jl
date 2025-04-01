Assumptions:
A, B, C, D, E, F, P, X, Y: Point
distinct(A, B, C, D, E, F, P, X, Y)

angle(A, B, C) < 90
angle(B, C, A) < 90
angle(C, A, B) < 90

F == projection(A, Line(B, C))
between(A, P, F)

D in parallel_line(P, Line(A, C)), Line(B, C)
E in parallel_line(P, Line(A, B)), Line(B, C)

X in Circle(A, B, D)
Y in Circle(A, C, E)
distance(D, A) == distance(D, X)
distance(E, A) == distance(E, Y)

Need to prove:
concyclic(B, C, X, Y)

Proof:
