Assumptions:
A, B, C, D, P, Q: Point
phi, psi: Angle
abs_phi, abs_psi : Scalar
distinct(A, B, C, D, P, Q)
convex(A, B, C, D)
# P inside ABCD
identical(orientation(A, B, C), orientation(A, B, P), orientation(B, C, P), orientation(C, D, P), orientation(D, A, P))

phi == angle(P, A, D)
psi == angle(C, B, P)

abs_phi == abs_angle(P, A, D)
abs_psi == abs_angle(C, B, P)

angle(P, B, A) == 2 * phi
angle(D, P, A) == 3 * phi
angle(B, A, P) == 2 * psi
angle(B, P, C) == 3 * psi
# don't it the follwing can be implied from the above
abs_angle(P, B, A) == 2 * abs_phi
abs_angle(D, P, A) == 3 * abs_phi
abs_angle(B, A, P) == 2 * abs_psi
abs_angle(B, P, C) == 3 * abs_psi

smaller(abs_phi, abs_angle(D, P, A))
smaller(abs_psi, abs_angle(B, P, C))


Q == line_intersection(internal_angle_bisector(A, D, P), internal_angle_bisector(P, C, B))
inside_triangle(Q, A, B, P)

Need to prove:
distance(A, Q) == distance(B, Q)

Proof:

#point_between_with_certain_angle




# show DP == DX
Let X := point_between_with_certain_angle(A, P, D, abs_phi)
It is almost always true that distinct(A, B, C, D, P, Q, X)
We have proved abs_angle(X, P, A) == abs_phi
We have proved between(A, X ,D)
By abs_angle_to_angle_v0 on X, P, A, P, A, D we get angle(X, P, A) == angle(P, A, D) 
We have proved angle(A, P, X) + angle(P, X, A) + angle(X, A, P) == 0 mod 180
By complementary_angles_180_v0 on P, A, X, D we get angle(A, X, P) + angle(P, X, D) == 0 mod 180
We have proved angle(P, X, D) == angle(X, P, A) + angle(P, A, X) mod 180
We have proved angle(P, X, D) == 2 * phi mod 180
By angle_sum on P, D, X, A we get angle(D, P, X) + angle(X, P, A) == angle(D, P, A) mod 360
We have proved angle(P, X, D) == angle(D, P, X) mod 180
It is almost always true that triangle(D, P, X)
By isosceles_angles_segments_v1 on D, P, X we get distance(D, P) == distance(D, X)
By isosceles_internal_angle_bisector on D, X, P we get internal_angle_bisector(X, D, P) == perpendicular_bisector(X, P)
#_
# show CP == CY
Let Y := point_between_with_certain_angle(B, P, C, abs_psi)
It is almost always true that distinct(A, B, C, D, P, Q, Y)
We have proved abs_angle(Y, P, B) == abs_psi
We have proved between(B, Y ,C)
By abs_angle_to_angle_v0 on B, P, Y, C, B, P we get angle(B, P, Y) == angle(C, B, P) 
We have proved angle(B, P, Y) + angle(P, Y, B) + angle(Y, B, P) == 0 mod 180
By complementary_angles_180_v0 on P, B, Y, C we get angle(B, Y, P) + angle(P, Y, C) == 0 mod 180
We have proved angle(P, Y, C) == angle(Y, P, B) + angle(P, B, Y) mod 180
We have proved angle(P, Y, C) == -2 * psi mod 180
By angle_sum on P, C, Y, B we get angle(C, P, Y) + angle(Y, P, B) == angle(C, P, B) mod 360
We have proved angle(P, Y, C) == angle(C, P, Y) mod 180
It is almost always true that triangle(C, P, Y)
By isosceles_angles_segments_v1 on C, P, Y we get distance(C, P) == distance(C, Y)
By isosceles_internal_angle_bisector on C, Y, P we get internal_angle_bisector(Y, C, P) == perpendicular_bisector(Y, P)
#_
# show concurrent(perpendicular_bisector(A, B), perpendicular_bisector(X, P), perpendicular_bisector(Y, P))
We have proved angle(A, X, P) + 2 * phi == 0 mod 180
We have proved angle(A, X, P) + angle(P, B, A) == 0 mod 180
By four_points_concyclic_sufficient_conditions_v0 on A, B, P, X we get concyclic(A, B, P, X)
We have proved angle(B, Y, P) - 2 * psi == 0 mod 180
We have proved angle(B, Y, P) + angle(P, A, B) == 0 mod 180
It is almost always true that triangle(A, B, Y)
By four_points_concyclic_sufficient_conditions_v0 on A, B, Y, P we get concyclic(A, B, Y, P)
By chord_which_is_symmetry_axis_is_diameter_v0_r on A, B, perpendicular_bisector(A, B), Circle(A, B, P) we get center(Circle(A, B, P)) in perpendicular_bisector(A, B)
By chord_which_is_symmetry_axis_is_diameter_v0_r on X, P, perpendicular_bisector(X, P), Circle(A, B, P) we get center(Circle(A, B, P)) in perpendicular_bisector(X, P)
By chord_which_is_symmetry_axis_is_diameter_v0_r on Y, P, perpendicular_bisector(Y, P), Circle(A, B, P) we get center(Circle(A, B, P)) in perpendicular_bisector(Y, P)
It is almost always true that line_angle(perpendicular_bisector(X, P)) != line_angle(perpendicular_bisector(Y, P)) mod 180
By line_intersection_definition on center(Circle(A, B, P)), perpendicular_bisector(X, P),  perpendicular_bisector(Y, P) we get center(Circle(A, B, P)) == line_intersection(perpendicular_bisector(X, P), perpendicular_bisector(Y, P))

By angle_bisectors_on_same_line on P, D, X, A we get internal_angle_bisector(P, D, X) == internal_angle_bisector(P, D, A)
By angle_bisectors_on_same_line on P, C, Y, B we get internal_angle_bisector(P, C, Y) == internal_angle_bisector(P, C, B) 

We have proved center(Circle(A, B, P)) == line_intersection(internal_angle_bisector(A, D, P), internal_angle_bisector(P, C, B))
#We have proved Q == center(Circle(A, B, P))
#We have proved Q in perpendicular_bisector(A, B)
# #By perpendicular_bisector_equi_distance

