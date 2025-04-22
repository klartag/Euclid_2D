Assumptions:
A, B, C, D, P, Q: Point
distinct(A, B, C, D, P, Q)
convex(A, B, C, D)

identical(orientation(P, A, B), orientation(P, B, C), orientation(P, C, D), orientation(P, D, A))

angle(P, B, A) == 2 * angle(P, A, D) mod 360
angle(D, P, A) == 3 * angle(P, A, D) mod 360
angle(B, A, P) == 2 * angle(C, B, P) mod 360
angle(B, P, C) == 3 * angle(C, B, P) mod 360



Q == line_intersection(internal_angle_bisector(A, D, P), internal_angle_bisector(P, C, B))

identical(orientation(Q, A, B), orientation(Q, B, C), orientation(Q, C, A))

Need to prove:
distance(A, Q) == distance(B, Q)

Proof:
