Assumptions:
A, B, C, D, E: Point
distinct(A, B, C, D, E)
not_collinear(A, B, C)
between(B, D, C)
between(D, C, E)
angle(D, A, B) == angle(C, A, D)

Need to prove: 
2 * angle(A, D, C) == angle(A, B, D) + angle(A, C, E) mod 360

Proof:
By between_implies_orientation on A, C, D, B we get orientation(A,C,D) == orientation(A,D,B) mod 360, orientation(A,C,B) == orientation(A,C,D) mod 360
By between_implies_orientation on A, E, C, D we get orientation(A,C,D) == orientation(A,E,C) mod 360, orientation(A,E,C) == orientation(A,E,D) mod 360
By reverse_direction on C, A we get 180 == direction(C,A) - direction(A,C) mod 360
By reverse_direction on B, A we get 180 == direction(B,A) - direction(A,B) mod 360
By same_angle on B, C, D, A we get coangle(C,B,A) == coangle(D,B,A) mod 360
By same_angle on C, B, D, A we get coangle(B,C,A) == coangle(D,C,A) mod 360
By collinear_definition on B, D, C we get D in Line(B,C), C in Line(B,D), Line(B,C) == Line(B,D), 0 == 2 * angle(D,B,C) mod 360
By coangle_definition_v0 on D, B, A we get angle(D,B,A) == coangle(D,B,A) + orientation(D,B,A) mod 360
By collinear_definition on D, B, C we get B in Line(C,D), C in Line(B,D), Line(B,D) == Line(C,D), 0 == 2 * angle(B,D,C) mod 360
By coangle_definition_v0 on E, C, A we get angle(E,C,A) == coangle(E,C,A) + orientation(E,C,A) mod 360
By collinear_definition on C, E, D we get E in Line(C,D), D in Line(C,E), Line(C,D) == Line(C,E), 0 == 2 * angle(E,C,D) mod 360
By triangle_halfangle_sum on D, B, A we get orientation(D,B,A) == halfangle(D,B,A) + halfangle(B,A,D) + halfangle(A,D,B) mod 360
By triangle_halfangle_sum on A, D, B we get orientation(A,D,B) == halfangle(A,D,B) + halfangle(D,B,A) + halfangle(B,A,D) mod 360
By in_imply_collinear on B, C, E we get collinear(B, C, E)
By reverse_direction on B, C we get 180 == direction(B,C) - direction(C,B) mod 360
By coangle_definition_v1 on B, C, A we get angle(B,C,A) == coangle(B,C,A) + orientation(B,C,A) mod 360
By orientations_are_cyclic on A, E, C we get orientation(A,E,C) == orientation(E,C,A) mod 360, orientation(A,E,C) == orientation(C,A,E) mod 360
By orientations_are_cyclic on A, B, C we get orientation(A,B,C) == orientation(B,C,A) mod 360, orientation(A,B,C) == orientation(C,A,B) mod 360
By reverse_orientation on A, B, C we get orientation(A,B,C) == 0 - orientation(C,B,A) mod 360
By coangle_definition_v1 on C, B, A we get angle(C,B,A) == coangle(C,B,A) + orientation(C,B,A) mod 360
By same_angle on C, B, E, A we get coangle(B,C,A) == coangle(E,C,A) mod 360
