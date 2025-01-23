Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
E == midpoint(B, D)
c == Circle(E, A, D)
F == projection(C, f)
G in f, c
j == Line(G, D)
H == projection(B, j)

Need to prove:
concyclic(E, F, G, H)

Proof:
By line_definition on F, A, f we get f == Line(A, F)
By line_definition on F, B, f we get f == Line(B, F)
By line_definition on G, H, j we get j == Line(G, H)
By line_definition on G, B, f we get f == Line(B, G)
By line_definition on C, F, perpendicular_line(C, f) we get Line(C, F) == perpendicular_line(C, f)
By line_definition on G, A, f we get f == Line(A, G)
By line_definition on H, B, perpendicular_line(B, j) we get Line(B, H) == perpendicular_line(B, j)
By line_definition on D, A, i we get i == Line(A, D)
By line_definition on F, G, f we get f == Line(F, G)
By line_definition on D, H, j we get j == Line(D, H)
By line_definition on C, D, h we get h == Line(C, D)
By circle_definition on D, G, E, c we get c == Circle(D, E, G)
By circle_definition on D, A, G, c we get c == Circle(A, D, G)
By line_unique_intersection_v1 on j, f, G, B we get B not in j
By line_unique_intersection_v1 on f, j, G, D we get D not in f
By line_unique_intersection_v1 on f, g, B, C we get C not in f
By line_unique_intersection_v1 on j, f, G, F we get F not in j
By angles_on_chord on D, A, E, G, c we get coangle(D, E, A) == coangle(D, G, A) mod 360
By angles_on_chord on G, E, A, D, c we get coangle(G, A, E) == coangle(G, D, E) mod 360
By in_imply_collinear on G, A, B we get collinear(A, B, G)
By in_imply_collinear on H, G, D we get collinear(D, G, H)
By double_perpendicular_and_parallel_v0_r on f, perpendicular_line(C, f), h we get perpendicular(h, perpendicular_line(C, f))
By collinear_definition on B, D, E we get D in Line(B, E), E in Line(B, D), Line(B, D) == Line(B, E), 0 == 2 * angle(D, B, E) mod 360
By collinear_definition on D, B, E we get B in Line(D, E), E in Line(B, D), Line(B, D) == Line(D, E), 0 == 2 * angle(B, D, E) mod 360
By collinear_definition on B, E, D we get E in Line(B, D), D in Line(B, E), Line(B, D) == Line(B, E), 0 == 2 * angle(E, B, D) mod 360
By collinear_definition on D, E, B we get E in Line(B, D), B in Line(D, E), Line(B, D) == Line(D, E), 0 == 2 * angle(E, D, B) mod 360
By isosceles_triangle_properties on E, D, B we get distance(B, E) == distance(D, E), angle(D, B, E) == angle(E, D, B) mod 360, orientation(E, D, B) == angle(E, D, B) + halfangle(B, E, D) mod 360
By isosceles_triangle_properties on E, B, D we get distance(B, E) == distance(D, E), angle(B, D, E) == angle(E, B, D) mod 360, orientation(E, B, D) == angle(E, B, D) + halfangle(D, E, B) mod 360
By perpendicular_line_definition on D, h, Line(C, F) we get h == perpendicular_line(D, Line(C, F))
By perpendicular_line_definition on C, h, Line(C, F) we get h == perpendicular_line(C, Line(C, F))
By perpendicular_line_definition on C, Line(C, F), h we get Line(C, F) == perpendicular_line(C, h)
By perpendicular_line_definition on F, Line(C, F), h we get Line(C, F) == perpendicular_line(F, h)
By projection_definition on G, F, Line(C, F) we get F == projection(G, Line(C, F))
By projection_definition on B, F, Line(C, F) we get F == projection(B, Line(C, F))
By projection_definition on A, F, Line(C, F) we get F == projection(A, Line(C, F))
By projection_definition on D, H, Line(B, H) we get H == projection(D, Line(B, H))
By projection_definition on G, H, Line(B, H) we get H == projection(G, Line(B, H))
By triangle_halfangle_sum on B, E, D we get orientation(B, E, D) == halfangle(B, E, D) + halfangle(E, D, B) + halfangle(D, B, E) mod 360
By different_points_v1 on D, A we get 0 != distance(A, D)
By different_points_v1 on A, F we get 0 != distance(A, F)
By triangle_halfangle_sum on D, E, B we get orientation(D, E, B) == halfangle(D, E, B) + halfangle(E, B, D) + halfangle(B, D, E) mod 360
By different_points_v1 on C, F we get 0 != distance(C, F)
By different_points_v1 on B, F we get 0 != distance(B, F)
By different_points_v1 on H, G we get 0 != distance(G, H)
By different_points_v1 on G, A we get 0 != distance(A, G)
By different_points_v1 on D, H we get 0 != distance(D, H)
By different_points_v1 on G, F we get 0 != distance(F, G)
By different_points_v1 on B, H we get 0 != distance(B, H)
By different_points_v1 on G, B we get 0 != distance(B, G)
By different_points_v1 on C, D we get 0 != distance(C, D)
By same_angle on D, G, H, E we get coangle(G, D, E) == coangle(H, D, E) mod 360
By same_angle on G, A, B, D we get coangle(A, G, D) == coangle(B, G, D) mod 360
By same_angle on G, D, H, A we get coangle(D, G, A) == coangle(H, G, A) mod 360
By projection_definition on F, C, h we get C == projection(F, h)
By same_angle on A, G, B, D we get coangle(B, A, D) == coangle(G, A, D) mod 360
By same_angle on D, E, B, G we get coangle(B, D, G) == coangle(E, D, G) mod 360
By same_angle on D, G, H, A we get coangle(G, D, A) == coangle(H, D, A) mod 360
By projection_definition on D, C, Line(C, F) we get C == projection(D, Line(C, F))
By same_angle on D, E, B, A we get coangle(B, D, A) == coangle(E, D, A) mod 360
By in_imply_collinear on F, G, A we get collinear(A, F, G)
By not_in_line_equivalent_to_not_collinear_v0 on C, A, B we get not_collinear(A, B, C), exists(Line(A, B))
By orientations_are_cyclic on C, D, B we get orientation(C, D, B) == orientation(D, B, C) mod 360, orientation(B, C, D) == orientation(C, D, B) mod 360
By reverse_direction on B, D we get 180 == direction(B, D) - direction(D, B) mod 360
By in_imply_collinear on G, B, F we get collinear(B, F, G)
By not_in_line_equivalent_to_not_collinear_v0 on D, F, G we get not_collinear(D, F, G), exists(Line(F, G))
By not_in_line_equivalent_to_not_collinear_v0 on B, G, D we get not_collinear(B, D, G), exists(Line(D, G))
By not_in_line_equivalent_to_not_collinear_v0 on B, G, H we get not_collinear(B, G, H), exists(Line(G, H))
By not_in_line_equivalent_to_not_collinear_v0 on F, G, H we get not_collinear(F, G, H), exists(Line(G, H))
By not_in_line_equivalent_to_not_collinear_v0_r on A, D, E we get A not in Line(D, E)
By not_in_line_equivalent_to_not_collinear_v0 on C, F, A we get not_collinear(A, C, F), exists(Line(A, F))
By perpendicular_direction_conditions_v0_r on H, B, G, H we get 180 == 2 * direction(H, B) - 2 * direction(G, H) mod 360
By perpendicular_direction_conditions_v0_r on F, B, F, C we get 180 == 2 * direction(F, B) - 2 * direction(F, C) mod 360
By perpendicular_direction_conditions_v0_r on C, F, A, G we get 180 == 2 * direction(C, F) - 2 * direction(A, G) mod 360
By perpendicular_direction_conditions_v0_r on F, C, A, F we get 180 == 2 * direction(F, C) - 2 * direction(A, F) mod 360
By perpendicular_direction_conditions_v0_r on F, B, C, F we get 180 == 2 * direction(F, B) - 2 * direction(C, F) mod 360
By perpendicular_direction_conditions_v0_r on H, B, G, D we get 180 == 2 * direction(H, B) - 2 * direction(G, D) mod 360
By perpendicular_direction_conditions_v0_r on C, F, G, B we get 180 == 2 * direction(C, F) - 2 * direction(G, B) mod 360
By perpendicular_direction_conditions_v0_r on H, B, D, G we get 180 == 2 * direction(H, B) - 2 * direction(D, G) mod 360
By perpendicular_direction_conditions_v0_r on H, B, D, H we get 180 == 2 * direction(H, B) - 2 * direction(D, H) mod 360
By perpendicular_direction_conditions_v0_r on C, F, G, A we get 180 == 2 * direction(C, F) - 2 * direction(G, A) mod 360
By perpendicular_direction_conditions_v0_r on G, F, C, F we get 180 == 2 * direction(G, F) - 2 * direction(C, F) mod 360
By coangle_definition_v1 on G, D, E we get angle(G, D, E) == coangle(G, D, E) + orientation(G, D, E) mod 360
By coangle_definition_v1 on D, E, A we get angle(D, E, A) == coangle(D, E, A) + orientation(D, E, A) mod 360
By coangle_definition_v1 on D, G, A we get angle(D, G, A) == coangle(D, G, A) + orientation(D, G, A) mod 360
By coangle_definition_v1 on G, A, E we get angle(G, A, E) == coangle(G, A, E) + orientation(G, A, E) mod 360
By right_triangle_circumcenter_v1 on D, H, B we get midpoint(B, D) == circumcenter(B, D, H)
By parallelogram_parallel_definition on D, C, B, A we get parallelogram(A, B, C, D)
By same_angle on G, F, B, D we get coangle(B, G, D) == coangle(F, G, D) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on A, B, E we get not_collinear(A, B, E), exists(Line(B, E))
By same_angle on G, F, B, H we get coangle(B, G, H) == coangle(F, G, H) mod 360
By angle_to_center on B, D, H, Circle(B, D, H) we get coangle(B, D, H) == halfangle(B, center(Circle(B, D, H)), H) - orientation(B, center(Circle(B, D, H)), H) mod 360
By parallelogram_diagonals_v1 on D, A, B, C we get identical(midpoint(A, C), midpoint(B, D), line_intersection(Line(A, C), Line(B, D)))
By divide_by_2_two_angles on B, G, H, F, G, D we get coangle(B, G, H) == coangle(F, G, D) mod 360
By same_angle on A, C, E, F we get coangle(C, A, F) == coangle(E, A, F) mod 360
By divide_by_2_two_angles on B, G, D, A, E, B we get coangle(A, E, B) == coangle(B, G, D) mod 360
By divide_by_2_two_angles on B, D, H, E, A, F we get coangle(B, D, H) == coangle(E, A, F) mod 360
By collinear_definition on E, A, C we get A in Line(C, E), C in Line(A, E), Line(A, E) == Line(C, E), 0 == 2 * angle(A, E, C) mod 360
By right_triangle_circumcenter_v1 on A, F, C we get midpoint(A, C) == circumcenter(A, C, F)
By angle_to_center on C, A, F, Circle(A, C, F) we get coangle(C, A, F) == halfangle(C, center(Circle(A, C, F)), F) - orientation(C, center(Circle(A, C, F)), F) mod 360
By divide_by_2_two_angles on A, E, B, F, E, H we get coangle(A, E, B) == coangle(F, E, H) mod 360
By concyclic_sufficient_conditions on F, E, H, G we get concyclic(E, F, G, H)
