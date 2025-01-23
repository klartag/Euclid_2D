Assumptions:
A, B, C, D, E, F, G, H, I, J, K: Point
f, g, h, i, j: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I, J, K)
distinct(f, g, h, i, j)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
G == line_intersection(i, j)
H == midpoint(A, G)
I == midpoint(C, A)
c == Circle(D, I, H)
J == center(c)
K == midpoint(E, F)

Need to prove:
collinear(H, K, J)

Proof:
By line_definition on G, A, i we get i == Line(A, G)
By line_definition on F, A, f we get f == Line(A, F)
By line_definition on B, F, f we get f == Line(B, F)
By line_definition on G, D, i we get i == Line(D, G)
By line_definition on D, B, g we get g == Line(B, D)
By line_definition on G, B, j we get j == Line(B, G)
By line_definition on E, A, h we get h == Line(A, E)
By line_definition on C, D, g we get g == Line(C, D)
By line_definition on A, D, perpendicular_line(A, g) we get Line(A, D) == perpendicular_line(A, g)
By line_definition on G, E, j we get j == Line(E, G)
By line_definition on B, E, perpendicular_line(B, h) we get Line(B, E) == perpendicular_line(B, h)
By line_definition on C, F, perpendicular_line(C, f) we get Line(C, F) == perpendicular_line(C, f)
By line_definition on E, C, h we get h == Line(C, E)
By line_unique_intersection_v1 on j, h, E, A we get A not in j
By line_unique_intersection_v1 on i, h, A, C we get C not in i
By line_unique_intersection_v1 on i, h, A, E we get E not in i
By line_unique_intersection_v1 on i, f, A, F we get F not in i
By line_unique_intersection_v1 on h, g, C, D we get D not in h
By line_unique_intersection_v1 on j, f, B, F we get F not in j
By line_unique_intersection_v1 on g, i, D, A we get A not in g
By line_unique_intersection_v1 on g, j, B, E we get E not in g
By line_unique_intersection_v1 on h, j, E, B we get B not in h
By line_unique_intersection_v1 on i, f, A, B we get B not in i
By line_unique_intersection_v1 on g, f, B, F we get F not in g
By line_unique_intersection_v1 on f, i, A, G we get G not in f
By line_unique_intersection_v1 on j, i, G, D we get D not in j
By line_unique_intersection_v1 on h, f, A, F we get F not in h
By line_unique_intersection_v1 on h, j, E, G we get G not in h
By between_implies_orientation on C, G, H, A we get orientation(C, G, H) == orientation(C, H, A) mod 360, orientation(C, G, A) == orientation(C, G, H) mod 360
By between_implies_orientation on B, A, H, G we get orientation(B, A, H) == orientation(B, H, G) mod 360, orientation(B, A, G) == orientation(B, A, H) mod 360
By between_implies_orientation on H, A, I, C we get orientation(H, A, I) == orientation(H, I, C) mod 360, orientation(H, A, C) == orientation(H, A, I) mod 360
By between_implies_orientation on D, C, I, A we get orientation(D, C, I) == orientation(D, I, A) mod 360, orientation(D, C, A) == orientation(D, C, I) mod 360
By between_implies_orientation on F, A, H, G we get orientation(F, A, H) == orientation(F, H, G) mod 360, orientation(F, A, G) == orientation(F, A, H) mod 360
By between_implies_orientation on F, C, I, A we get orientation(F, C, I) == orientation(F, I, A) mod 360, orientation(F, C, A) == orientation(F, C, I) mod 360
By between_implies_orientation on I, A, H, G we get orientation(I, A, H) == orientation(I, H, G) mod 360, orientation(I, A, G) == orientation(I, A, H) mod 360
By between_implies_orientation on E, A, H, G we get orientation(E, A, H) == orientation(E, H, G) mod 360, orientation(E, A, G) == orientation(E, A, H) mod 360
By between_implies_orientation on E, G, H, A we get orientation(E, G, H) == orientation(E, H, A) mod 360, orientation(E, G, A) == orientation(E, G, H) mod 360
By between_implies_orientation on G, C, I, A we get orientation(G, C, I) == orientation(G, I, A) mod 360, orientation(G, C, A) == orientation(G, C, I) mod 360
By between_implies_orientation on A, E, K, F we get orientation(A, E, K) == orientation(A, K, F) mod 360, orientation(A, E, F) == orientation(A, E, K) mod 360
By between_implies_orientation on D, A, I, C we get orientation(D, A, I) == orientation(D, I, C) mod 360, orientation(D, A, C) == orientation(D, A, I) mod 360
By between_implies_orientation on B, G, H, A we get orientation(B, G, H) == orientation(B, H, A) mod 360, orientation(B, G, A) == orientation(B, G, H) mod 360
By between_implies_orientation on F, G, H, A we get orientation(F, G, H) == orientation(F, H, A) mod 360, orientation(F, G, A) == orientation(F, G, H) mod 360
By circle_radius_v0_r on H, c we get radius(c) == distance(H, center(c))
By circle_radius_v0_r on I, c we get radius(c) == distance(I, center(c))
By in_imply_collinear on G, A, D we get collinear(A, D, G)
By in_imply_collinear on G, B, E we get collinear(B, E, G)
By in_imply_collinear on E, C, A we get collinear(A, C, E)
By in_imply_collinear on D, C, B we get collinear(B, C, D)
By in_imply_collinear on F, B, A we get collinear(A, B, F)
By angle_to_center on D, I, H, c we get coangle(D, I, H) == halfangle(D, center(c), H) - orientation(D, center(c), H) mod 360
By angle_to_center on I, H, D, c we get coangle(I, H, D) == halfangle(I, center(c), D) - orientation(I, center(c), D) mod 360
By angle_to_center on I, D, H, c we get coangle(I, D, H) == halfangle(I, center(c), H) - orientation(I, center(c), H) mod 360
By log_of_2_times_distance on A, C, A, I we get log(distance(A, C)) == 0.6931471805599453 + log(distance(A, I))
By collinear_definition on A, C, I we get C in Line(A, I), I in Line(A, C), Line(A, C) == Line(A, I), 0 == 2 * angle(C, A, I) mod 360
By collinear_definition on F, K, E we get K in Line(E, F), E in Line(F, K), Line(E, F) == Line(F, K), 0 == 2 * angle(K, F, E) mod 360
By collinear_definition on G, H, A we get H in Line(A, G), A in Line(G, H), Line(A, G) == Line(G, H), 0 == 2 * angle(H, G, A) mod 360
By collinear_definition on I, C, A we get C in Line(A, I), A in Line(C, I), Line(A, I) == Line(C, I), 0 == 2 * angle(C, I, A) mod 360
By collinear_definition on H, G, A we get G in Line(A, H), A in Line(G, H), Line(A, H) == Line(G, H), 0 == 2 * angle(G, H, A) mod 360
By log_of_2_times_distance on G, A, H, A we get log(distance(A, G)) == 0.6931471805599453 + log(distance(A, H))
By log_of_2_times_distance on F, E, K, E we get log(distance(E, F)) == 0.6931471805599453 + log(distance(E, K))
By isosceles_triangle_properties on K, E, F we get distance(E, K) == distance(F, K), angle(E, F, K) == angle(K, E, F) mod 360, orientation(K, E, F) == angle(K, E, F) + halfangle(F, K, E) mod 360
By isosceles_triangle_properties on I, C, A we get distance(A, I) == distance(C, I), angle(C, A, I) == angle(I, C, A) mod 360, orientation(I, C, A) == angle(I, C, A) + halfangle(A, I, C) mod 360
By isosceles_triangle_properties on I, A, C we get distance(A, I) == distance(C, I), angle(A, C, I) == angle(I, A, C) mod 360, orientation(I, A, C) == angle(I, A, C) + halfangle(C, I, A) mod 360
By isosceles_triangle_properties on K, F, E we get distance(E, K) == distance(F, K), angle(F, E, K) == angle(K, F, E) mod 360, orientation(K, F, E) == angle(K, F, E) + halfangle(E, K, F) mod 360
By isosceles_triangle_properties on H, A, G we get distance(A, H) == distance(G, H), angle(A, G, H) == angle(H, A, G) mod 360, orientation(H, A, G) == angle(H, A, G) + halfangle(G, H, A) mod 360
By line_definition on D, H, i we get i == Line(D, H)
By perpendicular_direction_conditions_v0_r on C, I, B, E we get 180 == 2 * direction(C, I) - 2 * direction(B, E) mod 360
By perpendicular_direction_conditions_v0_r on G, H, C, B we get 180 == 2 * direction(G, H) - 2 * direction(C, B) mod 360
By perpendicular_direction_conditions_v0_r on G, B, I, A we get 180 == 2 * direction(G, B) - 2 * direction(I, A) mod 360
By perpendicular_direction_conditions_v0_r on E, G, A, I we get 180 == 2 * direction(E, G) - 2 * direction(A, I) mod 360
By perpendicular_direction_conditions_v0_r on G, H, C, D we get 180 == 2 * direction(G, H) - 2 * direction(C, D) mod 360
By in_imply_collinear on I, C, E we get collinear(C, E, I)
By in_imply_collinear on D, H, G we get collinear(D, G, H)
By in_imply_collinear on I, E, A we get collinear(A, E, I)
By in_imply_collinear on H, A, D we get collinear(A, D, H)
By not_in_line_equivalent_to_not_collinear_v0 on F, E, B we get not_collinear(B, E, F), exists(Line(B, E))
By not_in_line_equivalent_to_not_collinear_v0 on C, G, D we get not_collinear(C, D, G), exists(Line(D, G))
By orientations_are_cyclic on I, A, C we get orientation(A, C, I) == orientation(I, A, C) mod 360, orientation(C, I, A) == orientation(I, A, C) mod 360
By reverse_direction on C, A we get 180 == direction(C, A) - direction(A, C) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on C, A, H we get not_collinear(A, C, H), exists(Line(A, H))
By reverse_direction on H, G we get 180 == direction(H, G) - direction(G, H) mod 360
By reverse_direction on I, A we get 180 == direction(I, A) - direction(A, I) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on D, E, G we get not_collinear(D, E, G), exists(Line(E, G))
By not_in_line_equivalent_to_not_collinear_v0 on E, A, D we get not_collinear(A, D, E), exists(Line(A, D))
By angles_equality_imply_halfangles_equality on C, I, A, G, H, A we get halfangle(C, I, A) == halfangle(G, H, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on G, A, C we get not_collinear(A, C, G), exists(Line(A, C))
By not_in_line_equivalent_to_not_collinear_v0 on F, I, C we get not_collinear(C, F, I), exists(Line(C, I))
By orientations_are_cyclic on B, C, A we get orientation(B, C, A) == orientation(C, A, B) mod 360, orientation(A, B, C) == orientation(B, C, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on F, E, A we get not_collinear(A, E, F), exists(Line(A, E))
By not_in_line_equivalent_to_not_collinear_v0 on A, C, B we get not_collinear(A, B, C), exists(Line(B, C))
By angles_equality_imply_halfangles_equality on F, K, E, G, H, A we get halfangle(F, K, E) == halfangle(G, H, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on B, A, D we get not_collinear(A, B, D), exists(Line(A, D))
By orientations_are_cyclic on A, E, F we get orientation(A, E, F) == orientation(E, F, A) mod 360, orientation(A, E, F) == orientation(F, A, E) mod 360
By orientations_are_cyclic on H, A, G we get orientation(A, G, H) == orientation(H, A, G) mod 360, orientation(G, H, A) == orientation(H, A, G) mod 360
By angles_equality_imply_halfangles_equality on E, K, F, F, K, E we get halfangle(E, K, F) == halfangle(F, K, E) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on D, C, E we get not_collinear(C, D, E), exists(Line(C, E))
By reverse_direction on F, E we get 180 == direction(F, E) - direction(E, F) mod 360
By orientations_are_cyclic on I, J, H we get orientation(I, J, H) == orientation(J, H, I) mod 360, orientation(H, I, J) == orientation(I, J, H) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on B, H, A we get not_collinear(A, B, H), exists(Line(A, H))
By orientations_are_cyclic on C, H, A we get orientation(C, H, A) == orientation(H, A, C) mod 360, orientation(A, C, H) == orientation(C, H, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on B, G, H we get not_collinear(B, G, H), exists(Line(G, H))
By orientations_are_cyclic on F, C, A we get orientation(C, A, F) == orientation(F, C, A) mod 360, orientation(A, F, C) == orientation(F, C, A) mod 360
By orientations_are_cyclic on D, C, A we get orientation(C, A, D) == orientation(D, C, A) mod 360, orientation(A, D, C) == orientation(D, C, A) mod 360
By orientations_are_cyclic on K, E, F we get orientation(E, F, K) == orientation(K, E, F) mod 360, orientation(F, K, E) == orientation(K, E, F) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on F, B, C we get not_collinear(B, C, F), exists(Line(B, C))
By not_in_line_equivalent_to_not_collinear_v0 on E, H, A we get not_collinear(A, E, H), exists(Line(A, H))
By orientations_are_cyclic on E, G, A we get orientation(E, G, A) == orientation(G, A, E) mod 360, orientation(A, E, G) == orientation(E, G, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on D, B, G we get not_collinear(B, D, G), exists(Line(B, G))
By orientations_are_cyclic on D, A, C we get orientation(A, C, D) == orientation(D, A, C) mod 360, orientation(C, D, A) == orientation(D, A, C) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on G, I, A we get not_collinear(A, G, I), exists(Line(A, I))
By orientations_are_cyclic on B, H, A we get orientation(B, H, A) == orientation(H, A, B) mod 360, orientation(A, B, H) == orientation(B, H, A) mod 360
By orientations_are_cyclic on G, C, A we get orientation(C, A, G) == orientation(G, C, A) mod 360, orientation(A, G, C) == orientation(G, C, A) mod 360
By reverse_direction on H, A we get 180 == direction(H, A) - direction(A, H) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on E, C, B we get not_collinear(B, C, E), exists(Line(B, C))
By orientations_are_cyclic on D, C, I we get orientation(C, I, D) == orientation(D, C, I) mod 360, orientation(D, C, I) == orientation(I, D, C) mod 360
By orientations_are_cyclic on C, G, A we get orientation(C, G, A) == orientation(G, A, C) mod 360, orientation(A, C, G) == orientation(C, G, A) mod 360
By orientations_are_cyclic on D, A, I we get orientation(A, I, D) == orientation(D, A, I) mod 360, orientation(D, A, I) == orientation(I, D, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on D, I, C we get not_collinear(C, D, I), exists(Line(C, I))
By not_in_line_equivalent_to_not_collinear_v0 on E, D, B we get not_collinear(B, D, E), exists(Line(B, D))
By orientations_are_cyclic on F, G, H we get orientation(F, G, H) == orientation(G, H, F) mod 360, orientation(F, G, H) == orientation(H, F, G) mod 360
By orientations_are_cyclic on I, C, A we get orientation(C, A, I) == orientation(I, C, A) mod 360, orientation(A, I, C) == orientation(I, C, A) mod 360
By orientations_are_cyclic on A, K, F we get orientation(A, K, F) == orientation(K, F, A) mod 360, orientation(A, K, F) == orientation(F, A, K) mod 360
By orientations_are_cyclic on B, G, H we get orientation(B, G, H) == orientation(G, H, B) mod 360, orientation(B, G, H) == orientation(H, B, G) mod 360
By orientations_are_cyclic on F, I, A we get orientation(F, I, A) == orientation(I, A, F) mod 360, orientation(A, F, I) == orientation(F, I, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on F, I, A we get not_collinear(A, F, I), exists(Line(A, I))
By orientations_are_cyclic on E, A, G we get orientation(A, G, E) == orientation(E, A, G) mod 360, orientation(E, A, G) == orientation(G, E, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on B, A, I we get not_collinear(A, B, I), exists(Line(A, I))
By orientations_are_cyclic on K, F, E we get orientation(F, E, K) == orientation(K, F, E) mod 360, orientation(E, K, F) == orientation(K, F, E) mod 360
By orientations_are_cyclic on G, I, A we get orientation(G, I, A) == orientation(I, A, G) mod 360, orientation(A, G, I) == orientation(G, I, A) mod 360
By orientations_are_cyclic on D, I, C we get orientation(D, I, C) == orientation(I, C, D) mod 360, orientation(C, D, I) == orientation(D, I, C) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on F, D, C we get not_collinear(C, D, F), exists(Line(C, D))
By orientations_are_cyclic on B, E, F we get orientation(B, E, F) == orientation(E, F, B) mod 360, orientation(B, E, F) == orientation(F, B, E) mod 360
By orientations_are_cyclic on F, H, A we get orientation(F, H, A) == orientation(H, A, F) mod 360, orientation(A, F, H) == orientation(F, H, A) mod 360
By orientations_are_cyclic on B, A, C we get orientation(A, C, B) == orientation(B, A, C) mod 360, orientation(B, A, C) == orientation(C, B, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on A, B, G we get not_collinear(A, B, G), exists(Line(B, G))
By orientations_are_cyclic on B, A, G we get orientation(A, G, B) == orientation(B, A, G) mod 360, orientation(B, A, G) == orientation(G, B, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on B, C, I we get not_collinear(B, C, I), exists(Line(C, I))
By not_in_line_equivalent_to_not_collinear_v0 on G, F, B we get not_collinear(B, F, G), exists(Line(B, F))
By not_in_line_equivalent_to_not_collinear_v0 on F, H, G we get not_collinear(F, G, H), exists(Line(G, H))
By perpendicular_direction_conditions_v0_r on E, A, G, E we get 180 == 2 * direction(E, A) - 2 * direction(G, E) mod 360
By perpendicular_direction_conditions_v0_r on G, E, C, E we get 180 == 2 * direction(G, E) - 2 * direction(C, E) mod 360
By perpendicular_direction_conditions_v0_r on G, D, D, C we get 180 == 2 * direction(G, D) - 2 * direction(D, C) mod 360
By perpendicular_direction_conditions_v0_r on F, C, B, F we get 180 == 2 * direction(F, C) - 2 * direction(B, F) mod 360
By perpendicular_direction_conditions_v0_r on B, A, F, C we get 180 == 2 * direction(B, A) - 2 * direction(F, C) mod 360
By perpendicular_angle_conditions_v0 on C, E, B we get 0 == coangle(C, E, B) mod 360
By reverse_direction on J, H we get 180 == direction(J, H) - direction(H, J) mod 360
By perpendicular_angle_conditions_v0 on C, F, B we get 0 == coangle(C, F, B) mod 360
By perpendicular_angle_conditions_v0 on B, D, A we get 0 == coangle(B, D, A) mod 360
By perpendicular_angle_conditions_v0 on A, D, C we get 0 == coangle(A, D, C) mod 360
By reverse_direction on J, I we get 180 == direction(J, I) - direction(I, J) mod 360
By perpendicular_angle_conditions_v0 on B, E, A we get 0 == coangle(B, E, A) mod 360
By perpendicular_angle_conditions_v0 on G, E, A we get 0 == coangle(G, E, A) mod 360
By perpendicular_angle_conditions_v0 on G, D, B we get 0 == coangle(G, D, B) mod 360
By perpendicular_angle_conditions_v0 on A, F, C we get 0 == coangle(A, F, C) mod 360
By perpendicular_angle_conditions_v0 on C, D, G we get 0 == coangle(C, D, G) mod 360
By perpendicular_angle_conditions_v0 on G, E, C we get 0 == coangle(G, E, C) mod 360
By perpendicular_angle_conditions_v0 on B, E, C we get 0 == coangle(B, E, C) mod 360
By angle_equality_conversions_v0 on E, K, F, G, H, A we get coangle(E, K, F) == coangle(G, H, A) mod 360, orientation(E, K, F) == orientation(G, H, A) mod 360
By angle_equality_conversions_v0 on F, K, E, C, I, A we get coangle(C, I, A) == coangle(F, K, E) mod 360, orientation(C, I, A) == orientation(F, K, E) mod 360
By coangle_definition_v1 on I, D, H we get angle(I, D, H) == coangle(I, D, H) + orientation(I, D, H) mod 360
By coangle_definition_v1 on I, H, D we get angle(I, H, D) == coangle(I, H, D) + orientation(I, H, D) mod 360
By coangle_definition_v1 on D, I, H we get angle(D, I, H) == coangle(D, I, H) + orientation(D, I, H) mod 360
By right_triangle_circumcenter_v1 on G, E, A we get midpoint(A, G) == circumcenter(A, E, G)
By right_triangle_circumcenter_v1 on A, D, C we get midpoint(A, C) == circumcenter(A, C, D)
By right_triangle_circumcenter_v1 on A, F, C we get midpoint(A, C) == circumcenter(A, C, F)
By isosceles_triangle_properties on J, I, H we get distance(H, J) == distance(I, J), angle(I, H, J) == angle(J, I, H) mod 360, orientation(J, I, H) == angle(J, I, H) + halfangle(H, J, I) mod 360
By isosceles_triangle_properties on J, H, I we get distance(H, J) == distance(I, J), angle(H, I, J) == angle(J, H, I) mod 360, orientation(J, H, I) == angle(J, H, I) + halfangle(I, J, H) mod 360
By concyclic_sufficient_conditions on C, E, B, F we get concyclic(B, C, E, F)
By concyclic_sufficient_conditions on B, D, A, E we get concyclic(A, B, D, E)
By perpendicular_direction_conditions_v0_r on B, D, H, D we get 180 == 2 * direction(B, D) - 2 * direction(H, D) mod 360
By circle_radius_v0_r on E, Circle(A, E, G) we get radius(Circle(A, E, G)) == distance(E, center(Circle(A, E, G)))
By circle_radius_v0_r on G, Circle(A, E, G) we get radius(Circle(A, E, G)) == distance(G, center(Circle(A, E, G)))
By reverse_direction on F, C we get 180 == direction(F, C) - direction(C, F) mod 360
By reverse_orientation on G, H, B we get orientation(G, H, B) == 0 - orientation(B, H, G) mod 360
By coangle_definition_v1 on A, F, C we get angle(A, F, C) == coangle(A, F, C) + orientation(A, F, C) mod 360
By reverse_orientation on C, A, G we get orientation(C, A, G) == 0 - orientation(G, A, C) mod 360
By reverse_direction on B, D we get 180 == direction(B, D) - direction(D, B) mod 360
By reverse_orientation on F, B, E we get orientation(F, B, E) == 0 - orientation(E, B, F) mod 360
By reverse_orientation on E, A, G we get orientation(E, A, G) == 0 - orientation(G, A, E) mod 360
By coangle_definition_v1 on C, E, B we get angle(C, E, B) == coangle(C, E, B) + orientation(C, E, B) mod 360
By reverse_orientation on F, A, I we get orientation(F, A, I) == 0 - orientation(I, A, F) mod 360
By reverse_orientation on C, D, A we get orientation(C, D, A) == 0 - orientation(A, D, C) mod 360
By reverse_direction on B, E we get 180 == direction(B, E) - direction(E, B) mod 360
By reverse_orientation on B, C, A we get orientation(B, C, A) == 0 - orientation(A, C, B) mod 360
By reverse_orientation on G, H, F we get orientation(G, H, F) == 0 - orientation(F, H, G) mod 360
By coangle_definition_v1 on A, D, C we get angle(A, D, C) == coangle(A, D, C) + orientation(A, D, C) mod 360
By reverse_direction on B, F we get 180 == direction(B, F) - direction(F, B) mod 360
By reverse_direction on E, A we get 180 == direction(E, A) - direction(A, E) mod 360
By reverse_orientation on F, A, E we get orientation(F, A, E) == 0 - orientation(E, A, F) mod 360
By reverse_direction on G, B we get 180 == direction(G, B) - direction(B, G) mod 360
By reverse_direction on E, G we get 180 == direction(E, G) - direction(G, E) mod 360
By reverse_direction on C, B we get 180 == direction(C, B) - direction(B, C) mod 360
By coangle_definition_v1 on G, E, A we get angle(G, E, A) == coangle(G, E, A) + orientation(G, E, A) mod 360
By reverse_direction on B, A we get 180 == direction(B, A) - direction(A, B) mod 360
By coangle_definition_v1 on C, D, G we get angle(C, D, G) == coangle(C, D, G) + orientation(C, D, G) mod 360
By coangle_definition_v1 on G, E, C we get angle(G, E, C) == coangle(G, E, C) + orientation(G, E, C) mod 360
By coangle_definition_v1 on G, D, B we get angle(G, D, B) == coangle(G, D, B) + orientation(G, D, B) mod 360
By reverse_direction on F, A we get 180 == direction(F, A) - direction(A, F) mod 360
By reverse_direction on D, A we get 180 == direction(D, A) - direction(A, D) mod 360
By reverse_direction on C, E we get 180 == direction(C, E) - direction(E, C) mod 360
By coangle_definition_v1 on C, F, B we get angle(C, F, B) == coangle(C, F, B) + orientation(C, F, B) mod 360
By coangle_definition_v1 on B, E, C we get angle(B, E, C) == coangle(B, E, C) + orientation(B, E, C) mod 360
By reverse_direction on C, D we get 180 == direction(C, D) - direction(D, C) mod 360
By angle_to_center on A, F, C, Circle(A, C, F) we get coangle(A, F, C) == halfangle(A, center(Circle(A, C, F)), C) - orientation(A, center(Circle(A, C, F)), C) mod 360
By same_angle on A, D, H, E we get coangle(D, A, E) == coangle(H, A, E) mod 360
By same_angle on G, D, A, E we get coangle(A, G, E) == coangle(D, G, E) mod 360
By same_angle on G, D, A, B we get coangle(A, G, B) == coangle(D, G, B) mod 360
By same_angle on G, B, E, D we get coangle(B, G, D) == coangle(E, G, D) mod 360
By same_angle on A, D, G, B we get coangle(D, A, B) == coangle(G, A, B) mod 360
By same_angle on C, E, I, D we get coangle(E, C, D) == coangle(I, C, D) mod 360
By same_angle on C, I, E, F we get coangle(E, C, F) == coangle(I, C, F) mod 360
By same_angle on C, E, A, D we get coangle(A, C, D) == coangle(E, C, D) mod 360
By same_angle on B, G, E, A we get coangle(E, B, A) == coangle(G, B, A) mod 360
By same_angle on A, E, I, H we get coangle(E, A, H) == coangle(I, A, H) mod 360
By same_angle on G, H, D, B we get coangle(D, G, B) == coangle(H, G, B) mod 360
By same_angle on C, D, B, A we get coangle(B, C, A) == coangle(D, C, A) mod 360
By same_angle on A, G, H, I we get coangle(G, A, I) == coangle(H, A, I) mod 360
By same_angle on B, D, C, E we get coangle(C, B, E) == coangle(D, B, E) mod 360
By same_angle on A, G, D, C we get coangle(D, A, C) == coangle(G, A, C) mod 360
By same_angle on A, B, F, G we get coangle(B, A, G) == coangle(F, A, G) mod 360
By same_angle on A, H, D, C we get coangle(D, A, C) == coangle(H, A, C) mod 360
By same_angle on A, H, G, B we get coangle(G, A, B) == coangle(H, A, B) mod 360
By same_angle on A, B, F, I we get coangle(B, A, I) == coangle(F, A, I) mod 360
By same_angle on A, E, I, F we get coangle(E, A, F) == coangle(I, A, F) mod 360
By same_angle on C, B, D, F we get coangle(B, C, F) == coangle(D, C, F) mod 360
By same_angle on C, A, I, B we get coangle(A, C, B) == coangle(I, C, B) mod 360
By same_angle on F, E, K, A we get coangle(E, F, A) == coangle(K, F, A) mod 360
By same_angle on A, C, I, B we get coangle(C, A, B) == coangle(I, A, B) mod 360
By coangle_definition_v0 on H, A, I we get angle(H, A, I) == coangle(H, A, I) + orientation(H, A, I) mod 360
By coangle_definition_v0 on J, I, D we get angle(J, I, D) == coangle(J, I, D) + orientation(J, I, D) mod 360
By coangle_definition_v0 on I, A, H we get angle(I, A, H) == coangle(I, A, H) + orientation(I, A, H) mod 360
By coangle_definition_v0 on J, I, H we get angle(J, I, H) == coangle(J, I, H) + orientation(J, I, H) mod 360
By angle_to_center on A, C, D, Circle(A, C, D) we get coangle(A, C, D) == halfangle(A, center(Circle(A, C, D)), D) - orientation(A, center(Circle(A, C, D)), D) mod 360
By angle_to_center on E, G, A, Circle(A, E, G) we get coangle(E, G, A) == halfangle(E, center(Circle(A, E, G)), A) - orientation(E, center(Circle(A, E, G)), A) mod 360
By angle_to_center on C, A, D, Circle(A, C, D) we get coangle(C, A, D) == halfangle(C, center(Circle(A, C, D)), D) - orientation(C, center(Circle(A, C, D)), D) mod 360
By sas_similarity on G, A, C, H, A, I we get similar_triangles(A, C, G, A, I, H)
By orthocenter_concurrency on A, C, B we get orthocenter(A, B, C) in altitude(A, B, C), orthocenter(A, B, C) in altitude(C, A, B), orthocenter(A, B, C) in altitude(B, A, C)
By divide_by_2_two_angles on D, B, E, G, A, C we get coangle(D, B, E) == coangle(G, A, C) mod 360
By divide_by_2_two_angles on D, B, E, H, A, E we get coangle(D, B, E) == coangle(H, A, E) mod 360
By divide_by_2_two_angles on I, A, H, C, A, D we get coangle(C, A, D) == coangle(I, A, H) mod 360
By coangle_definition_v0 on E, A, H we get angle(E, A, H) == coangle(E, A, H) + orientation(E, A, H) mod 360
By divide_by_2_two_angles on B, C, A, H, G, B we get coangle(B, C, A) == coangle(H, G, B) mod 360
By divide_by_2_two_angles on D, C, I, A, G, E we get coangle(A, G, E) == coangle(D, C, I) mod 360
By divide_by_2_two_angles on A, G, B, D, G, E we get coangle(A, G, B) == coangle(D, G, E) mod 360
By divide_by_2_two_angles on I, C, B, I, C, D we get coangle(I, C, B) == coangle(I, C, D) mod 360
By divide_by_2_two_angles on D, C, A, J, I, H we get coangle(D, C, A) == coangle(J, I, H) mod 360
By divide_by_2_two_angles on I, A, F, I, A, B we get coangle(I, A, B) == coangle(I, A, F) mod 360
By divide_by_2_two_angles on B, G, D, A, C, B we get coangle(A, C, B) == coangle(B, G, D) mod 360
By coangle_definition_v0 on K, F, A we get angle(K, F, A) == coangle(K, F, A) + orientation(K, F, A) mod 360
By divide_by_2_two_angles on I, D, H, G, A, I we get coangle(G, A, I) == coangle(I, D, H) mod 360
By coangle_definition_v0 on E, G, A we get angle(E, G, A) == coangle(E, G, A) + orientation(E, G, A) mod 360
By divide_by_2_two_angles on B, C, E, D, C, I we get coangle(B, C, E) == coangle(D, C, I) mod 360
By divide_by_2_two_angles on B, A, C, B, A, E we get coangle(B, A, C) == coangle(B, A, E) mod 360
By divide_by_2_two_angles on E, G, A, E, G, D we get coangle(E, G, A) == coangle(E, G, D) mod 360
By coangle_definition_v0 on A, C, B we get angle(A, C, B) == coangle(A, C, B) + orientation(A, C, B) mod 360
By angles_equality_imply_halfangles_equality on C, I, D, H, J, I we get halfangle(C, I, D) == halfangle(H, J, I) mod 360
By divide_by_2_two_angles on D, A, B, D, C, F we get coangle(D, A, B) == coangle(D, C, F) mod 360
By coangle_definition_v0 on H, A, B we get angle(H, A, B) == coangle(H, A, B) + orientation(H, A, B) mod 360
By coangle_definition_v0 on E, F, B we get angle(E, F, B) == coangle(E, F, B) + orientation(E, F, B) mod 360
By divide_by_2_two_angles on H, A, C, D, B, G we get coangle(D, B, G) == coangle(H, A, C) mod 360
By divide_by_2_two_angles on G, A, B, H, A, F we get coangle(G, A, B) == coangle(H, A, F) mod 360
By angle_equality_conversions_v0 on B, A, I, B, A, C we get coangle(B, A, C) == coangle(B, A, I) mod 360, orientation(B, A, C) == orientation(B, A, I) mod 360
By angles_equality_imply_halfangles_equality on E, H, A, A, I, D we get halfangle(A, I, D) == halfangle(E, H, A) mod 360
By coangle_definition_v0 on D, A, E we get angle(D, A, E) == coangle(D, A, E) + orientation(D, A, E) mod 360
By divide_by_2_two_angles on E, F, B, E, F, A we get coangle(E, F, A) == coangle(E, F, B) mod 360
By coangle_definition_v1 on H, A, F we get angle(H, A, F) == coangle(H, A, F) + orientation(H, A, F) mod 360
By coangle_definition_v0 on F, A, I we get angle(F, A, I) == coangle(F, A, I) + orientation(F, A, I) mod 360
By coangle_definition_v1 on E, A, F we get angle(E, A, F) == coangle(E, A, F) + orientation(E, A, F) mod 360
By orientations_are_cyclic on G, D, B we get orientation(D, B, G) == orientation(G, D, B) mod 360, orientation(B, G, D) == orientation(G, D, B) mod 360
By coangle_definition_v1 on B, C, F we get angle(B, C, F) == coangle(B, C, F) + orientation(B, C, F) mod 360
By divide_by_2_two_angles on I, C, F, G, B, A we get coangle(G, B, A) == coangle(I, C, F) mod 360
By coangle_definition_v1 on C, A, B we get angle(C, A, B) == coangle(C, A, B) + orientation(C, A, B) mod 360
By coangle_definition_v0 on F, A, G we get angle(F, A, G) == coangle(F, A, G) + orientation(F, A, G) mod 360
By coangle_definition_v1 on I, C, D we get angle(I, C, D) == coangle(I, C, D) + orientation(I, C, D) mod 360
By orientations_are_cyclic on B, E, C we get orientation(B, E, C) == orientation(E, C, B) mod 360, orientation(B, E, C) == orientation(C, B, E) mod 360
By divide_by_2_two_angles on I, C, F, E, B, F we get coangle(E, B, F) == coangle(I, C, F) mod 360
By coangle_definition_v0 on G, B, A we get angle(G, B, A) == coangle(G, B, A) + orientation(G, B, A) mod 360
By coangle_definition_v0 on E, B, F we get angle(E, B, F) == coangle(E, B, F) + orientation(E, B, F) mod 360
By coangle_definition_v0 on B, A, C we get angle(B, A, C) == coangle(B, A, C) + orientation(B, A, C) mod 360
By coangle_definition_v1 on B, C, E we get angle(B, C, E) == coangle(B, C, E) + orientation(B, C, E) mod 360
By orientations_are_cyclic on C, E, B we get orientation(C, E, B) == orientation(E, B, C) mod 360, orientation(B, C, E) == orientation(C, E, B) mod 360
By coangle_definition_v0 on C, B, E we get angle(C, B, E) == coangle(C, B, E) + orientation(C, B, E) mod 360
By coangle_definition_v0 on B, E, F we get angle(B, E, F) == coangle(B, E, F) + orientation(B, E, F) mod 360
By coangle_definition_v1 on E, C, F we get angle(E, C, F) == coangle(E, C, F) + orientation(E, C, F) mod 360
By orientations_are_cyclic on G, E, C we get orientation(E, C, G) == orientation(G, E, C) mod 360, orientation(C, G, E) == orientation(G, E, C) mod 360
By coangle_definition_v0 on D, B, G we get angle(D, B, G) == coangle(D, B, G) + orientation(D, B, G) mod 360
By orientations_are_cyclic on C, F, B we get orientation(C, F, B) == orientation(F, B, C) mod 360, orientation(B, C, F) == orientation(C, F, B) mod 360
By orientations_are_cyclic on C, D, G we get orientation(C, D, G) == orientation(D, G, C) mod 360, orientation(C, D, G) == orientation(G, C, D) mod 360
By triangle_halfangle_sum on G, H, E we get orientation(G, H, E) == halfangle(G, H, E) + halfangle(H, E, G) + halfangle(E, G, H) mod 360
By divide_by_2_two_angles on F, C, D, B, A, G we get coangle(B, A, G) == coangle(F, C, D) mod 360
By log_of_2_times_distance on G, A, H, E we get log(distance(A, G)) == 0.6931471805599453 + log(distance(E, H))
By concyclic_definition_0 on C, B, E, F we get F in Circle(B, C, E)
By concyclic_definition_0 on D, A, B, E we get E in Circle(A, B, D)
By line_intersection_definition on orthocenter(A, B, C), j, i we get orthocenter(A, B, C) == line_intersection(i, j)
By angles_on_chord on B, F, E, C, Circle(B, C, E) we get coangle(B, C, F) == coangle(B, E, F) mod 360
By angles_on_chord on E, A, B, D, Circle(A, B, D) we get coangle(E, B, A) == coangle(E, D, A) mod 360
By angles_on_chord on B, E, A, D, Circle(A, B, D) we get coangle(B, A, E) == coangle(B, D, E) mod 360
By in_imply_collinear on orthocenter(A, B, C), C, F we get collinear(C, F, orthocenter(A, B, C))
By orientations_are_cyclic on D, A, E we get orientation(A, E, D) == orientation(D, A, E) mod 360, orientation(D, A, E) == orientation(E, D, A) mod 360
By angle_equality_conversions_v0 on J, I, D, G, C, D we get coangle(G, C, D) == coangle(J, I, D) mod 360, orientation(G, C, D) == orientation(J, I, D) mod 360
By coangle_definition_v0 on J, H, E we get angle(J, H, E) == coangle(J, H, E) + orientation(J, H, E) mod 360
By angle_equality_conversions_v0 on C, G, E, J, H, E we get coangle(C, G, E) == coangle(J, H, E) mod 360, orientation(C, G, E) == orientation(J, H, E) mod 360
By same_angle on C, G, F, D we get coangle(F, C, D) == coangle(G, C, D) mod 360
By anti_similar_triangle_basic_properties on G, A, B, F, E, B we get not_collinear(A, B, G), not_collinear(B, E, F), angle(G, A, B) == 0 - angle(F, E, B) mod 360, angle(A, B, G) == 0 - angle(E, B, F) mod 360, angle(B, G, A) == 0 - angle(B, F, E) mod 360, log(distance(A, G)) + log(distance(B, E)) == log(distance(E, F)) + log(distance(A, B)), log(distance(A, B)) + log(distance(B, F)) == log(distance(B, E)) + log(distance(B, G)), log(distance(B, F)) + log(distance(A, G)) == log(distance(B, G)) + log(distance(E, F))
By angle_equality_conversions_v0_r on E, C, F, E, D, A we get angle(E, C, F) == angle(E, D, A) mod 360
By collinear_definition on G, F, C we get F in Line(C, G), C in Line(F, G), Line(C, G) == Line(F, G), 0 == 2 * angle(F, G, C) mod 360
By sas_similarity on G, B, F, H, E, K we get similar_triangles(B, F, G, E, K, H)
By divide_by_2_two_angles on B, D, E, K, H, E we get coangle(B, D, E) == coangle(K, H, E) mod 360
By same_angle_converse on H, K, J, E we get collinear(H, J, K)
