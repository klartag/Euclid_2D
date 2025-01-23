Assumptions:
A, B, C, D: Point
distinct(A, B, C, D)
tangent(Line(C, D), Circle(A, B, C))
convex(A, B, C, D)

Need to prove:
angle(A, B, C) == angle(A, C, D) mod 360

Proof:
By orientations_are_cyclic on C, D, A we get orientation(C,D,A) == orientation(D,A,C) mod 360, orientation(A,C,D) == orientation(C,D,A) mod 360
By coangle_definition_v0 on A, B, C we get angle(A,B,C) == coangle(A,B,C) + orientation(A,B,C) mod 360
By coangle_definition_v0 on A, C, D we get angle(A,C,D) == coangle(A,C,D) + orientation(A,C,D) mod 360
By tangent_chord_angle_v0 on C, A, B, D we get coangle(A,B,C) == coangle(A,C,D) mod 360
