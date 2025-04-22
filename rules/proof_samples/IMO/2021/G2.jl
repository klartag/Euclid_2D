Assumptions:
A, B, C, D, I, X, Y, Z, T: Point
c, w: Circle
distinct(A, B, C, D, I, X, Y, Z, T)

convex(A, B, C, D)

tangent(Line(A, B), c)
tangent(Line(B, C), c)
tangent(Line(C, D), c)
tangent(Line(D, A), c)
I == center(c)
identical(orientation(I, A, B), orientation(I, B, C), orientation(I, C, D), orientation(I, D, A))


w == Circle(A, C, I)

between(B, A, X)
between(B, C, Z)
X, Z in w

between(A, D, Y)
between(C, D, T)
Y, T in w

Need to prove:
distance(A, D) + distance(D, T) + distance(T, X) + distance(X, A) == distance(C, D) + distance(D, Y) + distance(Y, Z) + distance(Z, C) 

Proof:
