Assumptions:
A, B, C, D, E, F, O: Point
distinct(A, B, C, D, E, F, O)
not_collinear(A, B, C)
collinear(A, B, F)
collinear(B, C, D)
collinear(A, C, E)
concyclic(A, E, F, O)
concyclic(B, D, F, O)

Need to prove:
concyclic(C, D, E, O)

Proof:
By concyclic_definition_0 on O, B, F, D we get D in Circle(B, F, O)
By concyclic_definition_0 on B, F, D, O we get O in Circle(B, D, F)
By concyclic_definition_0 on D, B, O, F we get F in Circle(B, D, O)
By concyclic_definition_0 on E, A, O, F we get F in Circle(A, E, O)
By concyclic_definition_0 on E, A, F, O we get O in Circle(A, E, F)
By collinear_definition on D, B, C we get B in Line(C, D), C in Line(B, D), Line(B, D) == Line(C, D), 0 == 2 * angle(B, D, C) mod 360
By angles_on_chord on A, O, F, E, Circle(A, E, F) we get coangle(A, E, O) == coangle(A, F, O) mod 360
By angles_on_chord on B, O, D, F, Circle(B, D, F) we get coangle(B, D, O) == coangle(B, F, O) mod 360
By not_in_line_equivalent_to_not_collinear_v0_r on O, B, D we get O not in Line(B, D)
By not_in_line_equivalent_to_not_collinear_v0 on O, D, C we get not_collinear(C, D, O), exists(Line(C, D))
By same_angle on F, B, A, O we get coangle(A, F, O) == coangle(B, F, O) mod 360
By same_angle on E, A, C, O we get coangle(A, E, O) == coangle(C, E, O) mod 360
By same_angle on D, B, C, O we get coangle(B, D, O) == coangle(C, D, O) mod 360
By concyclic_sufficient_conditions on C, D, O, E we get concyclic(C, D, E, O)
