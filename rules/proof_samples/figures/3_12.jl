Assumptions:
A, B, C, D, E, F, P: Point
distinct(A, B, C, D, E, F, P)
P in Circle(A, B, C)
D == projection(P, Line(B, C))
E == projection(P, Line(A, C))
F == projection(P, Line(A, B))

Need to prove:
collinear(D, E, F)

Proof:
By line_definition on C, D, Line(B, C) we get Line(B, C) == Line(C, D)
By line_definition on P, E, perpendicular_line(P, Line(A, C)) we get Line(E, P) == perpendicular_line(P, Line(A, C))
By line_definition on C, E, Line(A, C) we get Line(A, C) == Line(C, E)
By line_definition on P, F, perpendicular_line(P, Line(A, B)) we get Line(F, P) == perpendicular_line(P, Line(A, B))
By line_definition on E, A, Line(A, C) we get Line(A, C) == Line(A, E)
By line_definition on A, F, Line(A, B) we get Line(A, B) == Line(A, F)
By line_definition on D, P, perpendicular_line(P, Line(B, C)) we get Line(D, P) == perpendicular_line(P, Line(B, C))
By circle_definition on C, P, B, Circle(A, B, C) we get Circle(A, B, C) == Circle(B, C, P)
By circle_definition on B, P, A, Circle(A, B, C) we get Circle(A, B, C) == Circle(A, B, P)
By angles_on_chord on B, P, C, A, Circle(A, B, C) we get coangle(B, A, P) == coangle(B, C, P) mod 360
By in_imply_collinear on F, A, B we get collinear(A, B, F)
By in_imply_collinear on D, B, C we get collinear(B, C, D)
By not_in_line_equivalent_to_not_collinear_v0_r on P, B, A we get P not in Line(A, B)
By not_in_line_equivalent_to_not_collinear_v0_r on P, B, C we get P not in Line(B, C)
By perpendicular_angle_conditions_v0 on C, E, P we get 0 == coangle(C, E, P) mod 360
By perpendicular_angle_conditions_v0 on C, D, P we get 0 == coangle(C, D, P) mod 360
By perpendicular_angle_conditions_v0 on A, F, P we get 0 == coangle(A, F, P) mod 360
By perpendicular_angle_conditions_v0 on A, E, P we get 0 == coangle(A, E, P) mod 360
By same_angle on C, B, D, P we get coangle(B, C, P) == coangle(D, C, P) mod 360
By same_angle on A, B, F, P we get coangle(B, A, P) == coangle(F, A, P) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on P, F, A we get not_collinear(A, F, P), exists(Line(A, F))
By not_in_line_equivalent_to_not_collinear_v0 on P, C, D we get not_collinear(C, D, P), exists(Line(C, D))
By concyclic_sufficient_conditions on A, F, P, E we get concyclic(A, E, F, P)
By concyclic_sufficient_conditions on C, D, P, E we get concyclic(C, D, E, P)
By concyclic_definition_0 on C, D, E, P we get P in Circle(C, D, E)
By concyclic_definition_0 on E, F, A, P we get P in Circle(A, E, F)
By angles_on_chord on D, P, C, E, Circle(C, D, E) we get coangle(D, C, P) == coangle(D, E, P) mod 360
By angles_on_chord on F, P, E, A, Circle(A, E, F) we get coangle(F, A, P) == coangle(F, E, P) mod 360
By same_angle_converse on E, D, F, P we get collinear(D, E, F)
