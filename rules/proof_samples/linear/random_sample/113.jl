Assumptions:
A, B, C, D, E, F, G, H: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == parallel_line(C, f)
c == Circle(C, A, B)
D in h, c
i == Line(A, D)
E == line_intersection(g, i)
F == center(c)
d == Circle(E, F, D)
j == Line(C, A)
D in k # (defining k)
G == line_intersection(j, k)
H in k, d

Need to prove:
concyclic(C, F, G, H)

Proof:
By line_definition on C, D, h we get h == Line(C, D)
By line_definition on D, G, k we get k == Line(D, G)
By line_definition on G, C, j we get j == Line(C, G)
By line_unique_intersection_v1 on j, k, G, H we get H not in j
By circle_radius_v0_r on D, c we get radius(c) == distance(D, center(c))
By circle_radius_v0_r on A, c we get radius(c) == distance(A, center(c))
By circle_radius_v0_r on B, c we get radius(c) == distance(B, center(c))
By circle_radius_v0_r on C, c we get radius(c) == distance(C, center(c))
By angles_on_chord on B, C, A, D, c we get coangle(B, A, C) == coangle(B, D, C) mod 360
By angles_on_chord on D, A, B, C, c we get coangle(D, B, A) == coangle(D, C, A) mod 360
By angles_on_chord on D, H, E, F, d we get coangle(D, E, H) == coangle(D, F, H) mod 360
By angles_on_chord on F, H, E, D, d we get coangle(F, D, H) == coangle(F, E, H) mod 360
By angles_on_chord on F, D, E, H, d we get coangle(F, E, D) == coangle(F, H, D) mod 360
By in_imply_collinear on G, C, A we get collinear(A, C, G)
By in_imply_collinear on E, A, D we get collinear(A, D, E)
By in_imply_concyclic on B, C, A, D we get concyclic(A, B, C, D)
By angle_to_center on B, C, D, c we get coangle(B, C, D) == halfangle(B, center(c), D) - orientation(B, center(c), D) mod 360
By angle_to_center on B, D, C, c we get coangle(B, D, C) == halfangle(B, center(c), C) - orientation(B, center(c), C) mod 360
By angle_to_center on D, A, B, c we get coangle(D, A, B) == halfangle(D, center(c), B) - orientation(D, center(c), B) mod 360
By angle_to_center on C, A, D, c we get coangle(C, A, D) == halfangle(C, center(c), D) - orientation(C, center(c), D) mod 360
By angle_to_center on D, C, A, c we get coangle(D, C, A) == halfangle(D, center(c), A) - orientation(D, center(c), A) mod 360
By angles_on_equal_chords on B, A, C, D, B, A, c we get coangle(B, A, C) == coangle(D, B, A) mod 360
By in_imply_collinear on H, G, D we get collinear(D, G, H)
By not_in_line_equivalent_to_not_collinear_v0 on H, G, C we get not_collinear(C, G, H), exists(Line(C, G))
By coangle_definition_v1 on D, F, H we get angle(D, F, H) == coangle(D, F, H) + orientation(D, F, H) mod 360
By coangle_definition_v1 on D, A, B we get angle(D, A, B) == coangle(D, A, B) + orientation(D, A, B) mod 360
By coangle_definition_v1 on C, A, D we get angle(C, A, D) == coangle(C, A, D) + orientation(C, A, D) mod 360
By coangle_definition_v1 on D, E, H we get angle(D, E, H) == coangle(D, E, H) + orientation(D, E, H) mod 360
By collinear_definition on A, D, E we get D in Line(A, E), E in Line(A, D), Line(A, D) == Line(A, E), 0 == 2 * angle(D, A, E) mod 360
By collinear_definition on G, C, A we get C in Line(A, G), A in Line(C, G), Line(A, G) == Line(C, G), 0 == 2 * angle(C, G, A) mod 360
By coangle_definition_v1 on F, H, D we get angle(F, H, D) == coangle(F, H, D) + orientation(F, H, D) mod 360
By collinear_definition on E, A, D we get A in Line(D, E), D in Line(A, E), Line(A, E) == Line(D, E), 0 == 2 * angle(A, E, D) mod 360
By coangle_definition_v1 on F, E, H we get angle(F, E, H) == coangle(F, E, H) + orientation(F, E, H) mod 360
By collinear_definition on A, C, G we get C in Line(A, G), G in Line(A, C), Line(A, C) == Line(A, G), 0 == 2 * angle(C, A, G) mod 360
By coangle_definition_v1 on F, D, H we get angle(F, D, H) == coangle(F, D, H) + orientation(F, D, H) mod 360
By coangle_definition_v1 on B, C, D we get angle(B, C, D) == coangle(B, C, D) + orientation(B, C, D) mod 360
By triangle_halfangle_sum on A, F, D we get orientation(A, F, D) == halfangle(A, F, D) + halfangle(F, D, A) + halfangle(D, A, F) mod 360
By isosceles_triangle_properties on F, B, A we get distance(A, F) == distance(B, F), angle(B, A, F) == angle(F, B, A) mod 360, orientation(F, B, A) == angle(F, B, A) + halfangle(A, F, B) mod 360
By isosceles_trapezoids_are_concyclic_v1 on D, C, B, A we get isosceles_trapezoid(B, A, D, C)
By reverse_direction on H, D we get 180 == direction(H, D) - direction(D, H) mod 360
By reverse_direction on A, E we get 180 == direction(A, E) - direction(E, A) mod 360
By reverse_direction on A, G we get 180 == direction(A, G) - direction(G, A) mod 360
By isosceles_trapezoids_contain_isosceles_triangles on C, D, A, B we get isosceles_triangle(line_intersection(Line(A, D), Line(B, C)), C, D), isosceles_triangle(line_intersection(Line(A, D), Line(B, C)), A, B)
By collinear_definition on H, G, D we get G in Line(D, H), D in Line(G, H), Line(D, H) == Line(G, H), 0 == 2 * angle(G, H, D) mod 360
By reverse_direction on H, G we get 180 == direction(H, G) - direction(G, H) mod 360
By perpendicular_bisector_sufficient_conditions on C, D, F, E we get Line(E, F) == perpendicular_bisector(C, D)
By perpendicular_direction_conditions_v0_r on D, C, E, F we get 180 == 2 * direction(D, C) - 2 * direction(E, F) mod 360
By divide_by_2_two_angles on C, G, H, C, F, H we get coangle(C, F, H) == coangle(C, G, H) mod 360
By concyclic_sufficient_conditions on C, G, H, F we get concyclic(C, F, G, H)
