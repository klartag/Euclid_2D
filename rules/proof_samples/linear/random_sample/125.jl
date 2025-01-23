Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i)
distinct(c, d)
f == Line(B, C)
g == Line(C, A)
D == projection(A, f)
E == projection(B, g)
h == Line(D, A)
i == Line(E, B)
F == line_intersection(h, i)
c == Circle(B, C, E)
G == midpoint(F, A)
d == Circle(B, E, D)
H == center(c)
I == center(d)

Need to prove:
concyclic(D, G, H, I)

Proof:
By line_definition on E, B, perpendicular_line(B, g) we get Line(B, E) == perpendicular_line(B, g)
By line_definition on D, A, perpendicular_line(A, f) we get Line(A, D) == perpendicular_line(A, f)
By line_definition on A, F, h we get h == Line(A, F)
By line_definition on E, F, i we get i == Line(E, F)
By line_definition on A, E, g we get g == Line(A, E)
By line_definition on B, D, f we get f == Line(B, D)
By line_definition on E, C, g we get g == Line(C, E)
By line_unique_intersection_v1 on h, g, A, E we get E not in h
By line_unique_intersection_v1 on f, i, B, E we get E not in f
By between_implies_orientation on E, A, G, F we get orientation(E, A, G) == orientation(E, G, F) mod 360, orientation(E, A, F) == orientation(E, A, G) mod 360
By circle_radius_v0_r on E, d we get radius(d) == distance(E, center(d))
By circle_radius_v0_r on B, c we get radius(c) == distance(B, center(c))
By circle_radius_v0_r on D, d we get radius(d) == distance(D, center(d))
By circle_radius_v0_r on E, c we get radius(c) == distance(E, center(c))
By circle_radius_v0_r on C, c we get radius(c) == distance(C, center(c))
By in_imply_collinear on E, C, A we get collinear(A, C, E)
By in_imply_collinear on D, C, B we get collinear(B, C, D)
By angle_to_center on E, C, B, c we get coangle(E, C, B) == halfangle(E, center(c), B) - orientation(E, center(c), B) mod 360
By angle_to_center on C, B, E, c we get coangle(C, B, E) == halfangle(C, center(c), E) - orientation(C, center(c), E) mod 360
By angle_to_center on E, B, D, d we get coangle(E, B, D) == halfangle(E, center(d), D) - orientation(E, center(d), D) mod 360
By angle_to_center on D, B, E, d we get coangle(D, B, E) == halfangle(D, center(d), E) - orientation(D, center(d), E) mod 360
By angle_to_center on B, E, C, c we get coangle(B, E, C) == halfangle(B, center(c), C) - orientation(B, center(c), C) mod 360
By angle_to_center on E, B, C, c we get coangle(E, B, C) == halfangle(E, center(c), C) - orientation(E, center(c), C) mod 360
By collinear_definition on A, G, F we get G in Line(A, F), F in Line(A, G), Line(A, F) == Line(A, G), 0 == 2 * angle(G, A, F) mod 360
By same_angle on B, C, D, E we get coangle(C, B, E) == coangle(D, B, E) mod 360
By perpendicular_direction_conditions_v0_r on A, G, C, B we get 180 == 2 * direction(A, G) - 2 * direction(C, B) mod 360
By perpendicular_direction_conditions_v0_r on F, A, B, C we get 180 == 2 * direction(F, A) - 2 * direction(B, C) mod 360
By perpendicular_direction_conditions_v0_r on B, D, A, F we get 180 == 2 * direction(B, D) - 2 * direction(A, F) mod 360
By in_imply_collinear on G, D, A we get collinear(A, D, G)
By reverse_direction on A, F we get 180 == direction(A, F) - direction(F, A) mod 360
By orientations_are_cyclic on E, F, A we get orientation(E, F, A) == orientation(F, A, E) mod 360, orientation(A, E, F) == orientation(E, F, A) mod 360
By orientations_are_cyclic on B, H, E we get orientation(B, H, E) == orientation(H, E, B) mod 360, orientation(B, H, E) == orientation(E, B, H) mod 360
By orientations_are_cyclic on E, A, G we get orientation(A, G, E) == orientation(E, A, G) mod 360, orientation(E, A, G) == orientation(G, E, A) mod 360
By perpendicular_angle_conditions_v0 on B, E, C we get 0 == coangle(B, E, C) mod 360
By orientations_are_cyclic on C, H, E we get orientation(C, H, E) == orientation(H, E, C) mod 360, orientation(C, H, E) == orientation(E, C, H) mod 360
By orientations_are_cyclic on D, I, E we get orientation(D, I, E) == orientation(I, E, D) mod 360, orientation(D, I, E) == orientation(E, D, I) mod 360
By orientations_are_cyclic on B, H, C we get orientation(B, H, C) == orientation(H, C, B) mod 360, orientation(B, H, C) == orientation(C, B, H) mod 360
By orientations_are_cyclic on E, H, C we get orientation(E, H, C) == orientation(H, C, E) mod 360, orientation(C, E, H) == orientation(E, H, C) mod 360
By orientations_are_cyclic on E, H, B we get orientation(E, H, B) == orientation(H, B, E) mod 360, orientation(B, E, H) == orientation(E, H, B) mod 360
By orientations_are_cyclic on E, I, D we get orientation(E, I, D) == orientation(I, D, E) mod 360, orientation(D, E, I) == orientation(E, I, D) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on E, G, A we get not_collinear(A, E, G), exists(Line(A, G))
By perpendicular_direction_conditions_v0_r on E, B, C, E we get 180 == 2 * direction(E, B) - 2 * direction(C, E) mod 360
By perpendicular_direction_conditions_v0_r on C, E, E, F we get 180 == 2 * direction(C, E) - 2 * direction(E, F) mod 360
By perpendicular_direction_conditions_v0_r on A, E, E, F we get 180 == 2 * direction(A, E) - 2 * direction(E, F) mod 360
By perpendicular_direction_conditions_v0_r on A, C, E, B we get 180 == 2 * direction(A, C) - 2 * direction(E, B) mod 360
By perpendicular_angle_conditions_v0 on A, E, F we get 0 == coangle(A, E, F) mod 360
By coangle_definition_v0 on B, H, E we get angle(B, H, E) == coangle(B, H, E) + orientation(B, H, E) mod 360
By coangle_definition_v0 on D, I, E we get angle(D, I, E) == coangle(D, I, E) + orientation(D, I, E) mod 360
By coangle_definition_v1 on E, C, B we get angle(E, C, B) == coangle(E, C, B) + orientation(E, C, B) mod 360
By right_triangle_circumcenter_v1 on A, E, F we get midpoint(A, F) == circumcenter(A, E, F)
By isosceles_triangle_properties on H, B, E we get distance(B, H) == distance(E, H), angle(B, E, H) == angle(H, B, E) mod 360, orientation(H, B, E) == angle(H, B, E) + halfangle(E, H, B) mod 360
By isosceles_triangle_properties on H, C, B we get distance(B, H) == distance(C, H), angle(C, B, H) == angle(H, C, B) mod 360, orientation(H, C, B) == angle(H, C, B) + halfangle(B, H, C) mod 360
By isosceles_triangle_properties on H, E, C we get distance(C, H) == distance(E, H), angle(E, C, H) == angle(H, E, C) mod 360, orientation(H, E, C) == angle(H, E, C) + halfangle(C, H, E) mod 360
By isosceles_triangle_properties on I, E, D we get distance(D, I) == distance(E, I), angle(E, D, I) == angle(I, E, D) mod 360, orientation(I, E, D) == angle(I, E, D) + halfangle(D, I, E) mod 360
By isosceles_triangle_properties on H, C, E we get distance(C, H) == distance(E, H), angle(C, E, H) == angle(H, C, E) mod 360, orientation(H, C, E) == angle(H, C, E) + halfangle(E, H, C) mod 360
By isosceles_triangle_properties on I, D, E we get distance(D, I) == distance(E, I), angle(D, E, I) == angle(I, D, E) mod 360, orientation(I, D, E) == angle(I, D, E) + halfangle(E, I, D) mod 360
By reverse_direction on A, E we get 180 == direction(A, E) - direction(E, A) mod 360
By coangle_definition_v1 on A, E, F we get angle(A, E, F) == coangle(A, E, F) + orientation(A, E, F) mod 360
By reverse_direction on E, F we get 180 == direction(E, F) - direction(F, E) mod 360
By same_angle on A, E, C, G we get coangle(C, A, G) == coangle(E, A, G) mod 360
By divide_by_2_two_angles on E, B, C, H, E, B we get coangle(E, B, C) == coangle(H, E, B) mod 360
By coangle_definition_v0 on H, E, B we get angle(H, E, B) == coangle(H, E, B) + orientation(H, E, B) mod 360
By angle_equality_conversions_v0 on I, E, D, E, C, B we get coangle(E, C, B) == coangle(I, E, D) mod 360, orientation(E, C, B) == orientation(I, E, D) mod 360
By angle_equality_conversions_v0 on C, B, E, H, B, E we get coangle(C, B, E) == coangle(H, B, E) mod 360, orientation(C, B, E) == orientation(H, B, E) mod 360
By internal_angle_bisector_definition_v0_r on C, D, C, B we get Line(B, D) == internal_angle_bisector(C, B, C)
By internal_angle_bisector_definition_v0_r on C, H, C, B we get Line(B, H) == internal_angle_bisector(C, B, C)
By angle_to_center on E, F, A, Circle(A, E, F) we get coangle(E, F, A) == halfangle(E, center(Circle(A, E, F)), A) - orientation(E, center(Circle(A, E, F)), A) mod 360
By same_angle_converse on B, D, H, E we get collinear(B, D, H)
By divide_by_2_two_angles on E, A, G, E, B, D we get coangle(E, A, G) == coangle(E, B, D) mod 360
By divide_by_2_two_angles on E, A, F, C, A, G we get coangle(C, A, G) == coangle(E, A, F) mod 360
By divide_by_2_two_angles on E, F, A, I, E, D we get coangle(E, F, A) == coangle(I, E, D) mod 360
By coangle_definition_v0 on E, A, F we get angle(E, A, F) == coangle(E, A, F) + orientation(E, A, F) mod 360
By coangle_definition_v1 on E, F, A we get angle(E, F, A) == coangle(E, F, A) + orientation(E, F, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on E, B, H we get not_collinear(B, E, H), exists(Line(B, H))
By same_angle on G, A, D, E we get coangle(A, G, E) == coangle(D, G, E) mod 360
By coangle_definition_v0 on A, G, E we get angle(A, G, E) == coangle(A, G, E) + orientation(A, G, E) mod 360
By concyclic_sufficient_conditions on D, G, E, I we get concyclic(D, E, G, I)
By same_angle on H, B, D, E we get coangle(B, H, E) == coangle(D, H, E) mod 360
By concyclic_sufficient_conditions on D, G, E, H we get concyclic(D, E, G, H)
By concyclic_definition_1 on E, D, G, I we get Circle(D, E, G) == Circle(D, G, I)
By concyclic_definition_0 on E, D, G, H we get H in Circle(D, E, G)
By in_imply_concyclic on I, D, G, H we get concyclic(D, G, H, I)
