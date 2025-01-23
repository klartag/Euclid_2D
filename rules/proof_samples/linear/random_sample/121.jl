Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, A)
g == parallel_line(C, f)
c == Circle(C, A, B)
D in g, c
E == center(c)
h == Line(C, A)
i == internal_angle_bisector(D, E, B)
F == line_intersection(h, i)
d == Circle(F, E, C)
G == center(d)
H == midpoint(B, E)

Need to prove:
collinear(G, B, H)

Proof:
By line_definition on C, D, g we get g == Line(C, D)
By circle_definition on B, C, D, c we get c == Circle(B, C, D)
By circle_definition on D, C, A, c we get c == Circle(A, C, D)
By circle_radius_v0_r on B, c we get radius(c) == distance(B, center(c))
By circle_radius_v0_r on E, d we get radius(d) == distance(E, center(d))
By circle_radius_v0_r on F, d we get radius(d) == distance(F, center(d))
By circle_radius_v0_r on C, c we get radius(c) == distance(C, center(c))
By circle_radius_v0_r on D, c we get radius(c) == distance(D, center(c))
By circle_radius_v0_r on A, c we get radius(c) == distance(A, center(c))
By angles_on_chord on C, B, D, A, c we get coangle(C, A, B) == coangle(C, D, B) mod 360
By angles_on_chord on A, D, C, B, c we get coangle(A, B, D) == coangle(A, C, D) mod 360
By in_imply_collinear on F, C, A we get collinear(A, C, F)
By angle_to_center on C, D, B, c we get coangle(C, D, B) == halfangle(C, center(c), B) - orientation(C, center(c), B) mod 360
By angle_to_center on D, C, A, c we get coangle(D, C, A) == halfangle(D, center(c), A) - orientation(D, center(c), A) mod 360
By angle_to_center on C, D, A, c we get coangle(C, D, A) == halfangle(C, center(c), A) - orientation(C, center(c), A) mod 360
By angle_to_center on E, C, F, d we get coangle(E, C, F) == halfangle(E, center(d), F) - orientation(E, center(d), F) mod 360
By angle_to_center on A, B, D, c we get coangle(A, B, D) == halfangle(A, center(c), D) - orientation(A, center(c), D) mod 360
By angle_to_center on B, A, D, c we get coangle(B, A, D) == halfangle(B, center(c), D) - orientation(B, center(c), D) mod 360
By angle_to_center on F, C, E, d we get coangle(F, C, E) == halfangle(F, center(d), E) - orientation(F, center(d), E) mod 360
By log_of_2_times_distance on B, E, H, B we get log(distance(B, E)) == 0.6931471805599453 + log(distance(B, H))
By collinear_definition on B, E, H we get E in Line(B, H), H in Line(B, E), Line(B, E) == Line(B, H), 0 == 2 * angle(E, B, H) mod 360
By log_of_2_times_distance on B, E, E, H we get log(distance(B, E)) == 0.6931471805599453 + log(distance(E, H))
By collinear_definition on E, H, B we get H in Line(B, E), B in Line(E, H), Line(B, E) == Line(E, H), 0 == 2 * angle(H, E, B) mod 360
By angles_on_equal_chords on B, A, D, C, D, A, c we get coangle(B, A, D) == coangle(C, D, A) mod 360
By angles_on_equal_chords on A, C, D, C, A, B, c we get coangle(A, C, D) == coangle(C, A, B) mod 360
By same_angle on C, F, A, E we get coangle(A, C, E) == coangle(F, C, E) mod 360
By orientations_are_cyclic on B, E, D we get orientation(B, E, D) == orientation(E, D, B) mod 360, orientation(B, E, D) == orientation(D, B, E) mod 360
By orientations_are_cyclic on E, G, F we get orientation(E, G, F) == orientation(G, F, E) mod 360, orientation(E, G, F) == orientation(F, E, G) mod 360
By orientations_are_cyclic on D, E, B we get orientation(D, E, B) == orientation(E, B, D) mod 360, orientation(B, D, E) == orientation(D, E, B) mod 360
By orientations_are_cyclic on A, E, D we get orientation(A, E, D) == orientation(E, D, A) mod 360, orientation(A, E, D) == orientation(D, A, E) mod 360
By orientations_are_cyclic on C, E, A we get orientation(C, E, A) == orientation(E, A, C) mod 360, orientation(A, C, E) == orientation(C, E, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0_r on E, F, C we get E not in Line(C, F)
By orientations_are_cyclic on F, G, E we get orientation(F, G, E) == orientation(G, E, F) mod 360, orientation(E, F, G) == orientation(F, G, E) mod 360
By orientations_are_cyclic on C, E, B we get orientation(C, E, B) == orientation(E, B, C) mod 360, orientation(B, C, E) == orientation(C, E, B) mod 360
By reverse_direction on G, E we get 180 == direction(G, E) - direction(E, G) mod 360
By log_of_2_times_distance on D, E, H, E we get log(distance(D, E)) == 0.6931471805599453 + log(distance(E, H))
By reverse_direction on E, D we get 180 == direction(E, D) - direction(D, E) mod 360
By log_of_2_times_distance on A, E, H, B we get log(distance(A, E)) == 0.6931471805599453 + log(distance(B, H))
By log_of_2_times_distance on E, C, B, H we get log(distance(C, E)) == 0.6931471805599453 + log(distance(B, H))
By reverse_direction on G, F we get 180 == direction(G, F) - direction(F, G) mod 360
By internal_angle_bisector_definition_v0_r on H, B, H, E we get Line(B, E) == internal_angle_bisector(H, E, H)
By coangle_definition_v1 on D, C, A we get angle(D, C, A) == coangle(D, C, A) + orientation(D, C, A) mod 360
By collinear_definition on C, F, A we get F in Line(A, C), A in Line(C, F), Line(A, C) == Line(C, F), 0 == 2 * angle(F, C, A) mod 360
By isosceles_triangle_properties on E, B, C we get distance(B, E) == distance(C, E), angle(B, C, E) == angle(E, B, C) mod 360, orientation(E, B, C) == angle(E, B, C) + halfangle(C, E, B) mod 360
By isosceles_triangle_properties on E, D, B we get distance(B, E) == distance(D, E), angle(D, B, E) == angle(E, D, B) mod 360, orientation(E, D, B) == angle(E, D, B) + halfangle(B, E, D) mod 360
By triangle_halfangle_sum on D, E, C we get orientation(D, E, C) == halfangle(D, E, C) + halfangle(E, C, D) + halfangle(C, D, E) mod 360
By isosceles_triangle_properties on E, D, A we get distance(A, E) == distance(D, E), angle(D, A, E) == angle(E, D, A) mod 360, orientation(E, D, A) == angle(E, D, A) + halfangle(A, E, D) mod 360
By isosceles_triangle_properties on G, E, F we get distance(E, G) == distance(F, G), angle(E, F, G) == angle(G, E, F) mod 360, orientation(G, E, F) == angle(G, E, F) + halfangle(F, G, E) mod 360
By isosceles_triangle_properties on E, A, C we get distance(A, E) == distance(C, E), angle(A, C, E) == angle(E, A, C) mod 360, orientation(E, A, C) == angle(E, A, C) + halfangle(C, E, A) mod 360
By isosceles_triangle_properties on G, F, E we get distance(E, G) == distance(F, G), angle(F, E, G) == angle(G, F, E) mod 360, orientation(G, F, E) == angle(G, F, E) + halfangle(E, G, F) mod 360
By coangle_definition_v1 on A, C, E we get angle(A, C, E) == coangle(A, C, E) + orientation(A, C, E) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on E, C, A we get not_collinear(A, C, E), exists(Line(A, C))
By divide_by_2_two_angles on E, C, F, E, B, D we get coangle(E, B, D) == coangle(E, C, F) mod 360
By coangle_definition_v0 on E, B, D we get angle(E, B, D) == coangle(E, B, D) + orientation(E, B, D) mod 360
By anti_similar_triangle_basic_properties on C, D, A, D, C, B we get not_collinear(A, C, D), not_collinear(B, C, D), angle(C, D, A) == 0 - angle(D, C, B) mod 360, angle(D, A, C) == 0 - angle(C, B, D) mod 360, angle(A, C, D) == 0 - angle(B, D, C) mod 360, log(distance(C, D)) + log(distance(A, D)) == log(distance(C, D)) + log(distance(B, C)), log(distance(A, D)) + log(distance(B, D)) == log(distance(B, C)) + log(distance(A, C)), log(distance(A, C)) + log(distance(C, D)) == log(distance(B, D)) + log(distance(C, D))
By sss_anti_similarity on A, C, E, B, D, E we get anti_similar_triangles(A, C, E, B, D, E)
By isosceles_triangle_altitude_v2 on E, D, B we get identical(median(E, B, D), altitude(E, B, D), perpendicular_bisector(B, D), internal_angle_bisector(B, E, D))
By line_definition on F, E, i we get i == Line(E, F)
By perpendicular_direction_conditions_v0_r on F, E, D, B we get 180 == 2 * direction(F, E) - 2 * direction(D, B) mod 360
By internal_angle_bisector_definition_v0_r on H, G, H, E we get Line(E, G) == internal_angle_bisector(H, E, H)
By in_imply_collinear on G, B, H we get collinear(B, G, H)
