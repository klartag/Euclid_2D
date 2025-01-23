Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j, k, l)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
k == Line(C, F)
G == line_intersection(i, j)
H == midpoint(G, C)
I == midpoint(C, A)
l == Line(D, I)
c == Circle(H, I, A)
J in k, c
K == line_intersection(l, k)

Need to prove:
concyclic(A, D, J, K)

Proof:
By line_definition on A, F, f we get f == Line(A, F)
By line_definition on J, F, k we get k == Line(F, J)
By line_definition on E, G, j we get j == Line(E, G)
By line_definition on K, C, k we get k == Line(C, K)
By line_definition on C, F, perpendicular_line(C, f) we get Line(C, F) == perpendicular_line(C, f)
By line_definition on A, D, perpendicular_line(A, g) we get Line(A, D) == perpendicular_line(A, g)
By line_definition on A, G, i we get i == Line(A, G)
By line_definition on C, J, k we get k == Line(C, J)
By line_definition on C, D, g we get g == Line(C, D)
By line_definition on F, K, k we get k == Line(F, K)
By line_definition on D, K, l we get l == Line(D, K)
By line_definition on E, C, h we get h == Line(C, E)
By line_definition on B, F, f we get f == Line(B, F)
By line_definition on G, D, i we get i == Line(D, G)
By line_definition on A, E, h we get h == Line(A, E)
By line_definition on B, E, perpendicular_line(B, h) we get Line(B, E) == perpendicular_line(B, h)
By line_definition on B, D, g we get g == Line(B, D)
By line_definition on B, G, j we get j == Line(B, G)
By circle_definition on J, A, I, c we get c == Circle(A, I, J)
By line_unique_intersection_v1 on k, f, F, A we get A not in k
By line_unique_intersection_v1 on l, k, K, C we get C not in l
By line_unique_intersection_v1 on g, j, B, E we get E not in g
By line_unique_intersection_v1 on h, j, E, G we get G not in h
By line_unique_intersection_v1 on i, g, D, C we get C not in i
By line_unique_intersection_v1 on j, i, G, A we get A not in j
By line_unique_intersection_v1 on i, g, D, B we get B not in i
By line_unique_intersection_v1 on i, f, A, F we get F not in i
By line_unique_intersection_v1 on h, k, C, F we get F not in h
By line_unique_intersection_v1 on i, l, D, I we get I not in i
By line_unique_intersection_v1 on g, k, C, J we get J not in g
By line_unique_intersection_v1 on g, i, D, A we get A not in g
By line_unique_intersection_v1 on j, i, G, D we get D not in j
By line_unique_intersection_v1 on f, k, F, C we get C not in f
By line_unique_intersection_v1 on h, g, C, D we get D not in h
By line_unique_intersection_v1 on k, l, K, I we get I not in k
By line_unique_intersection_v1 on g, l, D, I we get I not in g
By line_unique_intersection_v1 on h, g, C, B we get B not in h
By line_unique_intersection_v1 on h, k, C, K we get K not in h
By between_implies_orientation on B, C, I, A we get orientation(B, C, I) == orientation(B, I, A) mod 360, orientation(B, C, A) == orientation(B, C, I) mod 360
By between_implies_orientation on H, A, I, C we get orientation(H, A, I) == orientation(H, I, C) mod 360, orientation(H, A, C) == orientation(H, A, I) mod 360
By between_implies_orientation on D, A, I, C we get orientation(D, A, I) == orientation(D, I, C) mod 360, orientation(D, A, C) == orientation(D, A, I) mod 360
By between_implies_orientation on D, C, H, G we get orientation(D, C, H) == orientation(D, H, G) mod 360, orientation(D, C, G) == orientation(D, C, H) mod 360
By angles_on_chord on J, A, I, H, c we get coangle(J, H, A) == coangle(J, I, A) mod 360
By angles_on_chord on I, A, J, H, c we get coangle(I, H, A) == coangle(I, J, A) mod 360
By in_imply_collinear on G, E, B we get collinear(B, E, G)
By in_imply_collinear on K, C, F we get collinear(C, F, K)
By in_imply_collinear on K, D, I we get collinear(D, I, K)
By in_imply_collinear on J, F, C we get collinear(C, F, J)
By in_imply_collinear on D, B, C we get collinear(B, C, D)
By in_imply_collinear on G, D, A we get collinear(A, D, G)
By in_imply_collinear on F, A, B we get collinear(A, B, F)
By collinear_definition on I, C, A we get C in Line(A, I), A in Line(C, I), Line(A, I) == Line(C, I), 0 == 2 * angle(C, I, A) mod 360
By collinear_definition on C, I, A we get I in Line(A, C), A in Line(C, I), Line(A, C) == Line(C, I), 0 == 2 * angle(I, C, A) mod 360
By log_of_2_times_distance on G, C, H, C we get log(distance(C, G)) == 0.6931471805599453 + log(distance(C, H))
By collinear_definition on C, H, G we get H in Line(C, G), G in Line(C, H), Line(C, G) == Line(C, H), 0 == 2 * angle(H, C, G) mod 360
By log_of_2_times_distance on A, C, C, I we get log(distance(A, C)) == 0.6931471805599453 + log(distance(C, I))
By isosceles_triangle_properties on H, C, G we get distance(C, H) == distance(G, H), angle(C, G, H) == angle(H, C, G) mod 360, orientation(H, C, G) == angle(H, C, G) + halfangle(G, H, C) mod 360
By isosceles_triangle_properties on I, C, A we get distance(A, I) == distance(C, I), angle(C, A, I) == angle(I, C, A) mod 360, orientation(I, C, A) == angle(I, C, A) + halfangle(A, I, C) mod 360
By perpendicular_direction_conditions_v0_r on B, G, A, I we get 180 == 2 * direction(B, G) - 2 * direction(A, I) mod 360
By perpendicular_direction_conditions_v0_r on G, E, I, C we get 180 == 2 * direction(G, E) - 2 * direction(I, C) mod 360
By perpendicular_direction_conditions_v0_r on E, B, C, I we get 180 == 2 * direction(E, B) - 2 * direction(C, I) mod 360
By in_imply_collinear on K, C, J we get collinear(C, J, K)
By not_in_line_equivalent_to_not_collinear_v0 on G, C, A we get not_collinear(A, C, G), exists(Line(A, C))
By orientations_are_cyclic on D, A, I we get orientation(A, I, D) == orientation(D, A, I) mod 360, orientation(D, A, I) == orientation(I, D, A) mod 360
By in_imply_collinear on E, I, A we get collinear(A, E, I)
By not_in_line_equivalent_to_not_collinear_v0 on B, E, A we get not_collinear(A, B, E), exists(Line(A, E))
By not_in_line_equivalent_to_not_collinear_v0 on A, B, D we get not_collinear(A, B, D), exists(Line(B, D))
By orientations_are_cyclic on H, C, G we get orientation(C, G, H) == orientation(H, C, G) mod 360, orientation(G, H, C) == orientation(H, C, G) mod 360
By in_imply_collinear on E, C, I we get collinear(C, E, I)
By reverse_direction on C, G we get 180 == direction(C, G) - direction(G, C) mod 360
By orientations_are_cyclic on J, A, I we get orientation(A, I, J) == orientation(J, A, I) mod 360, orientation(I, J, A) == orientation(J, A, I) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on C, K, D we get not_collinear(C, D, K), exists(Line(D, K))
By not_in_line_equivalent_to_not_collinear_v0 on I, B, C we get not_collinear(B, C, I), exists(Line(B, C))
By not_in_line_equivalent_to_not_collinear_v0 on A, C, F we get not_collinear(A, C, F), exists(Line(C, F))
By orientations_are_cyclic on D, A, C we get orientation(A, C, D) == orientation(D, A, C) mod 360, orientation(C, D, A) == orientation(D, A, C) mod 360
By orientations_are_cyclic on D, C, G we get orientation(C, G, D) == orientation(D, C, G) mod 360, orientation(D, C, G) == orientation(G, D, C) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on F, A, D we get not_collinear(A, D, F), exists(Line(A, D))
By angles_equality_imply_halfangles_equality on A, I, C, G, H, C we get halfangle(A, I, C) == halfangle(G, H, C) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on C, F, B we get not_collinear(B, C, F), exists(Line(B, F))
By not_in_line_equivalent_to_not_collinear_v0 on D, B, E we get not_collinear(B, D, E), exists(Line(B, E))
By not_in_line_equivalent_to_not_collinear_v0 on E, C, B we get not_collinear(B, C, E), exists(Line(B, C))
By not_in_line_equivalent_to_not_collinear_v0 on C, G, D we get not_collinear(C, D, G), exists(Line(D, G))
By orientations_are_cyclic on D, H, G we get orientation(D, H, G) == orientation(H, G, D) mod 360, orientation(D, H, G) == orientation(G, D, H) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on K, E, C we get not_collinear(C, E, K), exists(Line(C, E))
By reverse_orientation on J, I, A we get orientation(J, I, A) == 0 - orientation(A, I, J) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on I, D, A we get not_collinear(A, D, I), exists(Line(A, D))
By not_in_line_equivalent_to_not_collinear_v0 on B, D, G we get not_collinear(B, D, G), exists(Line(D, G))
By orientations_are_cyclic on I, C, A we get orientation(C, A, I) == orientation(I, C, A) mod 360, orientation(A, I, C) == orientation(I, C, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on A, G, B we get not_collinear(A, B, G), exists(Line(B, G))
By orientations_are_cyclic on D, C, A we get orientation(C, A, D) == orientation(D, C, A) mod 360, orientation(A, D, C) == orientation(D, C, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on F, E, C we get not_collinear(C, E, F), exists(Line(C, E))
By reverse_direction on C, A we get 180 == direction(C, A) - direction(A, C) mod 360
By orientations_are_cyclic on H, A, I we get orientation(A, I, H) == orientation(H, A, I) mod 360, orientation(H, A, I) == orientation(I, H, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on A, C, J we get not_collinear(A, C, J), exists(Line(C, J))
By not_in_line_equivalent_to_not_collinear_v0 on D, A, E we get not_collinear(A, D, E), exists(Line(A, E))
By orientations_are_cyclic on H, A, C we get orientation(A, C, H) == orientation(H, A, C) mod 360, orientation(C, H, A) == orientation(H, A, C) mod 360
By not_in_line_equivalent_to_not_collinear_v0_r on H, A, I we get H not in Line(A, I)
By orientations_are_cyclic on B, C, A we get orientation(B, C, A) == orientation(C, A, B) mod 360, orientation(A, B, C) == orientation(B, C, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on J, C, B we get not_collinear(B, C, J), exists(Line(B, C))
By not_in_line_equivalent_to_not_collinear_v0 on D, E, G we get not_collinear(D, E, G), exists(Line(E, G))
By not_in_line_equivalent_to_not_collinear_v0 on I, C, F we get not_collinear(C, F, I), exists(Line(C, F))
By orientations_are_cyclic on J, A, C we get orientation(A, C, J) == orientation(J, A, C) mod 360, orientation(C, J, A) == orientation(J, A, C) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on J, D, C we get not_collinear(C, D, J), exists(Line(C, D))
By perpendicular_direction_conditions_v0_r on J, C, A, B we get 180 == 2 * direction(J, C) - 2 * direction(A, B) mod 360
By perpendicular_direction_conditions_v0_r on A, F, J, C we get 180 == 2 * direction(A, F) - 2 * direction(J, C) mod 360
By perpendicular_direction_conditions_v0_r on D, G, B, C we get 180 == 2 * direction(D, G) - 2 * direction(B, C) mod 360
By perpendicular_direction_conditions_v0_r on A, D, B, C we get 180 == 2 * direction(A, D) - 2 * direction(B, C) mod 360
By perpendicular_direction_conditions_v0_r on F, K, F, A we get 180 == 2 * direction(F, K) - 2 * direction(F, A) mod 360
By perpendicular_direction_conditions_v0_r on G, B, C, E we get 180 == 2 * direction(G, B) - 2 * direction(C, E) mod 360
By perpendicular_direction_conditions_v0_r on F, A, C, K we get 180 == 2 * direction(F, A) - 2 * direction(C, K) mod 360
By perpendicular_direction_conditions_v0_r on B, F, J, F we get 180 == 2 * direction(B, F) - 2 * direction(J, F) mod 360
By perpendicular_direction_conditions_v0_r on A, F, F, K we get 180 == 2 * direction(A, F) - 2 * direction(F, K) mod 360
By perpendicular_direction_conditions_v0_r on J, F, F, B we get 180 == 2 * direction(J, F) - 2 * direction(F, B) mod 360
By perpendicular_direction_conditions_v0_r on C, J, F, B we get 180 == 2 * direction(C, J) - 2 * direction(F, B) mod 360
By perpendicular_direction_conditions_v0_r on B, F, C, F we get 180 == 2 * direction(B, F) - 2 * direction(C, F) mod 360
By perpendicular_direction_conditions_v0_r on G, A, D, B we get 180 == 2 * direction(G, A) - 2 * direction(D, B) mod 360
By perpendicular_angle_conditions_v0 on A, E, B we get 0 == coangle(A, E, B) mod 360
By coangle_definition_v1 on J, I, A we get angle(J, I, A) == coangle(J, I, A) + orientation(J, I, A) mod 360
By perpendicular_angle_conditions_v0 on A, D, B we get 0 == coangle(A, D, B) mod 360
By perpendicular_angle_conditions_v0 on C, D, A we get 0 == coangle(C, D, A) mod 360
By perpendicular_angle_conditions_v0 on G, D, C we get 0 == coangle(G, D, C) mod 360
By perpendicular_angle_conditions_v0 on G, E, A we get 0 == coangle(G, E, A) mod 360
By perpendicular_angle_conditions_v0 on G, E, C we get 0 == coangle(G, E, C) mod 360
By angle_equality_conversions_v0 on G, H, C, A, I, C we get coangle(A, I, C) == coangle(G, H, C) mod 360, orientation(A, I, C) == orientation(G, H, C) mod 360
By collinear_definition on D, I, K we get I in Line(D, K), K in Line(D, I), Line(D, I) == Line(D, K), 0 == 2 * angle(I, D, K) mod 360
By coangle_definition_v1 on I, J, A we get angle(I, J, A) == coangle(I, J, A) + orientation(I, J, A) mod 360
By coangle_definition_v1 on I, H, A we get angle(I, H, A) == coangle(I, H, A) + orientation(I, H, A) mod 360
By right_triangle_circumcenter_v1 on A, D, C we get midpoint(A, C) == circumcenter(A, C, D)
By concyclic_sufficient_conditions on G, E, C, D we get concyclic(C, D, E, G)
By concyclic_sufficient_conditions on A, D, B, E we get concyclic(A, B, D, E)
By reverse_orientation on A, D, C we get orientation(A, D, C) == 0 - orientation(C, D, A) mod 360
By reverse_orientation on D, C, G we get orientation(D, C, G) == 0 - orientation(G, C, D) mod 360
By reverse_direction on B, C we get 180 == direction(B, C) - direction(C, B) mod 360
By reverse_direction on I, J we get 180 == direction(I, J) - direction(J, I) mod 360
By reverse_direction on D, G we get 180 == direction(D, G) - direction(G, D) mod 360
By coangle_definition_v1 on C, D, A we get angle(C, D, A) == coangle(C, D, A) + orientation(C, D, A) mod 360
By reverse_direction on D, I we get 180 == direction(D, I) - direction(I, D) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on H, A, C we get not_collinear(A, C, H), exists(Line(A, C))
By reverse_direction on D, C we get 180 == direction(D, C) - direction(C, D) mod 360
By reverse_direction on D, B we get 180 == direction(D, B) - direction(B, D) mod 360
By reverse_direction on G, E we get 180 == direction(G, E) - direction(E, G) mod 360
By sas_similarity on A, C, G, I, C, H we get similar_triangles(A, C, G, I, C, H)
By reverse_direction on A, B we get 180 == direction(A, B) - direction(B, A) mod 360
By reverse_direction on E, B we get 180 == direction(E, B) - direction(B, E) mod 360
By reverse_direction on C, J we get 180 == direction(C, J) - direction(J, C) mod 360
By coangle_definition_v1 on G, D, C we get angle(G, D, C) == coangle(G, D, C) + orientation(G, D, C) mod 360
By coangle_definition_v1 on A, E, B we get angle(A, E, B) == coangle(A, E, B) + orientation(A, E, B) mod 360
By coangle_definition_v1 on G, E, A we get angle(G, E, A) == coangle(G, E, A) + orientation(G, E, A) mod 360
By coangle_definition_v1 on A, D, B we get angle(A, D, B) == coangle(A, D, B) + orientation(A, D, B) mod 360
By reverse_direction on G, B we get 180 == direction(G, B) - direction(B, G) mod 360
By same_angle on C, A, I, F we get coangle(A, C, F) == coangle(I, C, F) mod 360
By same_angle on C, A, I, J we get coangle(A, C, J) == coangle(I, C, J) mod 360
By same_angle on B, G, E, D we get coangle(E, B, D) == coangle(G, B, D) mod 360
By same_angle on C, I, E, F we get coangle(E, C, F) == coangle(I, C, F) mod 360
By same_angle on C, J, F, B we get coangle(F, C, B) == coangle(J, C, B) mod 360
By same_angle on J, C, K, A we get coangle(C, J, A) == coangle(K, J, A) mod 360
By same_angle on C, K, F, D we get coangle(F, C, D) == coangle(K, C, D) mod 360
By same_angle on C, J, K, D we get coangle(J, C, D) == coangle(K, C, D) mod 360
By same_angle on C, E, I, K we get coangle(E, C, K) == coangle(I, C, K) mod 360
By same_angle on A, F, B, D we get coangle(B, A, D) == coangle(F, A, D) mod 360
By same_angle on B, E, G, A we get coangle(E, B, A) == coangle(G, B, A) mod 360
By same_angle on G, D, A, E we get coangle(A, G, E) == coangle(D, G, E) mod 360
By same_angle on D, I, K, A we get coangle(I, D, A) == coangle(K, D, A) mod 360
By same_angle on G, D, A, B we get coangle(A, G, B) == coangle(D, G, B) mod 360
By same_angle on G, C, H, D we get coangle(C, G, D) == coangle(H, G, D) mod 360
By same_angle on C, G, H, D we get coangle(G, C, D) == coangle(H, C, D) mod 360
By same_angle on C, B, D, I we get coangle(B, C, I) == coangle(D, C, I) mod 360
By angle_to_center on C, A, D, Circle(A, C, D) we get coangle(C, A, D) == halfangle(C, center(Circle(A, C, D)), D) - orientation(C, center(Circle(A, C, D)), D) mod 360
By divide_by_2_two_angles on E, C, K, A, C, F we get coangle(A, C, F) == coangle(E, C, K) mod 360
By divide_by_2_two_angles on F, C, B, F, C, D we get coangle(F, C, B) == coangle(F, C, D) mod 360
By divide_by_2_two_angles on G, B, A, I, C, K we get coangle(G, B, A) == coangle(I, C, K) mod 360
By divide_by_2_two_angles on E, C, F, I, C, J we get coangle(E, C, F) == coangle(I, C, J) mod 360
By orientations_are_cyclic on A, E, B we get orientation(A, E, B) == orientation(E, B, A) mod 360, orientation(A, E, B) == orientation(B, A, E) mod 360
By divide_by_2_two_angles on D, G, B, D, C, I we get coangle(D, C, I) == coangle(D, G, B) mod 360
By divide_by_2_two_angles on J, C, B, F, A, D we get coangle(F, A, D) == coangle(J, C, B) mod 360
By divide_by_2_two_angles on B, C, E, A, G, B we get coangle(A, G, B) == coangle(B, C, E) mod 360
By coangle_definition_v1 on B, C, I we get angle(B, C, I) == coangle(B, C, I) + orientation(B, C, I) mod 360
By divide_by_2_two_angles on A, B, D, A, B, C we get coangle(A, B, C) == coangle(A, B, D) mod 360
By coangle_definition_v1 on G, B, D we get angle(G, B, D) == coangle(G, B, D) + orientation(G, B, D) mod 360
By divide_by_2_two_angles on E, B, D, C, A, D we get coangle(C, A, D) == coangle(E, B, D) mod 360
By divide_by_2_two_angles on D, G, E, B, C, E we get coangle(B, C, E) == coangle(D, G, E) mod 360
By coangle_definition_v1 on G, C, D we get angle(G, C, D) == coangle(G, C, D) + orientation(G, C, D) mod 360
By coangle_definition_v1 on A, C, J we get angle(A, C, J) == coangle(A, C, J) + orientation(A, C, J) mod 360
By coangle_definition_v1 on H, G, D we get angle(H, G, D) == coangle(H, G, D) + orientation(H, G, D) mod 360
By coangle_definition_v1 on B, A, D we get angle(B, A, D) == coangle(B, A, D) + orientation(B, A, D) mod 360
By coangle_definition_v0 on C, A, D we get angle(C, A, D) == coangle(C, A, D) + orientation(C, A, D) mod 360
By coangle_definition_v1 on E, B, A we get angle(E, B, A) == coangle(E, B, A) + orientation(E, B, A) mod 360
By coangle_definition_v1 on D, G, B we get angle(D, G, B) == coangle(D, G, B) + orientation(D, G, B) mod 360
By orientations_are_cyclic on B, D, G we get orientation(B, D, G) == orientation(D, G, B) mod 360, orientation(B, D, G) == orientation(G, B, D) mod 360
By orientations_are_cyclic on A, D, B we get orientation(A, D, B) == orientation(D, B, A) mod 360, orientation(A, D, B) == orientation(B, A, D) mod 360
By coangle_definition_v0 on A, B, C we get angle(A, B, C) == coangle(A, B, C) + orientation(A, B, C) mod 360
By coangle_definition_v0 on I, D, A we get angle(I, D, A) == coangle(I, D, A) + orientation(I, D, A) mod 360
By orientations_are_cyclic on G, E, A we get orientation(E, A, G) == orientation(G, E, A) mod 360, orientation(A, G, E) == orientation(G, E, A) mod 360
By coangle_definition_v0 on A, G, E we get angle(A, G, E) == coangle(A, G, E) + orientation(A, G, E) mod 360
By coangle_definition_v1 on C, J, A we get angle(C, J, A) == coangle(C, J, A) + orientation(C, J, A) mod 360
By concyclic_definition_0 on D, B, A, E we get E in Circle(A, B, D)
By concyclic_definition_1 on G, C, E, D we get Circle(C, D, E) == Circle(C, E, G)
By coangle_definition_v0 on C, H, A we get angle(C, H, A) == coangle(C, H, A) + orientation(C, H, A) mod 360
By angles_on_chord on A, D, B, E, Circle(A, B, D) we get coangle(A, B, D) == coangle(A, E, D) mod 360
By angles_on_chord on C, D, E, G, Circle(C, D, E) we get coangle(C, E, D) == coangle(C, G, D) mod 360
By same_angle on E, A, I, D we get coangle(A, E, D) == coangle(I, E, D) mod 360
By same_angle on E, C, I, D we get coangle(C, E, D) == coangle(I, E, D) mod 360
By same_angle_converse on C, H, J, D we get collinear(C, H, J)
By same_angle on H, C, J, A we get coangle(C, H, A) == coangle(J, H, A) mod 360
By concyclic_sufficient_conditions on K, J, A, D we get concyclic(A, D, J, K)
