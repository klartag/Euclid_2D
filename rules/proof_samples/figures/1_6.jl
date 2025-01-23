Assumptions:
A, B, C, D: Point
distinct(A, B, C, D)
concyclic(A, B, C, D)
convex(A, B, D, C)
isosceles_triangle(D, B, C)

Need to prove:
angle(B, A, D) == angle(D, A, C) mod 360

Proof:
By orientations_are_cyclic on D, C, A we get orientation(C,A,D) == orientation(D,C,A) mod 360, orientation(A,D,C) == orientation(D,C,A) mod 360
By orientations_are_cyclic on A, B, D we get orientation(A,B,D) == orientation(B,D,A) mod 360, orientation(A,B,D) == orientation(D,A,B) mod 360
By orientations_are_cyclic on B, D, C we get orientation(B,D,C) == orientation(D,C,B) mod 360, orientation(B,D,C) == orientation(C,B,D) mod 360
By coangle_definition_v0 on D, A, B we get angle(D,A,B) == coangle(D,A,B) + orientation(D,A,B) mod 360
By concyclic_definition_0 on C, B, A, D we get D in Circle(A,B,C)
By coangle_definition_v0 on C, A, D we get angle(C,A,D) == coangle(C,A,D) + orientation(C,A,D) mod 360
By isosceles_triangle_properties on D, C, B we get distance(B,D) == distance(C,D), angle(C,B,D) == angle(D,C,B) mod 360, orientation(D,C,B) == angle(D,C,B) + halfangle(B,D,C) mod 360
By angles_on_chord on C, D, B, A, Circle(A,B,C) we get coangle(C,A,D) == coangle(C,B,D) mod 360
By angles_on_chord on D, B, A, C, Circle(A,B,C) we get coangle(D,A,B) == coangle(D,C,B) mod 360
By coangle_definition_v0 on D, C, B we get angle(D,C,B) == coangle(D,C,B) + orientation(D,C,B) mod 360
By coangle_definition_v0 on C, B, D we get angle(C,B,D) == coangle(C,B,D) + orientation(C,B,D) mod 360
