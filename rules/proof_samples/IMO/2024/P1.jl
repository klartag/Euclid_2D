Assumptions:
A, B, C, I, X, Y, P, K, L: Point
lx, ly: Line
w: Circle
distinct(A, B, C, I, X, Y, P, K, L)

I == incenter(A, B, C)
w == incircle(A, B, C)

X in Line(B, C)
lx == parallel_line(X, Line(A, C))
tangent(lx, w)

Y in Line(B, C)
ly == parallel_line(Y, Line(A, B))
tangent(ly, w)

P in Line(A, I), Circle(A, B, C)

K == midpoint(A, C)
L == midpoint(A, B)

Need to prove:
angle(K, I, L) + angle(Y, P, X) == 180 mod 360

Proof:
