Assumptions:
A, B, C, D, E: Point
distinct(A, B, C, D, E)

convex(A, B, C, D, E)

identical(distance(A, B), distance(B, C), distance(C, D))
angle(E, A, B) == angle(B, C, D) mod 360
angle(E, D, C) == angle(C, B, A) mod 360

Need to prove:
concurrent(altitude(E, Line(B, C)), Line(A, C), Line(B, D))

Proof: