Assumptions:
A, B, C, D, E, F: Point
f, g: Line
c, d, e: Circle
distinct(A, B, C, D, E, F)
distinct(f, g)
distinct(c, d, e)
f == Line(B, A)
c == Circle(C, A, B)
D == center(c)
d == Circle(A, C, D)
e == Circle(B, C, D)
E == center(e)
g == Line(E, D)
F in f, d

Need to prove:
F in g

Proof:
By circle_radius_v0_r on B, c we get radius(c) == distance(B, center(c))
By circle_radius_v0_r on C, e we get radius(e) == distance(C, center(e))
By circle_radius_v0_r on C, c we get radius(c) == distance(C, center(c))
By circle_radius_v0_r on B, e we get radius(e) == distance(B, center(e))
By circle_radius_v0_r on D, e we get radius(e) == distance(D, center(e))
By angles_on_chord on F, C, D, A, d we get coangle(F, A, C) == coangle(F, D, C) mod 360
By in_imply_collinear on F, B, A we get collinear(A, B, F)
By angle_to_center on B, C, D, e we get coangle(B, C, D) == halfangle(B, center(e), D) - orientation(B, center(e), D) mod 360
By angle_to_center on B, A, C, c we get coangle(B, A, C) == halfangle(B, center(c), C) - orientation(B, center(c), C) mod 360
By angle_to_center on C, B, D, e we get coangle(C, B, D) == halfangle(C, center(e), D) - orientation(C, center(e), D) mod 360
By reverse_orientation on B, D, C we get orientation(B, D, C) == 0 - orientation(C, D, B) mod 360
By orientations_are_cyclic on C, E, D we get orientation(C, E, D) == orientation(E, D, C) mod 360, orientation(C, E, D) == orientation(D, C, E) mod 360
By orientations_are_cyclic on C, D, B we get orientation(C, D, B) == orientation(D, B, C) mod 360, orientation(B, C, D) == orientation(C, D, B) mod 360
By orientations_are_cyclic on B, E, D we get orientation(B, E, D) == orientation(E, D, B) mod 360, orientation(B, E, D) == orientation(D, B, E) mod 360
By orientations_are_cyclic on B, D, C we get orientation(B, D, C) == orientation(D, C, B) mod 360, orientation(B, D, C) == orientation(C, B, D) mod 360
By coangle_definition_v1 on F, D, C we get angle(F, D, C) == coangle(F, D, C) + orientation(F, D, C) mod 360
By reverse_direction on D, C we get 180 == direction(D, C) - direction(C, D) mod 360
By coangle_definition_v1 on F, A, C we get angle(F, A, C) == coangle(F, A, C) + orientation(F, A, C) mod 360
By collinear_definition on A, B, F we get B in Line(A, F), F in Line(A, B), Line(A, B) == Line(A, F), 0 == 2 * angle(B, A, F) mod 360
By coangle_definition_v1 on B, A, C we get angle(B, A, C) == coangle(B, A, C) + orientation(B, A, C) mod 360
By coangle_definition_v1 on C, B, D we get angle(C, B, D) == coangle(C, B, D) + orientation(C, B, D) mod 360
By coangle_definition_v1 on B, C, D we get angle(B, C, D) == coangle(B, C, D) + orientation(B, C, D) mod 360
By isosceles_triangle_properties on E, D, B we get distance(B, E) == distance(D, E), angle(D, B, E) == angle(E, D, B) mod 360, orientation(E, D, B) == angle(E, D, B) + halfangle(B, E, D) mod 360
By perpendicular_bisector_sufficient_conditions on B, C, E, D we get Line(D, E) == perpendicular_bisector(B, C)
By isosceles_triangle_properties on E, D, C we get distance(C, E) == distance(D, E), angle(D, C, E) == angle(E, D, C) mod 360, orientation(E, D, C) == angle(E, D, C) + halfangle(C, E, D) mod 360
By sas_anti_congruence on C, D, B, B, D, C we get anti_congruent_triangles(B, C, D, C, B, D)
By perpendicular_line_definition on D, g, Line(B, C) we get g == perpendicular_line(D, Line(B, C))
By perpendicular_direction_conditions_v0 on C, B, D, F we get perpendicular(Line(B, C), Line(D, F))
By perpendicular_line_definition on D, Line(D, F), Line(B, C) we get Line(D, F) == perpendicular_line(D, Line(B, C))
