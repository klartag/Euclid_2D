Assumptions:
A, B, C, D, X, Y, Z, W: Point
distinct(A, B, C, D, W, X, Y, Z)
distinct(Line(A, B), Line(A, D), Line(B, C), Line(C, D), Line(W, X), Line(W, Z), Line(X, Y), Line(Y, Z))
collinear(A, X, Y)
collinear(B, Y, Z)
collinear(C, W, Z)
collinear(D, W, X)
Line(X, Y) == external_angle_bisector(B, A, D)
Line(Y, Z) == external_angle_bisector(A, B, C)
Line(W, Z) == external_angle_bisector(B, C, D)
Line(W, X) == external_angle_bisector(A, D, C)

Need to prove:
concyclic(W, X, Y, Z)

Proof:
By line_unique_intersection_v1 on Line(W, Z), Line(B, C), C, B we get B not in Line(W, Z)
By line_unique_intersection_v1 on Line(W, X), Line(X, Y), X, A we get A not in Line(W, X)
By line_unique_intersection_v1 on Line(W, Z), Line(Y, Z), Z, Y we get Y not in Line(W, Z)
By line_unique_intersection_v1 on Line(X, Y), Line(W, X), X, W we get W not in Line(X, Y)
By collinear_definition on X, Y, A we get Y in Line(A, X), A in Line(X, Y), Line(A, X) == Line(X, Y), 0 == 2 * angle(Y, X, A) mod 360
By collinear_definition on Z, Y, B we get Y in Line(B, Z), B in Line(Y, Z), Line(B, Z) == Line(Y, Z), 0 == 2 * angle(Y, Z, B) mod 360
By collinear_definition on C, W, Z we get W in Line(C, Z), Z in Line(C, W), Line(C, W) == Line(C, Z), 0 == 2 * angle(W, C, Z) mod 360
By collinear_definition on Z, C, W we get C in Line(W, Z), W in Line(C, Z), Line(C, Z) == Line(W, Z), 0 == 2 * angle(C, Z, W) mod 360
By collinear_definition on D, W, X we get W in Line(D, X), X in Line(D, W), Line(D, W) == Line(D, X), 0 == 2 * angle(W, D, X) mod 360
By collinear_definition on X, W, D we get W in Line(D, X), D in Line(W, X), Line(D, X) == Line(W, X), 0 == 2 * angle(W, X, D) mod 360
By reverse_direction on Z, C we get 180 == direction(Z, C) - direction(C, Z) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on Y, W, Z we get not_collinear(W, Y, Z), exists(Line(W, Z))
By reverse_direction on X, A we get 180 == direction(X, A) - direction(A, X) mod 360
By reverse_direction on X, D we get 180 == direction(X, D) - direction(D, X) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on W, X, Y we get not_collinear(W, X, Y), exists(Line(X, Y))
By reverse_direction on Z, B we get 180 == direction(Z, B) - direction(B, Z) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on B, C, Z we get not_collinear(B, C, Z), exists(Line(C, Z))
By not_in_line_equivalent_to_not_collinear_v0 on A, W, X we get not_collinear(A, W, X), exists(Line(W, X))
By external_angle_bisector_definition_v0 on D, X, B, A we get 180 == angle(D, A, X) + angle(B, A, X) mod 360
By external_angle_bisector_definition_v0 on C, W, A, D we get 180 == angle(C, D, W) + angle(A, D, W) mod 360
By external_angle_bisector_definition_v0 on D, W, B, C we get 180 == angle(D, C, W) + angle(B, C, W) mod 360
By external_angle_bisector_definition_v0 on A, Z, C, B we get 180 == angle(A, B, Z) + angle(C, B, Z) mod 360
By reverse_direction on C, B we get 180 == direction(C, B) - direction(B, C) mod 360
By reverse_direction on C, D we get 180 == direction(C, D) - direction(D, C) mod 360
By reverse_direction on B, A we get 180 == direction(B, A) - direction(A, B) mod 360
By reverse_direction on D, A we get 180 == direction(D, A) - direction(A, D) mod 360
By same_angle on Z, C, W, B we get coangle(C, Z, B) == coangle(W, Z, B) mod 360
By same_angle on X, W, D, A we get coangle(D, X, A) == coangle(W, X, A) mod 360
By divide_by_2_two_angles on W, Z, Y, W, Z, B we get coangle(W, Z, B) == coangle(W, Z, Y) mod 360
By divide_by_2_two_angles on W, X, Y, D, X, A we get coangle(D, X, A) == coangle(W, X, Y) mod 360
By divide_by_2_two_angles on W, X, A, C, Z, B we get coangle(C, Z, B) == coangle(W, X, A) mod 360
By concyclic_sufficient_conditions on W, Z, Y, X we get concyclic(W, X, Y, Z)
