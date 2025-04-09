Assumptions:
A, B, C, D, E, O: Point
distinct(A, B, C, D, E)
convex(A, B, C, D, E)

angle(A, B, C) == 90 mod 360
angle(D, E, A) == 90 mod 360
midpoint(C, D) == circumcenter(A, B, E)
O == circumcenter(A, C, D)

Need to prove:
collinear(A, O, midpoint(B, E))

Proof:
