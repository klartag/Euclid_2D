Assumptions:
A, B, C, D, X, Y, Z, W: Point
distinct(A, B, C, D, W, X, Y, Z)
distinct(Line(A, B), Line(A, D), Line(B, C), Line(C, D), Line(W, X), Line(W, Z), Line(X, Y), Line(Y, Z))
collinear(A, X, Y)
collinear(B, Y, Z)
collinear(C, W, Z)
collinear(D, W, X)
Line(X, Y) == internal_angle_bisector(B, A, D)
Line(Y, Z) == internal_angle_bisector(A, B, C)
Line(W, Z) == internal_angle_bisector(B, C, D)
Line(W, X) == internal_angle_bisector(A, D, C)

Need to prove:
concyclic(W, X, Y, Z)

Proof:
By line_unique_intersection_v1 on Line(Y, Z), Line(X, Y), Y, A we get A not in Line(Y, Z)
By line_unique_intersection_v1 on Line(W, X), Line(W, Z), W, Z we get Z not in Line(W, X)
By line_unique_intersection_v1 on Line(X, Y), Line(Y, Z), Y, Z we get Z not in Line(X, Y)
By collinear_definition on C, Z, W we get Z in Line(C, W), W in Line(C, Z), Line(C, W) == Line(C, Z), 0 == 2 * angle(Z, C, W) mod 360
By collinear_definition on A, Y, X we get Y in Line(A, X), X in Line(A, Y), Line(A, X) == Line(A, Y), 0 == 2 * angle(Y, A, X) mod 360
By collinear_definition on B, Z, Y we get Z in Line(B, Y), Y in Line(B, Z), Line(B, Y) == Line(B, Z), 0 == 2 * angle(Z, B, Y) mod 360
By collinear_definition on Y, X, A we get X in Line(A, Y), A in Line(X, Y), Line(A, Y) == Line(X, Y), 0 == 2 * angle(X, Y, A) mod 360
By collinear_definition on Y, Z, B we get Z in Line(B, Y), B in Line(Y, Z), Line(B, Y) == Line(Y, Z), 0 == 2 * angle(Z, Y, B) mod 360
By collinear_definition on W, Z, C we get Z in Line(C, W), C in Line(W, Z), Line(C, W) == Line(W, Z), 0 == 2 * angle(Z, W, C) mod 360
By collinear_definition on D, W, X we get W in Line(D, X), X in Line(D, W), Line(D, W) == Line(D, X), 0 == 2 * angle(W, D, X) mod 360
By collinear_definition on W, D, X we get D in Line(W, X), X in Line(D, W), Line(D, W) == Line(W, X), 0 == 2 * angle(D, W, X) mod 360
By collinear_definition on Z, B, Y we get B in Line(Y, Z), Y in Line(B, Z), Line(B, Z) == Line(Y, Z), 0 == 2 * angle(B, Z, Y) mod 360
By reverse_direction on A, Y we get 180 == direction(A, Y) - direction(Y, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on Z, X, W we get not_collinear(W, X, Z), exists(Line(W, X))
By not_in_line_equivalent_to_not_collinear_v0 on A, B, Y we get not_collinear(A, B, Y), exists(Line(B, Y))
By reverse_direction on Z, Y we get 180 == direction(Z, Y) - direction(Y, Z) mod 360
By reverse_direction on Z, B we get 180 == direction(Z, B) - direction(B, Z) mod 360
By reverse_direction on D, W we get 180 == direction(D, W) - direction(W, D) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on Z, Y, X we get not_collinear(X, Y, Z), exists(Line(X, Y))
By reverse_direction on W, C we get 180 == direction(W, C) - direction(C, W) mod 360
By internal_angle_bisector_definition_v0 on A, Y, C, B we get angle(A, B, Y) == angle(Y, B, C) mod 360
By internal_angle_bisector_definition_v0 on B, Z, D, C we get angle(B, C, Z) == angle(Z, C, D) mod 360
By internal_angle_bisector_definition_v0 on C, W, A, D we get angle(C, D, W) == angle(W, D, A) mod 360
By internal_angle_bisector_definition_v0 on B, X, D, A we get angle(B, A, X) == angle(X, A, D) mod 360
By reverse_direction on A, B we get 180 == direction(A, B) - direction(B, A) mod 360
By reverse_direction on B, C we get 180 == direction(B, C) - direction(C, B) mod 360
By reverse_direction on D, A we get 180 == direction(D, A) - direction(A, D) mod 360
By reverse_direction on C, D we get 180 == direction(C, D) - direction(D, C) mod 360
By same_angle on Y, A, X, B we get coangle(A, Y, B) == coangle(X, Y, B) mod 360
By divide_by_2_two_angles on A, Y, B, X, Y, Z we get coangle(A, Y, B) == coangle(X, Y, Z) mod 360
By divide_by_2_two_angles on X, W, Z, X, Y, B we get coangle(X, W, Z) == coangle(X, Y, B) mod 360
By concyclic_sufficient_conditions on X, Y, Z, W we get concyclic(W, X, Y, Z)
