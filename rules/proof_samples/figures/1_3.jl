Assumptions:
A, B, C, D: Point
distinct(A, B, C, D)
concyclic(A, B, C, D)
convex(A, B, C, D)

Need to prove:
angle(A, C, B) == angle(A, D, B) mod 360

Proof:
By orientations_are_cyclic on D, A, B we get orientation(A,B,D) == orientation(D,A,B) mod 360, orientation(B,D,A) == orientation(D,A,B) mod 360
By orientations_are_cyclic on A, B, C we get orientation(A,B,C) == orientation(B,C,A) mod 360, orientation(A,B,C) == orientation(C,A,B) mod 360
By concyclic_definition_0 on C, A, B, D we get D in Circle(A,B,C)
By coangle_definition_v0 on B, D, A we get angle(B,D,A) == coangle(B,D,A) + orientation(B,D,A) mod 360
By coangle_definition_v0 on B, C, A we get angle(B,C,A) == coangle(B,C,A) + orientation(B,C,A) mod 360
By angles_on_chord on B, A, D, C, Circle(A,B,C) we get coangle(B,C,A) == coangle(B,D,A) mod 360
