Assumptions:
A, B, C, X, Y, Z, W: Point
c: Circle
distinct(A, B, C, W, X, Y, Z)
A, B, C, X, W in c
Y, Z in Line(W, X)
Y in Line(A, B)
Z in Line(A, C)
distance(A, W) == distance(A, X)

Need to prove:
concyclic(B, C, Y, Z)

Proof:
By line_definition on Y, W, Line(W, X) we get Line(W, X) == Line(W, Y)
By line_definition on Y, Z, Line(W, X) we get Line(W, X) == Line(Y, Z)
By line_definition on Z, C, Line(A, C) we get Line(A, C) == Line(C, Z)
By circle_definition on X, A, B, c we get c == Circle(A, B, X)
By circle_definition on A, C, B, c we get c == Circle(A, B, C)
By circle_definition on W, B, X, c we get c == Circle(B, W, X)
By angles_on_chord on A, B, C, X, c we get coangle(A, C, B) == coangle(A, X, B) mod 360
By angles_on_chord on B, W, A, X, c we get coangle(B, A, W) == coangle(B, X, W) mod 360
By in_imply_collinear on Y, W, X we get collinear(W, X, Y)
By in_imply_collinear on Z, C, A we get collinear(A, C, Z)
By in_imply_collinear on Y, B, A we get collinear(A, B, Y)
By isosceles_triangle_properties on A, X, W we get distance(A, W) == distance(A, X), angle(A, X, W) == angle(X, W, A) mod 360, orientation(A, X, W) == angle(A, X, W) + halfangle(W, A, X) mod 360
By in_imply_collinear on Z, W, Y we get collinear(W, Y, Z)
By reverse_direction on A, X we get 180 == direction(A, X) - direction(X, A) mod 360
By not_in_line_equivalent_to_not_collinear_v0_r on B, X, W we get B not in Line(W, X)
By not_in_line_equivalent_to_not_collinear_v0_r on B, A, C we get B not in Line(A, C)
By coangle_definition_v1 on B, A, W we get angle(B, A, W) == coangle(B, A, W) + orientation(B, A, W) mod 360
By coangle_definition_v1 on B, X, W we get angle(B, X, W) == coangle(B, X, W) + orientation(B, X, W) mod 360
By collinear_definition on X, Y, W we get Y in Line(W, X), W in Line(X, Y), Line(W, X) == Line(X, Y), 0 == 2 * angle(Y, X, W) mod 360
By collinear_definition on Y, W, X we get W in Line(X, Y), X in Line(W, Y), Line(W, Y) == Line(X, Y), 0 == 2 * angle(W, Y, X) mod 360
By collinear_definition on B, Y, A we get Y in Line(A, B), A in Line(B, Y), Line(A, B) == Line(B, Y), 0 == 2 * angle(Y, B, A) mod 360
By same_angle on C, A, Z, B we get coangle(A, C, B) == coangle(Z, C, B) mod 360
By reverse_direction on B, Y we get 180 == direction(B, Y) - direction(Y, B) mod 360
By reverse_direction on A, B we get 180 == direction(A, B) - direction(B, A) mod 360
By reverse_direction on X, Y we get 180 == direction(X, Y) - direction(Y, X) mod 360
By not_in_line_equivalent_to_not_collinear_v0 on B, Z, Y we get not_collinear(B, Y, Z), exists(Line(Y, Z))
By not_in_line_equivalent_to_not_collinear_v0 on B, C, Z we get not_collinear(B, C, Z), exists(Line(C, Z))
By same_angle on Y, Z, W, B we get coangle(W, Y, B) == coangle(Z, Y, B) mod 360
By divide_by_2_two_angles on A, X, B, W, Y, B we get coangle(A, X, B) == coangle(W, Y, B) mod 360
By concyclic_sufficient_conditions on Z, C, B, Y we get concyclic(B, C, Y, Z)
