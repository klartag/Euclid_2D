Assumptions:
A, B, C, D, X, Y, Z: Point
distinct(A, B, C, D, X, Y, Z)

concyclic(A, B, C, D)

between(X, A, B)
between(X, D, C)

between(B, C, Y)
between(A, D, Y)

Line(X, Z) == internal_angle_bisector(A, X, D)
Line(Y, Z) == internal_angle_bisector(C, Y, D)

Need to prove:
perpendicular(Line(X, Z), Line(Y, Z))

Proof:
By between_implies_orientation on B, Y, D, A we get orientation(B,D,A) == orientation(B,Y,D) mod 360, orientation(B,Y,A) == orientation(B,Y,D) mod 360       
By between_implies_orientation on D, B, C, Y we get orientation(D,B,C) == orientation(D,C,Y) mod 360, orientation(D,B,C) == orientation(D,B,Y) mod 360       
By between_implies_orientation on X, Y, C, B we get orientation(X,C,B) == orientation(X,Y,C) mod 360, orientation(X,Y,B) == orientation(X,Y,C) mod 360       
By between_implies_orientation on A, X, D, C we get orientation(A,D,C) == orientation(A,X,D) mod 360, orientation(A,X,C) == orientation(A,X,D) mod 360       
By between_implies_orientation on C, B, A, X we get orientation(C,A,X) == orientation(C,B,A) mod 360, orientation(C,B,A) == orientation(C,B,X) mod 360       
By between_implies_orientation on Y, C, D, X we get orientation(Y,C,D) == orientation(Y,D,X) mod 360, orientation(Y,C,D) == orientation(Y,C,X) mod 360       
By between_implies_orientation on A, B, C, Y we get orientation(A,B,C) == orientation(A,C,Y) mod 360, orientation(A,B,C) == orientation(A,B,Y) mod 360       
By between_implies_orientation on D, X, A, B we get orientation(D,A,B) == orientation(D,X,A) mod 360, orientation(D,X,A) == orientation(D,X,B) mod 360       
By between_implies_orientation on X, Y, D, A we get orientation(X,D,A) == orientation(X,Y,D) mod 360, orientation(X,Y,A) == orientation(X,Y,D) mod 360       
By between_implies_orientation on Y, B, A, X we get orientation(Y,A,X) == orientation(Y,B,A) mod 360, orientation(Y,B,A) == orientation(Y,B,X) mod 360       
By concyclic_definition_0 on C, B, A, D we get D in Circle(A,B,C)
By concyclic_definition_0 on A, D, C, B we get B in Circle(A,C,D)
By concyclic_definition_0 on A, B, D, C we get C in Circle(A,B,D)
By concyclic_definition_0 on D, C, B, A we get A in Circle(B,C,D)
By collinear_definition on A, Y, D we get Y in Line(A,D), D in Line(A,Y), Line(A,D) == Line(A,Y), 0 == 2 * angle(Y,A,D) mod 360
By collinear_definition on Y, D, A we get D in Line(A,Y), A in Line(D,Y), Line(A,Y) == Line(D,Y), 0 == 2 * angle(D,Y,A) mod 360
By collinear_definition on C, D, X we get D in Line(C,X), X in Line(C,D), Line(C,D) == Line(C,X), 0 == 2 * angle(D,C,X) mod 360
By collinear_definition on C, Y, B we get Y in Line(B,C), B in Line(C,Y), Line(B,C) == Line(C,Y), 0 == 2 * angle(Y,C,B) mod 360
By collinear_definition on D, C, X we get C in Line(D,X), X in Line(C,D), Line(C,D) == Line(D,X), 0 == 2 * angle(C,D,X) mod 360
By internal_angle_bisector_definition_v0 on D, Z, A, X we get angle(D,X,Z) == angle(Z,X,A) mod 360
By angles_on_chord on C, A, B, D, Circle(A,B,C) we get coangle(C,B,A) == coangle(C,D,A) mod 360
By angles_on_chord on B, D, A, C, Circle(A,B,C) we get coangle(B,A,D) == coangle(B,C,D) mod 360
By angles_on_chord on A, C, B, D, Circle(A,B,C) we get coangle(A,B,C) == coangle(A,D,C) mod 360
By orientations_are_cyclic on B, D, A we get orientation(B,D,A) == orientation(D,A,B) mod 360, orientation(A,B,D) == orientation(B,D,A) mod 360
By orientations_are_cyclic on A, D, X we get orientation(A,D,X) == orientation(D,X,A) mod 360, orientation(A,D,X) == orientation(X,A,D) mod 360
By orientations_are_cyclic on X, Y, C we get orientation(X,Y,C) == orientation(Y,C,X) mod 360, orientation(C,X,Y) == orientation(X,Y,C) mod 360
By reverse_orientation on A, B, C we get orientation(A,B,C) == 0 - orientation(C,B,A) mod 360
By orientations_are_cyclic on Y, D, X we get orientation(D,X,Y) == orientation(Y,D,X) mod 360, orientation(X,Y,D) == orientation(Y,D,X) mod 360
By orientations_are_cyclic on Y, A, B we get orientation(A,B,Y) == orientation(Y,A,B) mod 360, orientation(B,Y,A) == orientation(Y,A,B) mod 360
By orientations_are_cyclic on A, X, C we get orientation(A,X,C) == orientation(X,C,A) mod 360, orientation(A,X,C) == orientation(C,A,X) mod 360
By orientations_are_cyclic on D, C, Y we get orientation(C,Y,D) == orientation(D,C,Y) mod 360, orientation(D,C,Y) == orientation(Y,D,C) mod 360
By reverse_direction on X, A we get 180 == direction(X,A) - direction(A,X) mod 360
By orientations_are_cyclic on B, Y, D we get orientation(B,Y,D) == orientation(Y,D,B) mod 360, orientation(B,Y,D) == orientation(D,B,Y) mod 360
By orientations_are_cyclic on A, X, D we get orientation(A,X,D) == orientation(X,D,A) mod 360, orientation(A,X,D) == orientation(D,A,X) mod 360
By reverse_direction on C, D we get 180 == direction(C,D) - direction(D,C) mod 360
By orientations_are_cyclic on Y, B, X we get orientation(B,X,Y) == orientation(Y,B,X) mod 360, orientation(X,Y,B) == orientation(Y,B,X) mod 360
By reverse_direction on C, Y we get 180 == direction(C,Y) - direction(Y,C) mod 360
By reverse_direction on D, X we get 180 == direction(D,X) - direction(X,D) mod 360
By reverse_direction on Y, D we get 180 == direction(Y,D) - direction(D,Y) mod 360
By reverse_direction on A, D we get 180 == direction(A,D) - direction(D,A) mod 360
By same_angle on A, B, X, D we get coangle(B,A,D) == coangle(X,A,D) mod 360
By same_angle on D, A, Y, C we get coangle(A,D,C) == coangle(Y,D,C) mod 360
By same_angle on B, C, Y, A we get coangle(C,B,A) == coangle(Y,B,A) mod 360
By same_angle on C, B, Y, D we get coangle(B,C,D) == coangle(Y,C,D) mod 360
By same_angle on D, C, X, A we get coangle(C,D,A) == coangle(X,D,A) mod 360
By internal_angle_bisector_definition_v0 on D, Z, C, Y we get angle(D,Y,Z) == angle(Z,Y,C) mod 360
By angle_equality_conversions_v0_r on C, B, A, Y, B, A we get angle(C,B,A) == angle(Y,B,A) mod 360
By coangle_definition_v1 on Y, C, D we get angle(Y,C,D) == coangle(Y,C,D) + orientation(Y,C,D) mod 360
By angle_equality_conversions_v0_r on X, D, A, Y, B, A we get angle(X,D,A) == angle(Y,B,A) mod 360
By coangle_definition_v1 on X, A, D we get angle(X,A,D) == coangle(X,A,D) + orientation(X,A,D) mod 360
By angle_equality_conversions_v0_r on A, B, C, Y, D, C we get angle(A,B,C) == angle(Y,D,C) mod 360
By reverse_direction on Y, Z we get 180 == direction(Y,Z) - direction(Z,Y) mod 360
By perpendicular_direction_conditions_v0 on Z, Y, X, Z we get perpendicular(Line(X,Z), Line(Y,Z))
