Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d, e: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d, e)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == center(c)
F == midpoint(A, D)
G == line_intersection(g, i)
d == Circle(F, D, C)
e == Circle(G, F, E)
H in e, d

Need to prove:
collinear(G, H, C)

Proof:
By line_definition on D, C, h we get h == Line(C, D)
By line_definition on D, G, i we get i == Line(D, G)
By circle_definition on F, H, G, e we get e == Circle(F, G, H)
By circle_definition on E, F, H, e we get e == Circle(E, F, H)
By circle_definition on F, H, D, d we get d == Circle(D, F, H)
By circle_radius_v0_r on B, c we get radius(c) == distance(B, center(c))
By circle_radius_v0_r on D, c we get radius(c) == distance(D, center(c))
By circle_radius_v0_r on A, c we get radius(c) == distance(A, center(c))
By angles_on_chord on F, G, E, H, e we get coangle(F, E, G) == coangle(F, H, G) mod 360
By angles_on_chord on C, F, D, H, d we get coangle(C, D, F) == coangle(C, H, F) mod 360
By angles_on_chord on G, H, E, F, e we get coangle(G, E, H) == coangle(G, F, H) mod 360
By angles_on_chord on D, H, F, C, d we get coangle(D, C, H) == coangle(D, F, H) mod 360
By angles_on_chord on E, H, F, G, e we get coangle(E, F, H) == coangle(E, G, H) mod 360
By angles_on_chord on F, H, C, D, d we get coangle(F, C, H) == coangle(F, D, H) mod 360
By angles_on_chord on D, C, F, H, d we get coangle(D, F, C) == coangle(D, H, C) mod 360
By angles_on_chord on F, H, G, E, e we get coangle(F, E, H) == coangle(F, G, H) mod 360
By angles_on_chord on C, D, F, H, d we get coangle(C, F, D) == coangle(C, H, D) mod 360
By angles_on_chord on H, F, E, G, e we get coangle(H, E, F) == coangle(H, G, F) mod 360
By angles_on_chord on B, D, C, A, c we get coangle(B, A, D) == coangle(B, C, D) mod 360
By angles_on_chord on D, B, A, C, c we get coangle(D, A, B) == coangle(D, C, B) mod 360
By in_imply_collinear on G, D, A we get collinear(A, D, G)
By in_imply_concyclic on A, B, C, D we get concyclic(A, B, C, D)
By angle_to_center on C, D, A, c we get coangle(C, D, A) == halfangle(C, center(c), A) - orientation(C, center(c), A) mod 360
By angle_to_center on B, C, D, c we get coangle(B, C, D) == halfangle(B, center(c), D) - orientation(B, center(c), D) mod 360
By angle_to_center on A, D, C, c we get coangle(A, D, C) == halfangle(A, center(c), C) - orientation(A, center(c), C) mod 360
By angle_to_center on D, C, B, c we get coangle(D, C, B) == halfangle(D, center(c), B) - orientation(D, center(c), B) mod 360
By collinear_definition on D, A, F we get A in Line(D, F), F in Line(A, D), Line(A, D) == Line(D, F), 0 == 2 * angle(A, D, F) mod 360
By isosceles_triangle_properties on F, D, A we get distance(A, F) == distance(D, F), angle(D, A, F) == angle(F, D, A) mod 360, orientation(F, D, A) == angle(F, D, A) + halfangle(A, F, D) mod 360
By angles_on_equal_chords on C, D, A, B, A, D, c we get coangle(B, A, D) == coangle(C, D, A) mod 360
By in_imply_collinear on F, D, G we get collinear(D, F, G)
By reverse_direction on D, A we get 180 == direction(D, A) - direction(A, D) mod 360
By not_in_line_equivalent_to_not_collinear_v0_r on H, F, D we get H not in Line(D, F)
By reverse_orientation on C, F, D we get orientation(C, F, D) == 0 - orientation(D, F, C) mod 360
By reverse_direction on A, F we get 180 == direction(A, F) - direction(F, A) mod 360
By orientations_are_cyclic on H, F, D we get orientation(F, D, H) == orientation(H, F, D) mod 360, orientation(D, H, F) == orientation(H, F, D) mod 360
By reverse_orientation on H, F, D we get orientation(H, F, D) == 0 - orientation(D, F, H) mod 360
By coangle_definition_v1 on A, D, C we get angle(A, D, C) == coangle(A, D, C) + orientation(A, D, C) mod 360
By coangle_definition_v1 on D, F, C we get angle(D, F, C) == coangle(D, F, C) + orientation(D, F, C) mod 360
By coangle_definition_v1 on C, D, F we get angle(C, D, F) == coangle(C, D, F) + orientation(C, D, F) mod 360
By coangle_definition_v1 on D, A, B we get angle(D, A, B) == coangle(D, A, B) + orientation(D, A, B) mod 360
By reverse_direction on E, B we get 180 == direction(E, B) - direction(B, E) mod 360
By coangle_definition_v1 on C, F, D we get angle(C, F, D) == coangle(C, F, D) + orientation(C, F, D) mod 360
By reverse_direction on E, A we get 180 == direction(E, A) - direction(A, E) mod 360
By coangle_definition_v1 on F, D, H we get angle(F, D, H) == coangle(F, D, H) + orientation(F, D, H) mod 360
By coangle_definition_v1 on D, F, H we get angle(D, F, H) == coangle(D, F, H) + orientation(D, F, H) mod 360
By coangle_definition_v1 on G, E, H we get angle(G, E, H) == coangle(G, E, H) + orientation(G, E, H) mod 360
By coangle_definition_v1 on H, E, F we get angle(H, E, F) == coangle(H, E, F) + orientation(H, E, F) mod 360
By collinear_definition on G, D, A we get D in Line(A, G), A in Line(D, G), Line(A, G) == Line(D, G), 0 == 2 * angle(D, G, A) mod 360
By coangle_definition_v1 on E, F, H we get angle(E, F, H) == coangle(E, F, H) + orientation(E, F, H) mod 360
By coangle_definition_v1 on F, E, G we get angle(F, E, G) == coangle(F, E, G) + orientation(F, E, G) mod 360
By coangle_definition_v1 on D, H, C we get angle(D, H, C) == coangle(D, H, C) + orientation(D, H, C) mod 360
By coangle_definition_v1 on F, H, G we get angle(F, H, G) == coangle(F, H, G) + orientation(F, H, G) mod 360
By coangle_definition_v1 on C, H, F we get angle(C, H, F) == coangle(C, H, F) + orientation(C, H, F) mod 360
By coangle_definition_v1 on H, G, F we get angle(H, G, F) == coangle(H, G, F) + orientation(H, G, F) mod 360
By coangle_definition_v1 on E, G, H we get angle(E, G, H) == coangle(E, G, H) + orientation(E, G, H) mod 360
By coangle_definition_v1 on F, E, H we get angle(F, E, H) == coangle(F, E, H) + orientation(F, E, H) mod 360
By coangle_definition_v1 on G, F, H we get angle(G, F, H) == coangle(G, F, H) + orientation(G, F, H) mod 360
By triangle_halfangle_sum on B, E, A we get orientation(B, E, A) == halfangle(B, E, A) + halfangle(E, A, B) + halfangle(A, B, E) mod 360
By isosceles_trapezoids_are_concyclic_v1 on C, D, A, B we get isosceles_trapezoid(A, B, C, D)
By same_angle on F, G, D, H we get coangle(D, F, H) == coangle(G, F, H) mod 360
By same_angle on F, D, A, C we get coangle(A, F, C) == coangle(D, F, C) mod 360
By same_angle on G, F, D, H we get coangle(D, G, H) == coangle(F, G, H) mod 360
By same_angle on D, F, G, H we get coangle(F, D, H) == coangle(G, D, H) mod 360
By orientations_are_cyclic on F, H, G we get orientation(F, H, G) == orientation(H, G, F) mod 360, orientation(F, H, G) == orientation(G, F, H) mod 360
By reverse_orientation on H, E, F we get orientation(H, E, F) == 0 - orientation(F, E, H) mod 360
By reverse_direction on E, G we get 180 == direction(E, G) - direction(G, E) mod 360
By reverse_direction on G, F we get 180 == direction(G, F) - direction(F, G) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on H, G, D we get not_collinear(D, G, H), exists(Line(D, G))
By reverse_direction on G, D we get 180 == direction(G, D) - direction(D, G) mod 360
By isosceles_trapezoids_contain_isosceles_triangles on B, A, D, C we get isosceles_triangle(line_intersection(Line(A, D), Line(B, C)), A, B), isosceles_triangle(line_intersection(Line(A, D), Line(B, C)), C, D)
By perpendicular_bisector_sufficient_conditions on D, A, E, F we get Line(E, F) == perpendicular_bisector(A, D)
By perpendicular_direction_conditions_v0_r on G, D, F, E we get 180 == 2 * direction(G, D) - 2 * direction(F, E) mod 360
By coangle_definition_v1 on D, G, H we get angle(D, G, H) == coangle(D, G, H) + orientation(D, G, H) mod 360
By coangle_definition_v1 on G, D, H we get angle(G, D, H) == coangle(G, D, H) + orientation(G, D, H) mod 360
By coangle_definition_v0 on D, H, G we get angle(D, H, G) == coangle(D, H, G) + orientation(D, H, G) mod 360
By coangle_definition_v0 on G, H, D we get angle(G, H, D) == coangle(G, H, D) + orientation(G, H, D) mod 360
By perpendicular_bisector_sufficient_conditions on A, B, G, E we get Line(E, G) == perpendicular_bisector(A, B)
By perpendicular_direction_conditions_v0_r on B, A, E, G we get 180 == 2 * direction(B, A) - 2 * direction(E, G) mod 360
By orientations_are_cyclic on D, G, H we get orientation(D, G, H) == orientation(G, H, D) mod 360, orientation(D, G, H) == orientation(H, D, G) mod 360
By orientations_are_cyclic on D, H, G we get orientation(D, H, G) == orientation(H, G, D) mod 360, orientation(D, H, G) == orientation(G, D, H) mod 360
By divide_by_2_two_angles on D, H, G, A, F, C we get coangle(A, F, C) == coangle(D, H, G) mod 360
By same_angle_converse on H, G, C, D we get collinear(C, G, H)
