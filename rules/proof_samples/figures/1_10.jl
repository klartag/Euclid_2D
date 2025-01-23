Assumptions:
A, B, C, D, E, O, M: Point
distinct(A, B, C, D, E, O, M)
not_collinear(A, B, C)
collinear(A, D, B)
collinear(A, E, C)
concyclic(B, C, E, D)
O == center(Circle(A, D, E))

Need to prove:
perpendicular(Line(A, O), Line(B, C))

Proof:
By circle_radius_v0_r on A, Circle(A,D,E) we get distance(A,O) == radius(Circle(A,D,E))
By circle_radius_v0_r on D, Circle(A,D,E) we get distance(D,O) == radius(Circle(A,D,E))
By concyclic_definition_0 on B, C, D, E we get E in Circle(B,C,D)
By angle_to_center on A, E, D, Circle(A,D,E) we get coangle(A,E,D) == halfangle(A,O,D) - orientation(A,O,D) mod 360
By collinear_definition on A, B, D we get B in Line(A,D), D in Line(A,B), Line(A,B) == Line(A,D), 0 == 2 * angle(B,A,D) mod 360
By collinear_definition on C, A, E we get A in Line(C,E), E in Line(A,C), Line(A,C) == Line(C,E), 0 == 2 * angle(A,C,E) mod 360
By collinear_definition on B, D, A we get D in Line(A,B), A in Line(B,D), Line(A,B) == Line(B,D), 0 == 2 * angle(D,B,A) mod 360
By angles_on_chord on C, D, E, B, Circle(B,C,D) we get coangle(C,B,D) == coangle(C,E,D) mod 360
By reverse_direction on C, A we get 180 == direction(C,A) - direction(A,C) mod 360
By isosceles_triangle_properties on O, A, D we get distance(A,O) == distance(D,O), angle(A,D,O) == angle(O,A,D) mod 360, orientation(O,A,D) == angle(O,A,D) + halfangle(D,O,A) mod 360
By triangle_halfangle_sum on B, C, A we get orientation(B,C,A) == halfangle(B,C,A) + halfangle(C,A,B) + halfangle(A,B,C) mod 360
By same_angle on E, A, C, D we get coangle(A,E,D) == coangle(C,E,D) mod 360
By coangle_definition_v0 on C, B, D we get angle(C,B,D) == coangle(C,B,D) + orientation(C,B,D) mod 360
By perpendicular_direction_conditions_v0 on C, B, A, O we get perpendicular(Line(A,O), Line(B,C))