Assumptions:
A, B, C, D: Point
distinct(A, B, C, D)
concyclic(A, B, C, D)
convex(A, B, C, D)

Need to prove:
angle(A, B, C) + angle(C, D, A) == 180 mod 360

Proof:
By concyclic_definition_0 on A, C, B, D we get D in Circle(A,B,C)
By coangle_definition_v0 on C, B, A we get angle(C,B,A) == coangle(C,B,A) + orientation(C,B,A) mod 360
By coangle_definition_v0 on C, D, A we get angle(C,D,A) == coangle(C,D,A) + orientation(C,D,A) mod 360
By angles_on_chord on C, A, D, B, Circle(A,B,C) we get coangle(C,B,A) == coangle(C,D,A) mod 360
By reverse_orientation on A, B, C we get orientation(A,B,C) == 0 - orientation(C,B,A) mod 360
