Assumptions:
A, B, C, D, E, F: Point
distinct(A, B, C, D, E, F)
concyclic(A, B, C, D)
E, F in Line(C, D)
angle(D, A, F) == angle(E, B, C) mod 360

Need to prove:
concyclic(A, B, E, F)

Proof:
By line_definition on F, E, Line(C, D) we get Line(C, D) == Line(E, F)
By line_definition on E, D, Line(C, D) we get Line(C, D) == Line(D, E)
By in_imply_collinear on E, C, D we get collinear(C, D, E)
By concyclic_definition_0 on C, A, B, D we get D in Circle(A, B, C)
By concyclic_definition_0 on B, D, C, A we get A in Circle(B, C, D)
By reverse_direction on B, C we get 180 == direction(B, C) - direction(C, B) mod 360
By reverse_direction on B, E we get 180 == direction(B, E) - direction(E, B) mod 360
By angles_on_chord on B, D, C, A, Circle(A, B, C) we get coangle(B, A, D) == coangle(B, C, D) mod 360
By in_imply_collinear on F, E, D we get collinear(D, E, F)
By not_in_line_equivalent_to_not_collinear_v0_r on B, D, C we get B not in Line(C, D)
By collinear_definition on E, C, D we get C in Line(D, E), D in Line(C, E), Line(C, E) == Line(D, E), 0 == 2 * angle(C, E, D) mod 360
By collinear_definition on D, E, C we get E in Line(C, D), C in Line(D, E), Line(C, D) == Line(D, E), 0 == 2 * angle(E, D, C) mod 360
By coangle_definition_v1 on B, C, D we get angle(B, C, D) == coangle(B, C, D) + orientation(B, C, D) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on B, F, E we get not_collinear(B, E, F), exists(Line(E, F))
By reverse_direction on E, D we get 180 == direction(E, D) - direction(D, E) mod 360
By reverse_direction on D, C we get 180 == direction(D, C) - direction(C, D) mod 360
By collinear_definition on E, F, D we get F in Line(D, E), D in Line(E, F), Line(D, E) == Line(E, F), 0 == 2 * angle(F, E, D) mod 360
By coangle_definition_v1 on B, A, D we get angle(B, A, D) == coangle(B, A, D) + orientation(B, A, D) mod 360
By divide_by_2_two_angles on F, E, B, F, A, B we get coangle(F, A, B) == coangle(F, E, B) mod 360
By concyclic_sufficient_conditions on F, E, B, A we get concyclic(A, B, E, F)
