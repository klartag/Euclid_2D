Assumptions:
A, B, C, M, P, X, Y: Point
distinct(A, B, C, M, P, X, Y)

isosceles_triangle(A, B, C)
M == midpoint(B, C)

distance(P, B) < distance(P, C)
parallel(Line(P, A), Line(B, C))

X in Line(P, B)
Y in Line(P, C)
between(P, B, X)
between(P, C, Y)
angle(P, X, M) == angle(P, Y, M) mod 360

Need to prove:
concyclic(A, P, X, Y)

Proof:
