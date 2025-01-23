Assumptions:
A, B, C, D: Point
I, X, Y, Z, T: Point
c, w: Circle
distinct(A, B, C, D, I, X, Y, Z, T)

convex(A, B, C, D)

w == Circle(A, I, C)

# c is inscribed inside ABCD:
tangent(Line(A, B), c)
tangent(Line(B, C), c)
tangent(Line(C, D), c)
tangent(Line(D, A), c)

I == center(c)
inside_quadrilateral(I, A, B, C, D)

triangle(A, B, I) 
triangle(B, C, I)
triangle(C, D, I)
triangle(D, A, I)

#!# somthing wrong with possible conclusions of inside_quadrilateral - it supposed to derive all of that automaticaly
# identical(orientation(A, B, I), orientation(B, C, I), orientation(C, D, I), orientation(D, A, I))
##

between(D, tangent_Point(Line(C, D), c), C)
between(D, tangent_Point(Line(D, A), c), A)
between(A, tangent_Point(Line(A, B), c), B)
between(B, tangent_Point(Line(B, C), c), C)

between(B, A, X)
X == line_circle_other_intersection(A, Line(A, B), w)
between(B, C, Z)
Z == line_circle_other_intersection(C, Line(C, B), w)
between(A, D, Y)
Y == line_circle_other_intersection(A, Line(A, D), w)
between(C, D, T)
T == line_circle_other_intersection(C, Line(C, D), w)



Need to prove:
distance(A, D) + distance(D, T) + distance(T, X) + distance(X, A) == distance(C, D) + distance(D, Y) + distance(Y, Z) + distance(Z, C) 

Proof:
Let R := tangent_Point(Line(C, D), c)
Let S := tangent_Point(Line(D, A), c)
Let P := tangent_Point(Line(A, B), c)
Let Q := tangent_Point(Line(B, C), c)
It is almost always true that distinct(A, B, C, D, I, X, Y, Z, T, R, S, P, Q)


# ZI == TI
Let l := Line(I, C)
We introduce Line(P, I)
We introduce Line(S, I)
We introduce Line(R, I)
We introduce Line(Q, I)
## show that l == external_angle_bisector(Z, C, T)
By two_tangents_angle_bisector_v0_r on C, R, Q, Line(C, I), c we get Line(C, I) == internal_angle_bisector(R, C, Q)#angle(T, C, I) == angle(I, C, B) mod 180
It is almost always true that not_collinear(C, I, T)
By between_imply_same_orientation I, C, D, T we get orientation(C, D, I) == orientation(C, T, I)
We have proved orientation(B, C, I) == orientation(C, T, I)
It is almost always true that triangle(B, C, T)
By internal_angle_bisector_definition on B, C, T, I we get Line(C, I) == internal_angle_bisector(T, C, B) 
By angle_bisectors_on_same_line_v4 on T, B, C, Z we get internal_angle_bisector(T, C, B) == external_angle_bisector(T, C, Z)
We have proved l == external_angle_bisector(T, C, Z)
##_
By Circle_definition on Z, C, T, w we get w == Circle(Z, C, T)
By line_circle_other_intersection_definition_v3 on C, I, l, Circle(T, C, Z) we get I == line_circle_other_intersection(C, l, Circle(T, C, Z))
By external_angle_bisector_intersect_circle on Z, C, T, I we get distance(Z, I) == distance(I, T)
#_
# XI == YI
Let l_2 := Line(I, A)
## show that l == external_angle_bisector(X, A, Y)
By two_tangents_angle_bisector_v0_r on A, S, P, Line(A, I), c we get Line(A, I) == internal_angle_bisector(S, A, P)#angle(T, C, I) == angle(I, C, B) mod 180
It is almost always true that not_collinear(A, I, Y)
By between_imply_same_orientation I, A, D, Y we get orientation(A, D, I) == orientation(A, Y, I)
We have proved orientation(B, A, I) == orientation(A, Y, I)
It is almost always true that triangle(B, A, Y)
By internal_angle_bisector_definition on B, A, Y, I we get Line(A, I) == internal_angle_bisector(Y, A, B) 
By angle_bisectors_on_same_line_v4 on Y, B, A, X we get internal_angle_bisector(Y, A, B) == external_angle_bisector(Y, A, X)
We have proved l_2 == external_angle_bisector(Y, A, X)
##_
By Circle_definition on X, A, Y, w we get w == Circle(X, A, Y)
By line_circle_other_intersection_definition_v3 on A, I, l_2, Circle(Y, A, X) we get I == line_circle_other_intersection(A, l_2, Circle(Y, A, X))
By external_angle_bisector_intersect_circle on X, A, Y, I we get distance(X, I) == distance(I, Y)
#_
Let O := center(w)
# show that X == line_reflection(Y, Line(I, O))
By two_points_on_circle on X, Y, w we get distance(X, O) == distance(Y, O)
By point_on_circle on X, w we get X != O
By point_on_circle on Y, w we get Y != O
By point_on_circle on I, w we get I != O
We have proved kite(I, Y, O, X)
We introduce Line(I, O)
By kite_properties_v0 I, Y, O, X we get Line(I, O) == perpendicular_bisector(X, Y)
We have proved X == line_reflection(Y, Line(I, O))
#_
# show that T == line_reflection(Z, Line(I, O))
By two_points_on_circle on T, Z, w we get distance(T, O) == distance(Z, O)
By point_on_circle on T, w we get T != O
By point_on_circle on Z, w we get Z != O
By point_on_circle on I, w we get I != O
We have proved kite(I, Z, O, T)
By kite_properties_v0 I, Z, O, T we get Line(I, O) == perpendicular_bisector(T, Z)
We have proved T == line_reflection(Z, Line(I, O))
#_
# show XT == YZ
By line_reflection_preseve_distance on X, T, Y, Z, Line(I, O) we get distance(X, T) == distance(Y, Z)
#_

