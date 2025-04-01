Assumptions:
A, B, C, M, X0, T0, X1, T1: Point
distinct(A, B, C, M, X0, T0, X1, T1)

isosceles_triangle(A, B, C)

M == midpoint(B, C)

X0 in Circle(A, B, M)
convex(A, X0, M, B)
perpendicular(Line(T0, M), Line(M, X0))
distance(T0, X0) == distance(B, X0)
identical(orientation(B, M, A), orientation(B, M, T0), orientation(T0, M, A))

X1 in Circle(A, B, M)
convex(A, X1, M, B)
perpendicular(Line(T1, M), Line(M, X1))
distance(T1, X1) == distance(B, X1)
identical(orientation(B, M, A), orientation(B, M, T1), orientation(T1, M, A))

Need to prove:
angle(M, T0, B) - angle(C, T0, M) == angle(M, T1, B) - angle(C, T1, M) mod 360

Proof:
