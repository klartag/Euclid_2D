Assumptions:
A, B, C, D, X, Y, Z, W, P: Point
c: Circle
distinct(A, B, C, D, X, Y, Z, W, P)
A, B, C, D, X, Y, Z, W in c

distance(A, X) == distance(B, X)
distance(B, Y) == distance(C, Y)
distance(C, Z) == distance(D, Z)
distance(D, W) == distance(A, W)

convex(A, X, B, Y, C, Z, D, W)

Need to prove:
perpendicular(Line(X, Z), Line(Y, W))

Proof:
By circle_definition on A, Z, X, c we get c == Circle(A,X,Z)
By circle_definition on A, Z, W, c we get c == Circle(A,W,Z)
By angles_on_chord on X, B, Z, D, c we get coangle(X,D,B) == coangle(X,Z,B) mod 360
By angles_on_chord on X, B, Z, C, c we get coangle(X,C,B) == coangle(X,Z,B) mod 360
By angles_on_chord on C, X, B, Z, c we get coangle(C,B,X) == coangle(C,Z,X) mod 360
By angles_on_chord on Z, X, A, W, c we get coangle(Z,A,X) == coangle(Z,W,X) mod 360
By angles_on_chord on C, X, Y, W, c we get coangle(C,W,X) == coangle(C,Y,X) mod 360
By angles_on_chord on W, Z, A, C, c we get coangle(W,A,Z) == coangle(W,C,Z) mod 360
By angles_on_chord on X, B, D, Y, c we get coangle(X,D,B) == coangle(X,Y,B) mod 360
By angles_on_chord on W, Z, C, D, c we get coangle(W,C,Z) == coangle(W,D,Z) mod 360
By angles_on_chord on C, X, W, B, c we get coangle(C,B,X) == coangle(C,W,X) mod 360
By angles_on_chord on X, B, A, C, c we get coangle(X,A,B) == coangle(X,C,B) mod 360
By angles_on_chord on C, A, W, Z, c we get coangle(C,W,A) == coangle(C,Z,A) mod 360
By angles_on_chord on Z, X, C, W, c we get coangle(Z,C,X) == coangle(Z,W,X) mod 360
By angles_on_chord on C, A, X, W, c we get coangle(C,W,A) == coangle(C,X,A) mod 360
By angles_on_chord on C, A, X, D, c we get coangle(C,D,A) == coangle(C,X,A) mod 360
By angles_on_chord on C, A, B, Z, c we get coangle(C,B,A) == coangle(C,Z,A) mod 360
By angles_on_chord on A, Y, B, W, c we get coangle(A,B,Y) == coangle(A,W,Y) mod 360
By orientations_are_cyclic on Y, B, X we get orientation(B,X,Y) == orientation(Y,B,X) mod 360, orientation(X,Y,B) == orientation(Y,B,X) mod 360
By orientations_are_cyclic on A, W, Z we get orientation(A,W,Z) == orientation(W,Z,A) mod 360, orientation(A,W,Z) == orientation(Z,A,W) mod 360
By orientations_are_cyclic on B, X, A we get orientation(B,X,A) == orientation(X,A,B) mod 360, orientation(A,B,X) == orientation(B,X,A) mod 360
By orientations_are_cyclic on B, X, C we get orientation(B,X,C) == orientation(X,C,B) mod 360, orientation(B,X,C) == orientation(C,B,X) mod 360
By isosceles_triangle_properties on X, A, B we get distance(A,X) == distance(B,X), angle(A,B,X) == angle(X,A,B) mod 360, orientation(X,A,B) == angle(X,A,B) + halfangle(B,X,A) mod 360
By isosceles_triangle_properties on Y, C, B we get distance(B,Y) == distance(C,Y), angle(C,B,Y) == angle(Y,C,B) mod 360, orientation(Y,C,B) == angle(Y,C,B) + halfangle(B,Y,C) mod 360
By isosceles_triangle_properties on W, A, D we get distance(A,W) == distance(D,W), angle(A,D,W) == angle(W,A,D) mod 360, orientation(W,A,D) == angle(W,A,D) + halfangle(D,W,A) mod 360
By isosceles_triangle_properties on Z, C, D we get distance(C,Z) == distance(D,Z), angle(C,D,Z) == angle(Z,C,D) mod 360, orientation(Z,C,D) == angle(Z,C,D) + halfangle(D,Z,C) mod 360
By reverse_direction on B, Y we get 180 == direction(B,Y) - direction(Y,B) mod 360
By reverse_direction on C, D we get 180 == direction(C,D) - direction(D,C) mod 360
By reverse_direction on D, Z we get 180 == direction(D,Z) - direction(Z,D) mod 360
By reverse_orientation on Z, A, W we get orientation(Z,A,W) == 0 - orientation(W,A,Z) mod 360
By coangle_definition_v1 on C, D, A we get angle(C,D,A) == coangle(C,D,A) + orientation(C,D,A) mod 360
By reverse_direction on A, B we get 180 == direction(A,B) - direction(B,A) mod 360
By reverse_direction on C, Y we get 180 == direction(C,Y) - direction(Y,C) mod 360
By coangle_definition_v1 on C, B, X we get angle(C,B,X) == coangle(C,B,X) + orientation(C,B,X) mod 360
By reverse_direction on D, A we get 180 == direction(D,A) - direction(A,D) mod 360
By reverse_direction on A, W we get 180 == direction(A,W) - direction(W,A) mod 360
By coangle_definition_v1 on W, D, Z we get angle(W,D,Z) == coangle(W,D,Z) + orientation(W,D,Z) mod 360
By coangle_definition_v1 on C, B, A we get angle(C,B,A) == coangle(C,B,A) + orientation(C,B,A) mod 360
By reverse_orientation on X, A, Z we get orientation(X,A,Z) == 0 - orientation(Z,A,X) mod 360
By coangle_definition_v1 on A, B, Y we get angle(A,B,Y) == coangle(A,B,Y) + orientation(A,B,Y) mod 360
By coangle_definition_v1 on C, Z, X we get angle(C,Z,X) == coangle(C,Z,X) + orientation(C,Z,X) mod 360
By angle_equality_conversions_v0_r on X, A, B, X, Y, B we get angle(X,A,B) == angle(X,Y,B) mod 360
By coangle_definition_v1 on W, A, Z we get angle(W,A,Z) == coangle(W,A,Z) + orientation(W,A,Z) mod 360
By angle_equality_conversions_v0_r on C, Y, X, C, B, X we get angle(C,B,X) == angle(C,Y,X) mod 360
By coangle_definition_v1 on Z, A, X we get angle(Z,A,X) == coangle(Z,A,X) + orientation(Z,A,X) mod 360
By angle_equality_conversions_v0_r on X, A, B, X, C, B we get angle(X,A,B) == angle(X,C,B) mod 360
By coangle_definition_v1 on Z, C, X we get angle(Z,C,X) == coangle(Z,C,X) + orientation(Z,C,X) mod 360
By coangle_definition_v1 on A, W, Y we get angle(A,W,Y) == coangle(A,W,Y) + orientation(A,W,Y) mod 360
By perpendicular_direction_conditions_v0 on Z, X, W, Y we get perpendicular(Line(W,Y), Line(X,Z))