# show that IPX ISY are congruent
## big angle equality
By tangent_def_v0 on P, Line(A, B), c we get perpendicular(Line(A, B), Line(I, P))
It is almost always true that X != P
By Line_definition on X, P, Line(A, B) we get Line(A, B) == Line(X, P)
We have proved angle(I, P, X) == 90 mod 180
By tangent_def_v0 on S, Line(A, D), c we get perpendicular(Line(A, D), Line(I, S))
It is almost always true that Y != S
By Line_definition on Y, S, Line(A, D) we get Line(A, D) == Line(Y, S)
We have proved angle(I, S, Y) == 90 mod 180
## sides equality
By two_points_on_circle on S, P, c we get distance(I, P) == distance(I, S)
We have proved distance(I, X) == distance(I, Y)
##_
By triangle_sufficient_conditions_v1 on P, I, X we get triangle(I, P, X)
By triangle_sufficient_conditions_v1 on S, I, Y we get triangle(I, S, Y)
By right_triangles_congruence_no_orientation_v2 on I, P, X, I, S, Y we get distance(X, P) == distance(Y, S)
#_
# show that IRT IQZ are congruent
## big angle equality
By tangent_def_v0 on R, Line(D, C), c we get perpendicular(Line(D, C), Line(I, R))
It is almost always true that T != R
By Line_definition on T, R, Line(D, C) we get Line(D, C) == Line(T, R)
We have proved angle(I, R, T) == 90 mod 180
By tangent_def_v0 on Q, Line(B, C), c we get perpendicular(Line(B, C), Line(I, Q))
It is almost always true that Z != Q
By Line_definition on Z, Q, Line(B, C) we get Line(B, C) == Line(Z, Q)
We have proved angle(I, Q, Z) == 90 mod 180
## sides equality
By two_points_on_circle on Q, R, c we get distance(I, R) == distance(I, Q)
We have proved distance(I, T) == distance(I, Z)
##_
By triangle_sufficient_conditions_v1 on R, I, T we get triangle(I, R, T)
By triangle_sufficient_conditions_v1 on Q, I, Z we get triangle(I, Q, Z)
By right_triangles_congruence_no_orientation_v2 on I, R, T, I, Q, Z we get distance(T, R) == distance(Z, Q)
#_
# finish
By two_tangents_distances on A, S, P, c we get distance(A, S) == distance(A, P)
By two_tangents_distances on C, R, Q, c we get distance(C, R) == distance(C, Q)
By two_tangents_distances on D, S, R, c we get distance(D, S) == distance(D, R)
#By length_sum_v0 on A, S, D we get distance(A, D) == ditance(A, S) + distance()
We have proved distance(A, D) == distance(A, S) + distance(S, D)
We have proved distance(A, D) + distance(D, T) + distance(T, X) + distance(X, A) == distance(A, S) + distance(S, D) + distance(D, T) + distance(T, X) + distance(X, A)
#We have proved distance(A, S) + distance(S, D) + distance(D, T) + distance(T, X) + distance(X, A) == 
By inner_transitivity_of_between X, A, P, B we get between(P, A, X) # the betweens add distances equations 
By inner_transitivity_of_between T, D, R, C we get between(T, D, R)
By inner_transitivity_of_between Z, C, Q, B we get between(Z, C, Q)
By inner_transitivity_of_between Y, D, S, A we get between(Y, D, S)
#_
