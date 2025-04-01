Assumptions:
A, B, C, M, N, T, X, Y, K: Point
w: Circle

distinct(A, B, C, M, N, T, X, Y, K)

w == Circle(A, B, C)

M == midpoint(A, B)
N == midpoint(A, C)

T in w, perpendicular_bisector(B, C)
convex(B, T, C, A)

X in Circle(A, M, T), perpendicular_bisector(A, C)
Y in Circle(A, N, T), perpendicular_bisector(A, B)

identical(orientation(X, A, B), orientation(X, B, C), orientation(X, C, A))
identical(orientation(Y, A, B), orientation(Y, B, C), orientation(Y, C, A))

K in Line(M, N), Line(X, Y)

Need to prove:
distance(K, A) == distance(K, T)

Proof:
