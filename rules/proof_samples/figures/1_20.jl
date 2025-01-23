Assumptions:
A, B, C, D, X, Y, Z, W, T: Point
distinct(A, B, C, D, X, Y, Z, W, T)
distinct(Line(X, Y), Line(Y, Z), Line(Z, W), Line(W, X))

not_collinear(A, B, C)
not_collinear(A, B, D)
not_collinear(A, C, D)
not_collinear(B, C, D)

X == midpoint(A, B)
Y == midpoint(B, C)
Z == midpoint(C, D)
W == midpoint(D, A)

T == line_intersection(Line(X, Z), Line(Y, W))

Need to prove:
distance(X, T) == distance(Z, T)
distance(Y, T) == distance(W, T)

Proof:
By line_definition on T, X, Line(X,Z) we get Line(T,X) == Line(X,Z)
By line_unique_intersection_v1 on Line(Y,Z), Line(W,Z), Z, W we get W not in Line(Y,Z)
By line_unique_intersection_v1 on Line(X,Y), Line(W,X), X, W we get W not in Line(X,Y)
By line_unique_intersection_v1 on Line(W,X), Line(X,Y), X, Y we get Y not in Line(W,X)
By line_unique_intersection_v1 on Line(W,X), Line(W,Z), W, Z we get Z not in Line(W,X)
By line_unique_intersection_v1 on Line(X,Y), Line(Y,Z), Y, Z we get Z not in Line(X,Y)
By in_imply_collinear on T, W, Y we get collinear(T, W, Y)
By in_imply_collinear on T, Z, X we get collinear(T, X, Z)
By collinear_definition on C, Z, D we get Z in Line(C,D), D in Line(C,Z), Line(C,D) == Line(C,Z), 0 == 2 * angle(Z,C,D) mod 360
By log_of_2_times_distance on B, A, X, B we get log(distance(A,B)) == 0.6931471805599453 + log(distance(B,X))
By collinear_definition on B, Y, C we get Y in Line(B,C), C in Line(B,Y), Line(B,C) == Line(B,Y), 0 == 2 * angle(Y,B,C) mod 360
By log_of_2_times_distance on D, C, C, Z we get log(distance(C,D)) == 0.6931471805599453 + log(distance(C,Z))
By log_of_2_times_distance on B, C, C, Y we get log(distance(B,C)) == 0.6931471805599453 + log(distance(C,Y))
By collinear_definition on D, W, A we get W in Line(A,D), A in Line(D,W), Line(A,D) == Line(D,W), 0 == 2 * angle(W,D,A) mod 360
By collinear_definition on B, A, X we get A in Line(B,X), X in Line(A,B), Line(A,B) == Line(B,X), 0 == 2 * angle(A,B,X) mod 360
By log_of_2_times_distance on A, D, W, D we get log(distance(A,D)) == 0.6931471805599453 + log(distance(D,W))
By log_of_2_times_distance on A, D, W, A we get log(distance(A,D)) == 0.6931471805599453 + log(distance(A,W))
By log_of_2_times_distance on A, B, A, X we get log(distance(A,B)) == 0.6931471805599453 + log(distance(A,X))
By log_of_2_times_distance on B, C, Y, B we get log(distance(B,C)) == 0.6931471805599453 + log(distance(B,Y))
By log_of_2_times_distance on D, C, D, Z we get log(distance(C,D)) == 0.6931471805599453 + log(distance(D,Z))
By triangle_halfangle_sum on Y, Z, X we get orientation(Y,Z,X) == halfangle(Y,Z,X) + halfangle(Z,X,Y) + halfangle(X,Y,Z) mod 360
By triangle_halfangle_sum on Z, X, Y we get orientation(Z,X,Y) == halfangle(Z,X,Y) + halfangle(X,Y,Z) + halfangle(Y,Z,X) mod 360
By triangle_halfangle_sum on X, W, Z we get orientation(X,W,Z) == halfangle(X,W,Z) + halfangle(W,Z,X) + halfangle(Z,X,W) mod 360
By triangle_halfangle_sum on W, Y, X we get orientation(W,Y,X) == halfangle(W,Y,X) + halfangle(Y,X,W) + halfangle(X,W,Y) mod 360
By triangle_halfangle_sum on W, Y, Z we get orientation(W,Y,Z) == halfangle(W,Y,Z) + halfangle(Y,Z,W) + halfangle(Z,W,Y) mod 360
By triangle_halfangle_sum on Z, Y, X we get orientation(Z,Y,X) == halfangle(Z,Y,X) + halfangle(Y,X,Z) + halfangle(X,Z,Y) mod 360
By triangle_halfangle_sum on W, Z, Y we get orientation(W,Z,Y) == halfangle(W,Z,Y) + halfangle(Z,Y,W) + halfangle(Y,W,Z) mod 360
By triangle_halfangle_sum on Z, X, W we get orientation(Z,X,W) == halfangle(Z,X,W) + halfangle(X,W,Z) + halfangle(W,Z,X) mod 360
By triangle_halfangle_sum on Y, Z, W we get orientation(Y,Z,W) == halfangle(Y,Z,W) + halfangle(Z,W,Y) + halfangle(W,Y,Z) mod 360
By triangle_halfangle_sum on Z, Y, W we get orientation(Z,Y,W) == halfangle(Z,Y,W) + halfangle(Y,W,Z) + halfangle(W,Z,Y) mod 360
By triangle_halfangle_sum on X, W, Y we get orientation(X,W,Y) == halfangle(X,W,Y) + halfangle(W,Y,X) + halfangle(Y,X,W) mod 360
By triangle_halfangle_sum on X, Z, Y we get orientation(X,Z,Y) == halfangle(X,Z,Y) + halfangle(Z,Y,X) + halfangle(Y,X,Z) mod 360
By isosceles_triangle_properties on Y, C, B we get distance(B,Y) == distance(C,Y), angle(C,B,Y) == angle(Y,C,B) mod 360, orientation(Y,C,B) == angle(Y,C,B) + halfangle(B,Y,C) mod 360
By isosceles_triangle_properties on X, A, B we get distance(A,X) == distance(B,X), angle(A,B,X) == angle(X,A,B) mod 360, orientation(X,A,B) == angle(X,A,B) + halfangle(B,X,A) mod 360
By isosceles_triangle_properties on Z, C, D we get distance(C,Z) == distance(D,Z), angle(C,D,Z) == angle(Z,C,D) mod 360, orientation(Z,C,D) == angle(Z,C,D) + halfangle(D,Z,C) mod 360
By isosceles_triangle_properties on W, A, D we get distance(A,W) == distance(D,W), angle(A,D,W) == angle(W,A,D) mod 360, orientation(W,A,D) == angle(W,A,D) + halfangle(D,W,A) mod 360
By isosceles_triangle_properties on X, B, A we get distance(A,X) == distance(B,X), angle(B,A,X) == angle(X,B,A) mod 360, orientation(X,B,A) == angle(X,B,A) + halfangle(A,X,B) mod 360
By triangle_halfangle_sum on B, X, A we get orientation(B,X,A) == halfangle(B,X,A) + halfangle(X,A,B) + halfangle(A,B,X) mod 360
By triangle_halfangle_sum on X, B, A we get orientation(X,B,A) == halfangle(X,B,A) + halfangle(B,A,X) + halfangle(A,X,B) mod 360
By triangle_halfangle_sum on B, Y, C we get orientation(B,Y,C) == halfangle(B,Y,C) + halfangle(Y,C,B) + halfangle(C,B,Y) mod 360
By triangle_halfangle_sum on Y, C, B we get orientation(Y,C,B) == halfangle(Y,C,B) + halfangle(C,B,Y) + halfangle(B,Y,C) mod 360
By triangle_halfangle_sum on D, Z, C we get orientation(D,Z,C) == halfangle(D,Z,C) + halfangle(Z,C,D) + halfangle(C,D,Z) mod 360
By triangle_halfangle_sum on D, W, A we get orientation(D,W,A) == halfangle(D,W,A) + halfangle(W,A,D) + halfangle(A,D,W) mod 360
By triangle_halfangle_sum on A, X, B we get orientation(A,X,B) == halfangle(A,X,B) + halfangle(X,B,A) + halfangle(B,A,X) mod 360
By triangle_halfangle_sum on Z, C, D we get orientation(Z,C,D) == halfangle(Z,C,D) + halfangle(C,D,Z) + halfangle(D,Z,C) mod 360
By triangle_halfangle_sum on W, A, D we get orientation(W,A,D) == halfangle(W,A,D) + halfangle(A,D,W) + halfangle(D,W,A) mod 360
By triangle_halfangle_sum on X, A, B we get orientation(X,A,B) == halfangle(X,A,B) + halfangle(A,B,X) + halfangle(B,X,A) mod 360
By angles_equality_imply_halfangles_equality on B, X, A, D, Z, C we get halfangle(B,X,A) == halfangle(D,Z,C) mod 360
By angles_equality_imply_halfangles_equality on A, X, B, A, W, D we get halfangle(A,W,D) == halfangle(A,X,B) mod 360
By angles_equality_imply_halfangles_equality on C, Y, B, A, W, D we get halfangle(A,W,D) == halfangle(C,Y,B) mod 360
By reverse_direction on A, W we get 180 == direction(A,W) - direction(W,A) mod 360
By reverse_direction on D, Z we get 180 == direction(D,Z) - direction(Z,D) mod 360
By angles_equality_imply_halfangles_equality on C, Y, B, B, Y, C we get halfangle(B,Y,C) == halfangle(C,Y,B) mod 360
By angles_equality_imply_halfangles_equality on B, X, A, A, W, D we get halfangle(A,W,D) == halfangle(B,X,A) mod 360
By reverse_direction on D, A we get 180 == direction(D,A) - direction(A,D) mod 360
By angles_equality_imply_halfangles_equality on D, W, A, C, Y, B we get halfangle(C,Y,B) == halfangle(D,W,A) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on Z, X, Y we get not_collinear(X, Y, Z), exists(Line(X,Y))
By reverse_direction on A, X we get 180 == direction(A,X) - direction(X,A) mod 360
By reverse_direction on X, W we get 180 == direction(X,W) - direction(W,X) mod 360
By reverse_direction on Z, X we get 180 == direction(Z,X) - direction(X,Z) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on Z, W, X we get not_collinear(W, X, Z), exists(Line(W,X))
By not_in_line_equivalent_to_not_collinear_v0 on Y, W, X we get not_collinear(W, X, Y), exists(Line(W,X))
By not_in_line_equivalent_to_not_collinear_v0 on W, Z, Y we get not_collinear(W, Y, Z), exists(Line(Y,Z))
By line_inequality on Line(T,W), Line(X,Y), W we get Line(T,W) != Line(X,Y)
By line_inequality on Line(T,X), Line(X,Y), Z we get Line(T,X) != Line(X,Y)
By collinear_definition on Z, X, T we get X in Line(T,Z), T in Line(X,Z), Line(T,Z) == Line(X,Z), 0 == 2 * angle(X,Z,T) mod 360
By coangle_definition_v0 on X, W, Y we get angle(X,W,Y) == coangle(X,W,Y) + orientation(X,W,Y) mod 360
By coangle_definition_v0 on Y, Z, X we get angle(Y,Z,X) == coangle(Y,Z,X) + orientation(Y,Z,X) mod 360
By coangle_definition_v0 on Z, X, Y we get angle(Z,X,Y) == coangle(Z,X,Y) + orientation(Z,X,Y) mod 360
By coangle_definition_v0 on X, Y, W we get angle(X,Y,W) == coangle(X,Y,W) + orientation(X,Y,W) mod 360
By coangle_definition_v0 on Z, Y, X we get angle(Z,Y,X) == coangle(Z,Y,X) + orientation(Z,Y,X) mod 360
By coangle_definition_v0 on X, W, Z we get angle(X,W,Z) == coangle(X,W,Z) + orientation(X,W,Z) mod 360
By coangle_definition_v0 on Z, X, W we get angle(Z,X,W) == coangle(Z,X,W) + orientation(Z,X,W) mod 360
By collinear_definition on W, T, Y we get T in Line(W,Y), Y in Line(T,W), Line(T,W) == Line(W,Y), 0 == 2 * angle(T,W,Y) mod 360
By coangle_definition_v0 on Z, Y, W we get angle(Z,Y,W) == coangle(Z,Y,W) + orientation(Z,Y,W) mod 360
By coangle_definition_v0 on W, Y, Z we get angle(W,Y,Z) == coangle(W,Y,Z) + orientation(W,Y,Z) mod 360
By angle_equality_conversions_v0 on D, W, A, B, X, A we get coangle(B,X,A) == coangle(D,W,A) mod 360, orientation(B,X,A) == orientation(D,W,A) mod 360       
By angle_equality_conversions_v0 on A, X, B, B, Y, C we get coangle(A,X,B) == coangle(B,Y,C) mod 360, orientation(A,X,B) == orientation(B,Y,C) mod 360       
By angle_equality_conversions_v0 on D, Z, C, D, W, A we get coangle(D,W,A) == coangle(D,Z,C) mod 360, orientation(D,W,A) == orientation(D,Z,C) mod 360       
By triangle_halfangle_sum on X, Y, T we get orientation(X,Y,T) == halfangle(X,Y,T) + halfangle(Y,T,X) + halfangle(T,X,Y) mod 360
By triangle_halfangle_sum on T, Y, Z we get orientation(T,Y,Z) == halfangle(T,Y,Z) + halfangle(Y,Z,T) + halfangle(Z,T,Y) mod 360
By triangle_halfangle_sum on T, X, W we get orientation(T,X,W) == halfangle(T,X,W) + halfangle(X,W,T) + halfangle(W,T,X) mod 360
By triangle_halfangle_sum on T, X, Y we get orientation(T,X,Y) == halfangle(T,X,Y) + halfangle(X,Y,T) + halfangle(Y,T,X) mod 360
By triangle_halfangle_sum on Y, Z, T we get orientation(Y,Z,T) == halfangle(Y,Z,T) + halfangle(Z,T,Y) + halfangle(T,Y,Z) mod 360
By triangle_halfangle_sum on X, W, T we get orientation(X,W,T) == halfangle(X,W,T) + halfangle(W,T,X) + halfangle(T,X,W) mod 360
By line_unique_intersection_v1 on Line(T,W), Line(X,Y), Y, X we get X not in Line(T,W)
By line_unique_intersection_v1 on Line(T,X), Line(X,Y), X, Y we get Y not in Line(T,X)
By same_angle on X, Z, T, W we get coangle(T,X,W) == coangle(Z,X,W) mod 360
By same_angle on X, Z, T, Y we get coangle(T,X,Y) == coangle(Z,X,Y) mod 360
By same_angle on Y, W, T, Z we get coangle(T,Y,Z) == coangle(W,Y,Z) mod 360
By reverse_orientation on W, Z, Y we get orientation(W,Z,Y) == 0 - orientation(Y,Z,W) mod 360
By reverse_orientation on W, Y, X we get orientation(W,Y,X) == 0 - orientation(X,Y,W) mod 360
By reverse_orientation on X, Z, Y we get orientation(X,Z,Y) == 0 - orientation(Y,Z,X) mod 360
By divide_by_2_two_angles on X, W, Y, X, W, T we get coangle(X,W,T) == coangle(X,W,Y) mod 360
By coangle_definition_v0 on T, X, W we get angle(T,X,W) == coangle(T,X,W) + orientation(T,X,W) mod 360
By coangle_definition_v0 on T, X, Y we get angle(T,X,Y) == coangle(T,X,Y) + orientation(T,X,Y) mod 360
By coangle_definition_v0 on X, W, T we get angle(X,W,T) == coangle(X,W,T) + orientation(X,W,T) mod 360
By coangle_definition_v0 on X, Y, T we get angle(X,Y,T) == coangle(X,Y,T) + orientation(X,Y,T) mod 360
By coangle_definition_v0 on T, Y, Z we get angle(T,Y,Z) == coangle(T,Y,Z) + orientation(T,Y,Z) mod 360
By coangle_definition_v0 on Y, Z, T we get angle(Y,Z,T) == coangle(Y,Z,T) + orientation(Y,Z,T) mod 360
By divide_by_2_two_angles on X, Y, W, X, Y, T we get coangle(X,Y,T) == coangle(X,Y,W) mod 360
By divide_by_2_two_angles on Y, Z, X, Y, Z, T we get coangle(Y,Z,T) == coangle(Y,Z,X) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on Y, T, Z we get not_collinear(T, Y, Z), exists(Line(T,X))
By not_in_line_equivalent_to_not_collinear_v0 on X, W, T we get not_collinear(T, W, X), exists(Line(T,W))
By sas_similarity on C, B, A, Y, B, X we get similar_triangles(A, B, C, X, B, Y)
By sas_similarity on D, C, B, Z, C, Y we get similar_triangles(B, C, D, Y, C, Z)
By sas_similarity on C, D, A, Z, D, W we get similar_triangles(A, C, D, W, Z, D)
By sas_similarity on D, A, B, W, A, X we get similar_triangles(A, B, D, A, X, W)
By divide_by_2_two_angles on Z, Y, X, X, W, Z we get coangle(X,W,Z) == coangle(Z,Y,X) mod 360
By divide_by_2_two_angles on X, W, T, Z, Y, W we get coangle(X,W,T) == coangle(Z,Y,W) mod 360
By congruence_from_similar_triangles on Y, W, X, W, Y, Z we get congruent_triangles(W, X, Y, Y, Z, W)
By congruence_from_similar_triangles on Y, Z, T, W, X, T we get congruent_triangles(T, W, X, T, Y, Z)
