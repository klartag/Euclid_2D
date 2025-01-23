Assumptions:
# free objects
A, B, C, D, P, Q, E, F: Point
l: Line
omega: Circle
distinct(A,B,C,D,P,Q,E,F)
isosceles_triangle(C, A, B)
between(A,D,midpoint(A,B))
between(B,P,C)
perpendicular(Line(D,P), Line(P,B))
between(A,Q,C)
perpendicular(Line(D,Q), Line(Q,C))
l == perpendicular_bisector(P,Q)
E in l 
between(C, E, Q)
omega == Circle(C, P, Q)
F in omega
F in Circle(A,B,C)
collinear(F,E,P)
Need to prove:
perpendicular(Line(A,C), Line(B,C))


Proof:
We have proved angle(Q,C,P) + angle(P,D,Q) == 0 mod 180
By four_points_concyclic_sufficient_conditions_v0 on Q,C,P,D we get concyclic(Q,C,P,D)
We have proved D in omega
We have proved center(omega) == circumcenter(C,Q,D)
By circumcenter_and_right_triangle_v0 on C, Q, D we get circumcenter(C,Q,D) in Line(C,D)
We have proved Q == line_reflection(P, l)
By chord_which_is_symmetry_axis_is_diameter_v0_r on P, Q, l, omega we get center(omega) in l
It is almost always true that F not in l
It is almost always true that distinct(Q, line_reflection(F, l), F, E)

By reflection_of_three_points_through_line_v0 on P, E, F, Q, E, line_reflection(F, l), l we get collinear(Q, E, line_reflection(F, l))
By chord_which_is_symmetry_axis_is_diameter_v0 on F, line_reflection(F, l), l, omega we get line_reflection(F, l) in omega

By circle_line_at_most_two_intersections on line_reflection(F, l), C, Q, Line(E, Q), omega we get C == line_reflection(F, l)
By chord_which_is_symmetry_axis_is_diameter_v0_r F, C, l, Circle(A, B, C) we get center(Circle(A, B, C)) in l
Let O := center(Circle(A, B, C))
It is almost always true that distinct(A, B, C, D, P, Q, E, F, O)
We have proved O in l
#We have proved perpendicular(l, Line(C, F))
#By perpendicular_bisector_definition_1 on C, F, l we get l == perpendicular_bisector(C, F)
By isosceles_internal_angle_bisector on C, A, B we get identical(internal_angle_bisector(B, C, A), median(C, B, A), altitude(C, B, A), perpendicular_bisector(B, A))
Let M := midpoint(A, B)
It is almost always true that distinct(M, A, B, C, P, Q)
We have proved Line(C, M) == altitude(C,A,B)
It is almost always true that triangle(D, M, C)
By Line_definition on M, A, Line(A, B) we get Line(A, B) == Line(A, M)
By Line_definition on M, D, Line(A, B) we get Line(A, B) == Line(M, D)
By right_angle_on_diameter_v0 on C, M, D, omega we get M in omega
By chords_on_equi_angles_v0 on P, C, M, M, C, Q, omega we get distance(M,P) == distance(M, Q)
By perpendicular_bisector_equi_distance_v0 on P, Q, M we get M in l
By perpendicular_bisector_definition_1 on A, B, Line(C, M) we get Line(C, M) == perpendicular_bisector(A, B)
By chord_which_is_symmetry_axis_is_diameter_v0_r A, B, Line(C, M), Circle(A, B, C) we get O in Line(C, M)
It is almost always true that Line(C, M) != l
By line_unique_intersection_v0 on l, Line(C, M), M , O we get O == M
By circumcenter_and_right_triangle_v0_r on A, C, B we get right_triangle(A, C, B)

