Assumptions:
A, B, C, D, O: Point
distinct(A, B, C, D, O)
not_collinear(A, O, C)
D == projection(A, Line(B, C))
O == center(Circle(A, B, C))

Need to prove:
angle(D, A, B) == angle(C, A, O) mod 360

Proof:
By line_definition on A, D, perpendicular_line(A,Line(B,C)) we get Line(A,D) == perpendicular_line(A,Line(B,C))
By line_definition on B, D, Line(B,C) we get Line(B,C) == Line(B,D)
By circle_radius_v0_r on C, Circle(A,B,C) we get distance(C,O) == radius(Circle(A,B,C))
By circle_radius_v0_r on A, Circle(A,B,C) we get distance(A,O) == radius(Circle(A,B,C))
By in_imply_collinear on D, C, B we get collinear(B, C, D)
By not_in_line_equivalent_to_not_collinear_v0_r on A, C, B we get A not in Line(B,C)
By reverse_direction on A, D we get 180 == direction(A,D) - direction(D,A) mod 360
By reverse_direction on A, B we get 180 == direction(A,B) - direction(B,A) mod 360
By angle_to_center on C, B, A, Circle(A,B,C) we get coangle(C,B,A) == halfangle(C,O,A) - orientation(C,O,A) mod 360
By perpendicular_direction_conditions_v0_r on D, B, D, A we get 180 == 2 * direction(D,B) - 2 * direction(D,A) mod 360
By same_angle on B, C, D, A we get coangle(C,B,A) == coangle(D,B,A) mod 360
By orientations_are_cyclic on O, A, C we get orientation(A,C,O) == orientation(O,A,C) mod 360, orientation(C,O,A) == orientation(O,A,C) mod 360
By orientations_are_cyclic on B, A, D we get orientation(A,D,B) == orientation(B,A,D) mod 360, orientation(B,A,D) == orientation(D,B,A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on A, B, D we get not_collinear(A, B, D), exists(Line(B,C))
By isosceles_triangle_properties on O, A, C we get distance(A,O) == distance(C,O), angle(A,C,O) == angle(O,A,C) mod 360, orientation(O,A,C) == angle(O,A,C) + halfangle(C,O,A) mod 360
By perpendicular_angle_conditions_v0 on B, D, A we get 0 == coangle(B,D,A) mod 360
By reverse_orientation on A, D, B we get orientation(A,D,B) == 0 - orientation(B,D,A) mod 360
By reverse_direction on D, B we get 180 == direction(D,B) - direction(B,D) mod 360
By coangle_definition_v1 on D, B, A we get angle(D,B,A) == coangle(D,B,A) + orientation(D,B,A) mod 360
By coangle_definition_v1 on B, D, A we get angle(B,D,A) == coangle(B,D,A) + orientation(B,D,A) mod 360
