Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(C, A)
c == Circle(D, C, A)
F == projection(A, g)
j == Line(A, F)
G in j, c
d == Circle(C, E, F)
H in c, d

Need to prove:
concyclic(B, F, G, H)

Proof:
By line_definition on F, A, perpendicular_line(A, g) we get Line(A, F) == perpendicular_line(A, g)
By line_definition on D, C, h we get h == Line(C, D)
By line_definition on F, C, g we get g == Line(C, F)
By line_definition on A, G, j we get j == Line(A, G)
By line_definition on F, G, j we get j == Line(F, G)
By line_definition on A, D, i we get i == Line(A, D)
By line_definition on F, B, g we get g == Line(B, F)
By circle_definition on G, D, C, c we get c == Circle(C, D, G)
By circle_definition on A, C, G, c we get c == Circle(A, C, G)
By line_unique_intersection_v1 on g, j, F, G we get G not in g
By line_unique_intersection_v1 on j, g, F, B we get B not in j
By line_unique_intersection_v1 on g, f, B, A we get A not in g
By line_unique_intersection_v1 on f, g, B, C we get C not in f
By angles_on_chord on C, F, E, H, d we get coangle(C, E, F) == coangle(C, H, F) mod 360
By angles_on_chord on C, A, H, D, c we get coangle(C, D, A) == coangle(C, H, A) mod 360
By angles_on_chord on A, C, D, G, c we get coangle(A, D, C) == coangle(A, G, C) mod 360
By angles_on_chord on G, C, H, A, c we get coangle(G, A, C) == coangle(G, H, C) mod 360
By angles_on_chord on D, C, G, A, c we get coangle(D, A, C) == coangle(D, G, C) mod 360
By angles_on_chord on C, G, A, H, c we get coangle(C, A, G) == coangle(C, H, G) mod 360
By angles_on_chord on D, G, A, C, c we get coangle(D, A, G) == coangle(D, C, G) mod 360
By angles_on_chord on C, D, G, A, c we get coangle(C, A, D) == coangle(C, G, D) mod 360
By angles_on_chord on C, A, G, H, c we get coangle(C, G, A) == coangle(C, H, A) mod 360
By in_imply_collinear on F, C, B we get collinear(B, C, F)
By in_imply_collinear on G, F, A we get collinear(A, F, G)
By double_perpendicular_and_parallel_v0_r on g, perpendicular_line(A, g), i we get perpendicular(i, perpendicular_line(A, g))
By collinear_definition on E, A, C we get A in Line(C, E), C in Line(A, E), Line(A, E) == Line(C, E), 0 == 2 * angle(A, E, C) mod 360
By collinear_definition on A, E, C we get E in Line(A, C), C in Line(A, E), Line(A, C) == Line(A, E), 0 == 2 * angle(E, A, C) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on A, F, B we get not_collinear(A, B, F), exists(Line(B, F))
By reverse_direction on A, C we get 180 == direction(A, C) - direction(C, A) mod 360
By reverse_orientation on D, A, C we get orientation(D, A, C) == 0 - orientation(C, A, D) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on G, C, F we get not_collinear(C, F, G), exists(Line(C, F))
By not_in_line_equivalent_to_not_collinear_v0 on C, A, B we get not_collinear(A, B, C), exists(Line(A, B))
By orientations_are_cyclic on D, A, C we get orientation(A, C, D) == orientation(D, A, C) mod 360, orientation(C, D, A) == orientation(D, A, C) mod 360
By orientations_are_cyclic on G, A, C we get orientation(A, C, G) == orientation(G, A, C) mod 360, orientation(C, G, A) == orientation(G, A, C) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on B, G, F we get not_collinear(B, F, G), exists(Line(F, G))
By perpendicular_angle_conditions_v0 on D, A, G we get 0 == coangle(D, A, G) mod 360
By perpendicular_direction_conditions_v0_r on C, F, G, A we get 180 == 2 * direction(C, F) - 2 * direction(G, A) mod 360
By perpendicular_direction_conditions_v0_r on D, A, G, F we get 180 == 2 * direction(D, A) - 2 * direction(G, F) mod 360
By coangle_definition_v1 on C, A, D we get angle(C, A, D) == coangle(C, A, D) + orientation(C, A, D) mod 360
By coangle_definition_v1 on C, E, F we get angle(C, E, F) == coangle(C, E, F) + orientation(C, E, F) mod 360
By coangle_definition_v1 on C, A, G we get angle(C, A, G) == coangle(C, A, G) + orientation(C, A, G) mod 360
By perpendicular_angle_conditions_v0 on A, F, B we get 0 == coangle(A, F, B) mod 360
By perpendicular_angle_conditions_v0 on C, F, G we get 0 == coangle(C, F, G) mod 360
By coangle_definition_v1 on G, A, C we get angle(G, A, C) == coangle(G, A, C) + orientation(G, A, C) mod 360
By coangle_definition_v1 on D, A, C we get angle(D, A, C) == coangle(D, A, C) + orientation(D, A, C) mod 360
By perpendicular_angle_conditions_v0 on A, F, C we get 0 == coangle(A, F, C) mod 360
By parallel_line_angles_v0 on D, A, C, F we get coangle(D, A, C) == coangle(F, C, A) mod 360
By coangle_definition_v1 on C, H, G we get angle(C, H, G) == coangle(C, H, G) + orientation(C, H, G) mod 360
By right_triangle_circumcenter_v1 on A, F, C we get midpoint(A, C) == circumcenter(A, C, F)
By coangle_definition_v1 on C, G, D we get angle(C, G, D) == coangle(C, G, D) + orientation(C, G, D) mod 360
By coangle_definition_v1 on D, C, G we get angle(D, C, G) == coangle(D, C, G) + orientation(D, C, G) mod 360
By coangle_definition_v1 on C, D, A we get angle(C, D, A) == coangle(C, D, A) + orientation(C, D, A) mod 360
By coangle_definition_v1 on C, H, F we get angle(C, H, F) == coangle(C, H, F) + orientation(C, H, F) mod 360
By coangle_definition_v1 on C, G, A we get angle(C, G, A) == coangle(C, G, A) + orientation(C, G, A) mod 360
By parallelogram_parallel_definition on B, C, D, A we get parallelogram(A, B, C, D)
By same_angle on G, F, A, C we get coangle(A, G, C) == coangle(F, G, C) mod 360
By sas_congruence on A, B, C, C, D, A we get congruent_triangles(A, B, C, C, D, A)
By reverse_direction on G, F we get 180 == direction(G, F) - direction(F, G) mod 360
By orientations_are_cyclic on G, D, C we get orientation(D, C, G) == orientation(G, D, C) mod 360, orientation(C, G, D) == orientation(G, D, C) mod 360
By aa_anti_similarity on D, C, G, A, F, C we get anti_similar_triangles(A, C, F, D, G, C)
By reverse_direction on G, A we get 180 == direction(G, A) - direction(A, G) mod 360
By reverse_direction on F, A we get 180 == direction(F, A) - direction(A, F) mod 360
By coangle_definition_v1 on C, F, G we get angle(C, F, G) == coangle(C, F, G) + orientation(C, F, G) mod 360
By angle_to_center on F, C, A, Circle(A, C, F) we get coangle(F, C, A) == halfangle(F, center(Circle(A, C, F)), A) - orientation(F, center(Circle(A, C, F)), A) mod 360
By same_angle on B, F, C, A we get coangle(C, B, A) == coangle(F, B, A) mod 360
By angle_equality_conversions_v0 on A, D, C, C, B, A we get coangle(A, D, C) == coangle(C, B, A) mod 360, orientation(A, D, C) == orientation(C, B, A) mod 360
By aa_similarity on C, F, G, A, F, B we get similar_triangles(A, B, F, C, G, F)
By orientations_are_cyclic on C, F, G we get orientation(C, F, G) == orientation(F, G, C) mod 360, orientation(C, F, G) == orientation(G, C, F) mod 360
By divide_by_2_two_angles on G, A, C, F, H, G we get coangle(F, H, G) == coangle(G, A, C) mod 360
By coangle_definition_v0 on G, C, F we get angle(G, C, F) == coangle(G, C, F) + orientation(G, C, F) mod 360
By coangle_definition_v0 on G, C, B we get angle(G, C, B) == coangle(G, C, B) + orientation(G, C, B) mod 360
By divide_by_2_two_angles on G, C, F, G, C, B we get coangle(G, C, B) == coangle(G, C, F) mod 360
By similar_triangle_basic_properties on G, F, C, B, F, A we get not_collinear(C, F, G), not_collinear(A, B, F), angle(B, F, A) == angle(G, F, C) mod 360, angle(F, A, B) == angle(F, C, G) mod 360, angle(A, B, F) == angle(C, G, F) mod 360, log(distance(B, F)) + log(distance(C, F)) == log(distance(F, G)) + log(distance(A, F)), log(distance(A, F)) + log(distance(C, G)) == log(distance(C, F)) + log(distance(A, B)), log(distance(A, B)) + log(distance(F, G)) == log(distance(C, G)) + log(distance(B, F))
By orientations_are_cyclic on G, C, B we get orientation(C, B, G) == orientation(G, C, B) mod 360, orientation(B, G, C) == orientation(G, C, B) mod 360
By same_angle on B, F, C, G we get coangle(C, B, G) == coangle(F, B, G) mod 360
By coangle_definition_v1 on C, B, G we get angle(C, B, G) == coangle(C, B, G) + orientation(C, B, G) mod 360
By sas_similarity on A, F, C, B, F, G we get similar_triangles(A, C, F, B, G, F)
By concyclic_sufficient_conditions on F, B, G, H we get concyclic(B, F, G, H)
