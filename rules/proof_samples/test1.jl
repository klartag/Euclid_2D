Assumptions:
A, B, C, D, E, F, G, H, I: Point
f, g, h, i, j, k, l: Line
c: Circle
distinct(A, B, C, D, E, F, G, H, I)
distinct(f, g, h, i, j, k, l)
f == Line(A, B)
g == Line(B, C)
h == Line(A, C)
i == internal_angle_bisector(B, A, C)
j == internal_angle_bisector(A, B, C)
D == line_intersection(i, j)
E == projection(D, g)
F == projection(D, h)
G == projection(D, f)
c == Circle(E, F, G)
k == internal_angle_bisector(D, E, G)
H in k, c
l == external_angle_bisector(D, G, E)
I == line_intersection(j, l)

Need to prove:
concyclic(D, E, H, I)

Proof:
By line_definition on B, D, j we get j == Line(B, D)
By line_definition on H, E, k we get k == Line(E, H)
By line_definition on G, B, f we get f == Line(B, G)
By line_definition on D, A, i we get i == Line(A, D)
By line_definition on C, F, h we get h == Line(C, F)
By line_definition on I, D, j we get j == Line(D, I)
By line_definition on D, G, perpendicular_line(D, f) we get Line(D, G) == perpendicular_line(D, f)
By line_definition on B, I, j we get j == Line(B, I)
By line_definition on E, C, g we get g == Line(C, E)
By line_definition on E, D, perpendicular_line(D, g) we get Line(D, E) == perpendicular_line(D, g)
By line_definition on A, G, f we get f == Line(A, G)
By line_definition on B, E, g we get g == Line(B, E)
By line_definition on D, F, perpendicular_line(D, h) we get Line(D, F) == perpendicular_line(D, h)
By line_definition on G, I, l we get l == Line(G, I)
By line_definition on A, F, h we get h == Line(A, F)
By circle_definition on E, G, H, c we get c == Circle(E, G, H)
By line_unique_intersection_v1 on g, h, C, A we get A not in g
By line_unique_intersection_v1 on j, f, B, G we get G not in j
By line_unique_intersection_v1 on j, g, B, C we get C not in j
By line_unique_intersection_v1 on j, f, B, A we get A not in j
By line_unique_intersection_v1 on j, g, B, E we get E not in j
By line_unique_intersection_v1 on g, j, B, I we get I not in g
By angles_on_chord on F, E, H, G, c we get coangle(F, G, E) == coangle(F, H, E) mod 360
By angles_on_chord on F, G, E, H, c we get coangle(F, E, G) == coangle(F, H, G) mod 360
By angles_on_chord on E, G, H, F, c we get coangle(E, F, G) == coangle(E, H, G) mod 360
By angles_on_chord on G, E, F, H, c we get coangle(G, F, E) == coangle(G, H, E) mod 360
By angles_on_chord on F, H, G, E, c we get coangle(F, E, H) == coangle(F, G, H) mod 360
By in_imply_collinear on E, C, B we get collinear(B, C, E)
By in_imply_collinear on D, I, B we get collinear(B, D, I)
By not_in_line_equivalent_to_not_collinear_v0 on A, C, B we get not_collinear(A, B, C), exists(Line(B, C))
By not_in_line_equivalent_to_not_collinear_v0 on I, B, C we get not_collinear(B, C, I), exists(Line(B, C))
By not_in_line_equivalent_to_not_collinear_v0 on C, B, D we get not_collinear(B, C, D), exists(Line(B, D))
By not_in_line_equivalent_to_not_collinear_v0 on G, B, D we get not_collinear(B, D, G), exists(Line(B, D))
By not_in_line_equivalent_to_not_collinear_v0 on A, B, I we get not_collinear(A, B, I), exists(Line(B, I))
By not_in_line_equivalent_to_not_collinear_v0_r on G, E, H we get G not in Line(E, H)
By not_in_line_equivalent_to_not_collinear_v0 on E, D, I we get not_collinear(D, E, I), exists(Line(D, I))
By perpendicular_direction_conditions_v0_r on B, A, G, D we get 180 == 2 * direction(B, A) - 2 * direction(G, D) mod 360
By perpendicular_direction_conditions_v0_r on A, F, F, D we get 180 == 2 * direction(A, F) - 2 * direction(F, D) mod 360
By perpendicular_direction_conditions_v0_r on B, E, D, E we get 180 == 2 * direction(B, E) - 2 * direction(D, E) mod 360
By perpendicular_direction_conditions_v0_r on B, C, D, E we get 180 == 2 * direction(B, C) - 2 * direction(D, E) mod 360
By perpendicular_angle_conditions_v0 on A, G, D we get 0 == coangle(A, G, D) mod 360
By perpendicular_angle_conditions_v0 on C, E, D we get 0 == coangle(C, E, D) mod 360
By perpendicular_angle_conditions_v0 on A, F, D we get 0 == coangle(A, F, D) mod 360
By perpendicular_angle_conditions_v0 on B, G, D we get 0 == coangle(B, G, D) mod 360
By perpendicular_angle_conditions_v0 on D, G, B we get 0 == coangle(D, G, B) mod 360
By perpendicular_angle_conditions_v0 on C, F, D we get 0 == coangle(C, F, D) mod 360
By perpendicular_angle_conditions_v0 on D, E, B we get 0 == coangle(D, E, B) mod 360
By perpendicular_angle_conditions_v0 on B, E, D we get 0 == coangle(B, E, D) mod 360
By coangle_definition_v1 on F, H, G we get angle(F, H, G) == coangle(F, H, G) + orientation(F, H, G) mod 360
By coangle_definition_v1 on F, G, E we get angle(F, G, E) == coangle(F, G, E) + orientation(F, G, E) mod 360
By coangle_definition_v1 on F, H, E we get angle(F, H, E) == coangle(F, H, E) + orientation(F, H, E) mod 360
By coangle_definition_v1 on F, G, H we get angle(F, G, H) == coangle(F, G, H) + orientation(F, G, H) mod 360
By coangle_definition_v1 on E, H, G we get angle(E, H, G) == coangle(E, H, G) + orientation(E, H, G) mod 360
By coangle_definition_v1 on F, E, H we get angle(F, E, H) == coangle(F, E, H) + orientation(F, E, H) mod 360
By coangle_definition_v1 on F, E, G we get angle(F, E, G) == coangle(F, E, G) + orientation(F, E, G) mod 360
By coangle_definition_v1 on E, F, G we get angle(E, F, G) == coangle(E, F, G) + orientation(E, F, G) mod 360
By coangle_definition_v1 on G, F, E we get angle(G, F, E) == coangle(G, F, E) + orientation(G, F, E) mod 360
By internal_angle_bisector_definition_v0 on B, D, C, A we get angle(B, A, D) == angle(D, A, C) mod 360
By internal_angle_bisector_definition_v0 on C, D, A, B we get angle(C, B, D) == angle(D, B, A) mod 360
By internal_angle_bisector_definition_v0 on C, I, A, B we get angle(C, B, I) == angle(I, B, A) mod 360
By internal_angle_bisector_definition_v0 on G, H, D, E we get angle(G, E, H) == angle(H, E, D) mod 360
By concyclic_sufficient_conditions on D, E, B, G we get concyclic(B, D, E, G)
By concyclic_sufficient_conditions on A, G, D, F we get concyclic(A, D, F, G)
By concyclic_sufficient_conditions on C, E, D, F we get concyclic(C, D, E, F)
By reverse_direction on G, E we get 180 == direction(G, E) - direction(E, G) mod 360
By reverse_direction on B, E we get 180 == direction(B, E) - direction(E, B) mod 360
By reverse_direction on B, A we get 180 == direction(B, A) - direction(A, B) mod 360
By coangle_definition_v1 on D, G, B we get angle(D, G, B) == coangle(D, G, B) + orientation(D, G, B) mod 360
By reverse_direction on G, F we get 180 == direction(G, F) - direction(F, G) mod 360
By reverse_direction on E, D we get 180 == direction(E, D) - direction(D, E) mod 360
By reverse_orientation on G, F, E we get orientation(G, F, E) == 0 - orientation(E, F, G) mod 360
By reverse_direction on B, C we get 180 == direction(B, C) - direction(C, B) mod 360
By reverse_direction on G, B we get 180 == direction(G, B) - direction(B, G) mod 360
By reverse_direction on G, D we get 180 == direction(G, D) - direction(D, G) mod 360
By coangle_definition_v1 on D, E, B we get angle(D, E, B) == coangle(D, E, B) + orientation(D, E, B) mod 360
By reverse_direction on A, C we get 180 == direction(A, C) - direction(C, A) mod 360
By line_inequality on Line(G, H), k, G we get k != Line(G, H)
By same_angle on B, D, I, G we get coangle(D, B, G) == coangle(I, B, G) mod 360
By same_angle on B, I, D, A we get coangle(D, B, A) == coangle(I, B, A) mod 360
By same_angle on D, B, I, G we get coangle(B, D, G) == coangle(I, D, G) mod 360
By same_angle on D, I, B, E we get coangle(B, D, E) == coangle(I, D, E) mod 360
By coangle_definition_v0 on C, B, I we get angle(C, B, I) == coangle(C, B, I) + orientation(C, B, I) mod 360
By coangle_definition_v0 on I, B, C we get angle(I, B, C) == coangle(I, B, C) + orientation(I, B, C) mod 360
By angle_equality_conversions_v0 on D, B, A, C, B, D we get coangle(C, B, D) == coangle(D, B, A) mod 360, orientation(C, B, D) == orientation(D, B, A) mod 360
By angle_equality_conversions_v0 on A, B, I, I, B, C we get coangle(A, B, I) == coangle(I, B, C) mod 360, orientation(A, B, I) == orientation(I, B, C) mod 360
By divide_by_2_two_angles on I, B, A, C, B, I we get coangle(C, B, I) == coangle(I, B, A) mod 360
By incenter_concurrency on C, A, B we get incenter(A, B, C) in internal_angle_bisector(B, A, C), incenter(A, B, C) in internal_angle_bisector(A, B, C), incenter(A, B, C) in internal_angle_bisector(A, C, B)
By line_definition on C, D, internal_angle_bisector(A, C, B) we get Line(C, D) == internal_angle_bisector(A, C, B)
By line_intersection_definition on H, k, Line(G, H) we get H == line_intersection(k, Line(G, H))
By divide_by_2_two_angles on A, B, I, D, B, E we get coangle(A, B, I) == coangle(D, B, E) mod 360
By divide_by_2_two_angles on C, B, D, I, B, G we get coangle(C, B, D) == coangle(I, B, G) mod 360
By reverse_orientation on I, B, C we get orientation(I, B, C) == 0 - orientation(C, B, I) mod 360
By coangle_definition_v1 on B, D, E we get angle(B, D, E) == coangle(B, D, E) + orientation(B, D, E) mod 360
By orientations_are_cyclic on D, E, B we get orientation(D, E, B) == orientation(E, B, D) mod 360, orientation(B, D, E) == orientation(D, E, B) mod 360
By coangle_definition_v1 on B, D, G we get angle(B, D, G) == coangle(B, D, G) + orientation(B, D, G) mod 360
By orientations_are_cyclic on D, G, B we get orientation(D, G, B) == orientation(G, B, D) mod 360, orientation(B, D, G) == orientation(D, G, B) mod 360
By coangle_definition_v0 on E, F, D we get angle(E, F, D) == coangle(E, F, D) + orientation(E, F, D) mod 360
By concyclic_definition_0 on A, D, F, G we get G in Circle(A, D, F)
By concyclic_definition_0 on G, E, D, B we get B in Circle(D, E, G)
By concyclic_definition_0 on C, E, D, F we get F in Circle(C, D, E)
By coangle_definition_v0 on D, A, F we get angle(D, A, F) == coangle(D, A, F) + orientation(D, A, F) mod 360
By coangle_definition_v0 on D, G, F we get angle(D, G, F) == coangle(D, G, F) + orientation(D, G, F) mod 360
By angles_on_chord on D, F, G, A, Circle(A, D, F) we get coangle(D, A, F) == coangle(D, G, F) mod 360
By angles_on_chord on E, D, F, C, Circle(C, D, E) we get coangle(E, C, D) == coangle(E, F, D) mod 360
By aa_anti_similarity on D, B, G, D, B, E we get anti_similar_triangles(B, D, E, B, D, G)
By same_angle on C, B, E, D we get coangle(B, C, D) == coangle(E, C, D) mod 360
By internal_angle_bisector_definition_v1 on B, D, A, C we get coangle(B, C, D) == halfangle(B, C, A) - orientation(B, C, A) mod 360
By divide_by_2_two_angles on E, F, G, B, D, G we get coangle(B, D, G) == coangle(E, F, G) mod 360
By in_imply_collinear on excenter(E, D, G), G, I we get collinear(G, I, excenter(E, D, G))
By external_angle_bisector_definition_v0_r on D, H, E, G we get Line(G, H) == external_angle_bisector(D, G, E)
By same_angle on H, G, I, E we get coangle(G, H, E) == coangle(I, H, E) mod 360
By concyclic_sufficient_conditions on I, H, E, D we get concyclic(D, E, H, I)
