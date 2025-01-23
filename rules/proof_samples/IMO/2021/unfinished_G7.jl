Assumptions:
A, B, C, D, E, F ,X, O_1, O_2: Point
distinct(A, B, C, D, E, F ,X, O_1, O_2)
acute_triangle(A, B, C)
distance(A, B) != distance(A, C)
inside_triangle(D, A, B, C)
Line(A, D) == internal_angle_bisector(B, A, C)
between(A, E, C)
angle(A, D, E) == angle(B, C, D)
between(A, F, B)
angle(A, D, F) == angle(C, B, D)
X in Line(A, C)
distance(X, C) == distance(X, B)
O_1 == circumcenter(A, D, C)
O_2 == circumcenter(X, D, E)

Need to prove:
concurrent(Line(O_1, O_2), Line(B, C), Line(E, F))

Proof:
Let Q := isogonal_conjugate(D, A, B, C)
It is almost always true that distinct(A, B, C, D, E, F ,X, O_1, O_2, Q)
We have proved Q in Line(A, D)
By in_imply_collinear on Q, A, D we get collinear(Q, A, D)
# prove that concyclic(F, D, Q, B)
By isogonal_conjugate_halve_the_angle on A, B, C, D, Q we get angle(D, B, C) == angle(A, B, Q)
By same_angle_v3 on Q, B, F, A we get angle(Q, B, F) == angle(Q, B, A) mod 360
By complementary_angles_180_v0 on F, A, D, Q we get angle(A, D, F) + angle(F, D, Q) == 0 mod 180
It is almost always true that triangle(D, F, Q)
By four_points_concyclic_sufficient_conditions_v0 on F, D, Q, B we get concyclic(F, D, Q, B)
#_
# prove that concyclic(E, D, Q, C)
By isogonal_conjugate_halve_the_angle on A, C, B, D, Q we get angle(D, C, B) == angle(A, C, Q)       
By same_angle_v3 on Q, C, E, A we get angle(Q, C, E) == angle(Q, C, A) mod 360
By complementary_angles_180_v0 on E, A, D, Q we get angle(A, D, E) + angle(E, D, Q) == 0 mod 180     
It is almost always true that triangle(D, E, Q)
By four_points_concyclic_sufficient_conditions_v0 on E, D, Q, C we get concyclic(E, D, Q, C)
#_
# using power of a point to prove concyclic(B, F, E, C)
By isogonal_conjugate_of_inside_point_is_inside on A, B, C, D, Q we get inside_triangle(Q, A, B, C)
By two_points_inside_triangle_and_triangle_vertex_collinear on A, B, C, D, Q we get collinear_and_not_between(D, A, Q)
By between_imply_not_between on A, F, B we get collinear_and_not_between(F, A, B)
By power_of_a_point_concyclic_condition_v1_r on A, B, F, D, Q we get log(distance(A, F)) + log(distance(A, B)) == log(distance(A, D)) + log(distance(A, Q)) 
By between_imply_not_between on A, E, C we get collinear_and_not_between(E, A, C)
By power_of_a_point_concyclic_condition_v1_r on A, C, E, D, Q we get log(distance(A, E)) + log(distance(A, C)) == log(distance(A, D)) + log(distance(A, Q)) 
It is almost always true that triangle(B, E, F)
By power_of_a_point_concyclic_condition_v1 on A, F, B, E, C we get concyclic(F, B, E, C)
#_
It is almost always true that line_angle(Line(F, E)) != line_angle(Line(B, C)) mod 180 # highly non trivial to prove!
Let T := line_intersection(Line(F, E), Line(B, C))
It is almost always true that distinct(A, B, C, D, E, F ,X, O_1, O_2, Q, T)
# claim: log(distance(T, D)) + log(distance(T, D)) == log(distance(T, B)) + log(distance(T, C))
# log(distance(T, D)) + log(distance(T, D)) == log(distance(T, F)) + log(distance(T, E))
## tangent(Circle(D, E, F), Circle(B, D, C))
### angle computation:
We have proved angle(B, D, F) == angle(A, F, D) - angle(A, B, D) mod 180
It is almost always true that triangle(A, F, D)
We have proved angle(A, F, D) == - angle(F, D , A) - angle(D, A, F) mod 180
We have proved angle(A, B, D) == angle(A, B, C) - angle(D, B, C) mod 180
We have proved angle(B, D, F) == - angle(D, A, F) - angle(A, B, C) mod 180
By angles_on_chord on F, C, E, B, Circle(F, E, B) we get angle(F, E, C) == angle(F, B, C) mod 180
We have proved angle(F, B, C) == angle(A, B, C) mod 180
By complementary_angles_180_v0 on F, C, E, A we get angle(C, E, F) + angle(F, E, A) == 0 mod 180
We have proved angle(A, B, C) == angle(F, E, A) mod 180
We have proved angle(F, A, D) == angle(D, A, E) mod 180
We have proved angle(B, D, F) == - angle(E, A, D) - angle(F, E, A) mod 180
We have proved angle(B, D, F) == angle(D, E, F) + angle(A, D, E) mod 180
We have proved angle(B, D, F) == angle(D, E, F) + angle(B, C, D) mod 180
###_
It is almost always true that triangle(F, D, E)
By two_tangent_circles_angles_on_chord_v0 on B, C, D, E, F, Circle(B, C, D), Circle(D, E, F) we get tangent(Circle(B, C, D), Circle(D, E, F))
##_
By power_of_a_point_concyclic_condition_v2 on T, E, F, B, C we get log(distance(T, F)) + log(distance(T, E)) == log(distance(T, B)) + log(distance(T, C)), good_position_for_power_of_a_point(E, F, B, C)
It is almost always true that circumcenter(E, F, D) != circumcenter(B, C, D) # should be an autmatic conclusion of the tangency of the circles
By equal_power_on_radical_v5 on T, F, E, C, B, Circle(E, F, D), Circle(B, C, D) we get T in radical_axis(Circle(F, E, D), Circle(B, C, D))
By point_in_the_intersection_is_in_radical_axis on D, Circle(E, F, D), Circle(B, C, D) we get D in radical_axis(Circle(F, E, D), Circle(B, C, D))
By Line_definition on D, T, radical_axis(Circle(F, E, D), Circle(B, C, D)) we get radical_axis(Circle(F, E, D), Circle(B, C, D)) == Line(D, T)
It is almost always true that Circle(F, E, D) != Circle(B, C, D)
By radical_axis_of_tangent_circles_v1 on D, Line(T, D), Circle(B, C, D), Circle(D, E, F) we get tangent(Line(T, D), Circle(B, C, D)), tangent(Line(T, D), Circle(D, E, F))
By line_circle_other_intersection_definition_v2 on D, D, Line(T, D), Circle(D, E, F) we get D == line_circle_other_intersection(D, Line(T, D), Circle(D, E, F))
By equal_power_on_radical_tangent_case on T, E, F, D we get distance(T, D) * distance(T, D) == distance(T, F) * distance(T, E)
We have proved log(distance(T, D)) + log(distance(T, D)) == log(distance(T, F)) + log(distance(T, E))
#_
Let M := line_circle_other_intersection(A, Line(A, T), Circle(A, B, C))
It is almost always true that distinct(A, B, C, D, E, F ,X, O_1, O_2, Q, T, M)
By in_imply_collinear on M, A, T we get collinear(A, M, T)
It is almost always true that triangle(A, B, M)
By four_points_concyclic_sufficient_conditions_v1 on A, B, C, M we get concyclic(A, B, C, M)
It is almost always true that triangle(A, E, F)
It is almost always true that line_angle(Line(A, M)) != line_angle(Line(B, C)) mod 180 
By line_intersection_definition on T, Line(A, M), Line(B, C) we get T == line_intersection(Line(A, M), Line(B, C))
By power_of_a_point_concyclic_condition_v2 on T, B, C, A, M we get log(distance(T, B)) + log(distance(T, C)) == log(distance(T, M)) + log(distance(T, A)), good_position_for_power_of_a_point(A, M, B, C)

By point_on_tangent_is_outside_primitive_version T, D, Circle(E, F, D) we get outside_circle(T, Circle(E, F, D))
By in_imply_collinear on T, F, E we get collinear(T, F, E)
By circle_and_orientation_of_three_collinear_points_v0 on F, E, T, Circle(E, F, D) we get collinear_and_not_between(F, T, E)

By point_on_tangent_is_outside_primitive_version T, D, Circle(B, C, D) we get outside_circle(T, Circle(B, C, D))
By in_imply_collinear on T, B, C we get collinear(T, B, C)
By circle_and_orientation_of_three_collinear_points_v0 on B, C, T, Circle(B, C, D) we get collinear_and_not_between(B, T, C)

