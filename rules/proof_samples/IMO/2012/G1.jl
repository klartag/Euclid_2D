Assumptions:
A, B, C, J, M, K, L, F, G, S, T: Point
distinct(A, B, C, J, M, K, L, F, G, S, T)

J == excenter(A, B, C)
M == line_circle_tangent_point(Line(B, C), excircle(A, B, C))
K == line_circle_tangent_point(Line(A, B), excircle(A, B, C))
L == line_circle_tangent_point(Line(A, C), excircle(A, B, C))

F in Line(L, M), Line(B, J)
G in Line(K, M), Line(C, J)

S in Line(A, F), Line(B, C)
T in Line(A, G), Line(B, C)

Need to prove:
M == midpoint(S, T)

Proof:
