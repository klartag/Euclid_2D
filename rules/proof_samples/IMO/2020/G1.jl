Assumptions:
A, B, C, D, E, F, P, Q: Point
distinct(A, B, C, D, E, F, P, Q)

isosceles_triangle(C, A, B)
between(A, D, B)
distance(A, D) < distance(D, B)

between(B, P, C)
between(C, Q, A)

perpendicular(Line(D, P), Line(P, B))
perpendicular(Line(D, Q), Line(Q, A))

E in perpendicular_bisector(P, Q)
between(C, E, Q)

F in Circle(A, B, C), Circle(C, P, Q)

collinear(P, E, F)

Need to prove:
perpendicular(Line(A, C), Line(B, C))

Proof:
