Assumptions:
A, B, C, D, E: Point
distinct(A, B, C, D, E)
not_collinear(A, B, C)
tangent(Line(A, E), Circle(A, B, C))
Line(A, D) == internal_angle_bisector(B, A, C)
D, E in Line(B, C)

Need to prove:
distance(A, E) == distance(D, E)

Proof:
By line_definition on D, B, Line(B,C) we get Line(B,C) == Line(B,D)
By line_definition on E, D, Line(B,C) we get Line(B,C) == Line(D,E)
By in_imply_collinear on D, B, C we get collinear(B, C, D)
By not_in_line_equivalent_to_not_collinear_v0_r on A, C, B we get A not in Line(B,C)
By tangent_chord_angle_v0 on A, B, C, E we get coangle(B,A,E) == coangle(B,C,A) mod 360
By in_imply_collinear on E, B, D we get collinear(B, D, E)
By not_in_line_equivalent_to_not_collinear_v0 on A, E, D we get not_collinear(A, D, E), exists(Line(B,C))
By collinear_definition on C, D, B we get D in Line(B,C), B in Line(C,D), Line(B,C) == Line(C,D), 0 == 2 * angle(D,C,B) mod 360
By coangle_definition_v1 on B, A, E we get angle(B,A,E) == coangle(B,A,E) + orientation(B,A,E) mod 360
By collinear_definition on D, C, B we get C in Line(B,D), B in Line(C,D), Line(B,D) == Line(C,D), 0 == 2 * angle(C,D,B) mod 360
By coangle_definition_v1 on B, C, A we get angle(B,C,A) == coangle(B,C,A) + orientation(B,C,A) mod 360
By internal_angle_bisector_definition_v0 on B, D, C, A we get angle(B,A,D) == angle(D,A,C) mod 360
By triangle_halfangle_sum on A, D, E we get orientation(A,D,E) == halfangle(A,D,E) + halfangle(D,E,A) + halfangle(E,A,D) mod 360
By triangle_halfangle_sum on E, D, A we get orientation(E,D,A) == halfangle(E,D,A) + halfangle(D,A,E) + halfangle(A,E,D) mod 360
By triangle_halfangle_sum on E, A, D we get orientation(E,A,D) == halfangle(E,A,D) + halfangle(A,D,E) + halfangle(D,E,A) mod 360
By triangle_halfangle_sum on D, A, E we get orientation(D,A,E) == halfangle(D,A,E) + halfangle(A,E,D) + halfangle(E,D,A) mod 360
By reverse_direction on A, D we get 180 == direction(A,D) - direction(D,A) mod 360
By reverse_direction on A, C we get 180 == direction(A,C) - direction(C,A) mod 360
By reverse_direction on D, C we get 180 == direction(D,C) - direction(C,D) mod 360
By collinear_definition on D, E, B we get E in Line(B,D), B in Line(D,E), Line(B,D) == Line(D,E), 0 == 2 * angle(E,D,B) mod 360
By coangle_definition_v0 on D, A, E we get angle(D,A,E) == coangle(D,A,E) + orientation(D,A,E) mod 360
By coangle_definition_v0 on E, A, D we get angle(E,A,D) == coangle(E,A,D) + orientation(E,A,D) mod 360
By coangle_definition_v0 on A, D, E we get angle(A,D,E) == coangle(A,D,E) + orientation(A,D,E) mod 360
By coangle_definition_v0 on E, D, A we get angle(E,D,A) == coangle(E,D,A) + orientation(E,D,A) mod 360
By divide_by_2_two_angles on D, A, E, E, D, A we get coangle(D,A,E) == coangle(E,D,A) mod 360
By isosceles_triangle_from_angles on E, A, D we get isosceles_triangle(E, A, D)
