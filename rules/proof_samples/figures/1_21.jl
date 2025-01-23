Assumptions:
A, B, C, D, X: Point
distinct(A, B, C, D, X)

concyclic(A, B, C, D)

X == line_intersection(Line(A, C), Line(B, D))

Need to prove:
distance(A, X) * distance(C, X) == distance(B, X) * distance(D, X)

Proof:
By in_imply_collinear on X, D, B we get collinear(B, D, X)
By in_imply_collinear on X, C, A we get collinear(A, C, X)
By concyclic_definition_0 on B, A, C, D we get D in Circle(A,B,C)
By line_circle_intersection_has_at_most_two_points_0 on B, D, X, Circle(A,B,C) we get X not in Circle(A,B,C)
By power_of_a_point_definition on X, C, A, Circle(A,B,C) we get log(power_of_a_point(X,Circle(A,B,C))) == log(distance(C,X)) + log(distance(A,X))
By power_of_a_point_definition on X, B, D, Circle(A,B,C) we get log(power_of_a_point(X,Circle(A,B,C))) == log(distance(B,X)) + log(distance(D,X))
