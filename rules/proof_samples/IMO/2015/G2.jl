Assumptions:
A, B, C, D, E, F, G, K, L, O, X: Point
g, w: Circle

distinct(A, B, C, D, E, F, G, K, L, O, X)

w == Circle(A, B, C)
O == center(w)

center(g) == A
D, E in g, Line(B, C)
between(B, D, E, C)

F, G in g, w
convex(A, F, B, C)
convex(A, G, C, B)

K in Circle(B, D, F)
between(A, K, B)

L in Circle(C, E, G)
between(A, L, C)

Line(F, K) != Line(G, L)
X in Line(F, K), Line(G, L)

Need to prove:
collinear(A, X, O)

Proof:
