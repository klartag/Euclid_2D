Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h: Line
c, d, e, k: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h)
distinct(c, d, e, k)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == center(c)
d == Circle(A, E, D)
h == Line(C, A)
e == Circle(C, E, B)
k == Circle(D, C, E)
F in h, k
G in h, e
H == center(d)

Need to prove:
concyclic(D, F, G, H)

Proof:
By line_definition on F, G, h we get h == Line(F, G)
By line_definition on G, C, h we get h == Line(C, G)
By line_definition on C, D, g we get g == Line(C, D)
By line_definition on F, C, h we get h == Line(C, F)
By circle_definition on C, A, D, c we get c == Circle(A, C, D)
By circle_definition on D, B, C, c we get c == Circle(B, C, D)
By circle_definition on C, E, G, e we get e == Circle(C, E, G)
By circle_definition on E, F, C, k we get k == Circle(C, E, F)
By circle_definition on G, B, C, e we get e == Circle(B, C, G)
By circle_radius_v0_r on D, d we get radius(d) == distance(D, center(d))
By circle_radius_v0_r on C, c we get radius(c) == distance(C, center(c))
By circle_radius_v0_r on D, c we get radius(c) == distance(D, center(c))
By angles_on_chord on D, E, F, C, k we get coangle(D, C, E) == coangle(D, F, E) mod 360
By circle_radius_v0_r on A, c we get radius(c) == distance(A, center(c))
By circle_radius_v0_r on E, d we get radius(d) == distance(E, center(d))
By circle_radius_v0_r on B, c we get radius(c) == distance(B, center(c))
By angles_on_chord on C, G, B, E, e we get coangle(C, B, G) == coangle(C, E, G) mod 360
By angles_on_chord on E, C, B, G, e we get coangle(E, B, C) == coangle(E, G, C) mod 360
By angles_on_chord on A, B, D, C, c we get coangle(A, C, B) == coangle(A, D, B) mod 360
By angles_on_chord on F, D, E, C, k we get coangle(F, C, D) == coangle(F, E, D) mod 360
By angles_on_chord on B, C, E, G, e we get coangle(B, E, C) == coangle(B, G, C) mod 360
By angles_on_chord on F, E, D, C, k we get coangle(F, C, E) == coangle(F, D, E) mod 360
By angles_on_chord on F, C, E, D, k we get coangle(F, D, C) == coangle(F, E, C) mod 360
By angles_on_chord on A, D, B, C, c we get coangle(A, B, D) == coangle(A, C, D) mod 360
By angles_on_chord on B, E, G, C, e we get coangle(B, C, E) == coangle(B, G, E) mod 360
By angles_on_chord on G, B, E, C, e we get coangle(G, C, B) == coangle(G, E, B) mod 360
By angles_on_chord on G, E, C, B, e we get coangle(G, B, E) == coangle(G, C, E) mod 360
By angles_on_chord on E, C, F, D, k we get coangle(E, D, C) == coangle(E, F, C) mod 360
By angles_on_chord on C, B, D, A, c we get coangle(C, A, B) == coangle(C, D, B) mod 360
By in_imply_collinear on G, A, C we get collinear(A, C, G)
By in_imply_collinear on F, C, A we get collinear(A, C, F)
By angle_to_center on C, A, B, c we get coangle(C, A, B) == halfangle(C, center(c), B) - orientation(C, center(c), B) mod 360
By angle_to_center on D, B, C, c we get coangle(D, B, C) == halfangle(D, center(c), C) - orientation(D, center(c), C) mod 360
By angle_to_center on A, C, B, c we get coangle(A, C, B) == halfangle(A, center(c), B) - orientation(A, center(c), B) mod 360
By angle_to_center on A, C, D, c we get coangle(A, C, D) == halfangle(A, center(c), D) - orientation(A, center(c), D) mod 360
By angle_to_center on C, B, D, c we get coangle(C, B, D) == halfangle(C, center(c), D) - orientation(C, center(c), D) mod 360
By angle_to_center on E, A, D, d we get coangle(E, A, D) == halfangle(E, center(d), D) - orientation(E, center(d), D) mod 360
By angle_to_center on D, E, A, d we get coangle(D, E, A) == halfangle(D, center(d), A) - orientation(D, center(d), A) mod 360
By angles_on_equal_chords on C, A, B, A, B, D, c we get coangle(A, B, D) == coangle(C, A, B) mod 360
By same_angle on C, A, F, D we get coangle(A, C, D) == coangle(F, C, D) mod 360
By same_angle on C, F, A, E we get coangle(A, C, E) == coangle(F, C, E) mod 360
By same_angle on C, G, A, E we get coangle(A, C, E) == coangle(G, C, E) mod 360
By orientations_are_cyclic on A, E, D we get orientation(A, E, D) == orientation(E, D, A) mod 360, orientation(A, E, D) == orientation(D, A, E) mod 360
By in_imply_collinear on C, G, F we get collinear(C, F, G)
By orientations_are_cyclic on E, H, D we get orientation(E, H, D) == orientation(H, D, E) mod 360, orientation(D, E, H) == orientation(E, H, D) mod 360
By coangle_definition_v1 on D, E, A we get angle(D, E, A) == coangle(D, E, A) + orientation(D, E, A) mod 360
By orientations_are_cyclic on D, E, A we get orientation(D, E, A) == orientation(E, A, D) mod 360, orientation(A, D, E) == orientation(D, E, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0_r on E, G, C we get E not in Line(C, G)
By orientations_are_cyclic on C, E, D we get orientation(C, E, D) == orientation(E, D, C) mod 360, orientation(C, E, D) == orientation(D, C, E) mod 360
By orientations_are_cyclic on C, E, B we get orientation(C, E, B) == orientation(E, B, C) mod 360, orientation(B, C, E) == orientation(C, E, B) mod 360
By coangle_definition_v1 on F, E, C we get angle(F, E, C) == coangle(F, E, C) + orientation(F, E, C) mod 360
By coangle_definition_v1 on G, E, B we get angle(G, E, B) == coangle(G, E, B) + orientation(G, E, B) mod 360
By coangle_definition_v1 on C, E, G we get angle(C, E, G) == coangle(C, E, G) + orientation(C, E, G) mod 360
By coangle_definition_v1 on F, E, D we get angle(F, E, D) == coangle(F, E, D) + orientation(F, E, D) mod 360
By coangle_definition_v1 on G, B, E we get angle(G, B, E) == coangle(G, B, E) + orientation(G, B, E) mod 360
By coangle_definition_v1 on A, D, B we get angle(A, D, B) == coangle(A, D, B) + orientation(A, D, B) mod 360
By collinear_definition on F, A, C we get A in Line(C, F), C in Line(A, F), Line(A, F) == Line(C, F), 0 == 2 * angle(A, F, C) mod 360
By coangle_definition_v1 on E, B, C we get angle(E, B, C) == coangle(E, B, C) + orientation(E, B, C) mod 360
By coangle_definition_v1 on E, A, D we get angle(E, A, D) == coangle(E, A, D) + orientation(E, A, D) mod 360
By coangle_definition_v1 on E, F, C we get angle(E, F, C) == coangle(E, F, C) + orientation(E, F, C) mod 360
By coangle_definition_v1 on F, D, C we get angle(F, D, C) == coangle(F, D, C) + orientation(F, D, C) mod 360
By coangle_definition_v1 on D, B, C we get angle(D, B, C) == coangle(D, B, C) + orientation(D, B, C) mod 360
By coangle_definition_v1 on B, G, C we get angle(B, G, C) == coangle(B, G, C) + orientation(B, G, C) mod 360
By coangle_definition_v1 on E, D, C we get angle(E, D, C) == coangle(E, D, C) + orientation(E, D, C) mod 360
By coangle_definition_v1 on D, C, E we get angle(D, C, E) == coangle(D, C, E) + orientation(D, C, E) mod 360
By coangle_definition_v1 on F, D, E we get angle(F, D, E) == coangle(F, D, E) + orientation(F, D, E) mod 360
By coangle_definition_v1 on E, G, C we get angle(E, G, C) == coangle(E, G, C) + orientation(E, G, C) mod 360
By coangle_definition_v1 on B, G, E we get angle(B, G, E) == coangle(B, G, E) + orientation(B, G, E) mod 360
By coangle_definition_v1 on G, C, B we get angle(G, C, B) == coangle(G, C, B) + orientation(G, C, B) mod 360
By coangle_definition_v1 on B, C, E we get angle(B, C, E) == coangle(B, C, E) + orientation(B, C, E) mod 360
By isosceles_triangle_properties on H, D, E we get distance(D, H) == distance(E, H), angle(D, E, H) == angle(H, D, E) mod 360, orientation(H, D, E) == angle(H, D, E) + halfangle(E, H, D) mod 360
By isosceles_triangle_properties on E, D, C we get distance(C, E) == distance(D, E), angle(D, C, E) == angle(E, D, C) mod 360, orientation(E, D, C) == angle(E, D, C) + halfangle(C, E, D) mod 360
By isosceles_triangle_properties on E, D, A we get distance(A, E) == distance(D, E), angle(D, A, E) == angle(E, D, A) mod 360, orientation(E, D, A) == angle(E, D, A) + halfangle(A, E, D) mod 360
By isosceles_triangle_properties on E, B, C we get distance(B, E) == distance(C, E), angle(B, C, E) == angle(E, B, C) mod 360, orientation(E, B, C) == angle(E, B, C) + halfangle(C, E, B) mod 360
By divide_by_2_two_angles on C, B, G, C, B, D we get coangle(C, B, D) == coangle(C, B, G) mod 360
By orientations_are_cyclic on G, E, B we get orientation(E, B, G) == orientation(G, E, B) mod 360, orientation(B, G, E) == orientation(G, E, B) mod 360
By divide_by_2_two_angles on D, E, A, B, G, C we get coangle(B, G, C) == coangle(D, E, A) mod 360
By orientations_are_cyclic on C, E, G we get orientation(C, E, G) == orientation(E, G, C) mod 360, orientation(C, E, G) == orientation(G, C, E) mod 360
By orientations_are_cyclic on G, C, B we get orientation(C, B, G) == orientation(G, C, B) mod 360, orientation(B, G, C) == orientation(G, C, B) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on E, F, A we get not_collinear(A, E, F), exists(Line(A, F))
By not_in_line_equivalent_to_not_collinear_v0 on E, F, G we get not_collinear(E, F, G), exists(Line(F, G))
By divide_by_2_two_angles on C, D, B, H, E, D we get coangle(C, D, B) == coangle(H, E, D) mod 360
By collinear_definition on F, G, C we get G in Line(C, F), C in Line(F, G), Line(C, F) == Line(F, G), 0 == 2 * angle(G, F, C) mod 360
By same_angle_converse on E, F, H, D we get collinear(E, F, H)
By divide_by_2_two_angles on D, C, E, E, F, A we get coangle(D, C, E) == coangle(E, F, A) mod 360
By sas_anti_congruence on G, E, C, G, E, D we get anti_congruent_triangles(C, E, G, D, E, G)
By same_angle on F, E, H, G we get coangle(E, F, G) == coangle(H, F, G) mod 360
By divide_by_2_two_angles on E, F, A, E, F, G we get coangle(E, F, A) == coangle(E, F, G) mod 360
By angle_equality_conversions_v0 on E, D, C, H, D, G we get coangle(E, D, C) == coangle(H, D, G) mod 360, orientation(E, D, C) == orientation(H, D, G) mod 360
By concyclic_sufficient_conditions on H, F, G, D we get concyclic(D, F, G, H)
