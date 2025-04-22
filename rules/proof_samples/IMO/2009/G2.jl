Assumptions:
A, B, C, O, P, Q: Point
k: Circle
distinct(A, B, C, O, P, Q)

O == circumcenter(A, B, C)

between(A, P, C)
between(A, Q, B)

midpoint(B, P), midpoint(C, Q), midpoint(P, Q) in k

tangent(Line(P, Q), k)

Need to prove:
distance(O, P) == distance(O, Q)

Proof:
