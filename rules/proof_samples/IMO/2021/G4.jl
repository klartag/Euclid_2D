Assumptions:
A, B, C, D, E, F, T, K: Point
l: Line
omega: Circle


quadrilateral(A, B, C, D)
tangent(l, omega)
D in l
inside_triangle(T, A, B, C)
parallel(Line(E, T), Line(D, C))
parallel(Line(F, T), Line(D, A))
distance(T, D) == distance(T, K)

#distinct
distinct(A, B, C, D, E, F, T, K)

#quadrilateral incribes in omega
A, B, C, D in omega

#constructed objects
E == line_intersection(l, Line(A, B))
F == line_intersection(l, Line(B, C))

# collinear
# we should implement collinear of arbitrary lengeth.
collinear(E, D, K)
collinear(E, D, F)
collinear(E, K, F)
between(D, K, F) 
#_
collinear(B, A, E)
collinear(B, C, F)
l == Line(E, F)


# Unchecked.

Need to prove:
concurrent(Line(A, C), Line(D, T), Line(B, K))

Proof:
By inscribed_quadrilateral_and_tangent on A, B, C, D, T, l, omega we get convex(A, B, C, D)
Let Q := line_intersection(Line(T, F), Line(A, C))
Let P := line_intersection(Line(T, E), Line(A, C))
It is almost always true that distinct(A, B, C, D, E, F, T, K, Q, P) # I add that the new points are different from all the other points
# show that E, P, A, D concyclic
We introduce Line(D, P)
We introduce Line(D, Q)

By Line_definition on A, P, Line(A, C) we get Line(A, C) == Line(A, P)
By Line_definition on E, P, Line(E, T) we get Line(E, T) == Line(E, P)
We have proved angle(E, P, A) == angle(D, C, A) mod 180
By tangent_angle_180_v0 on D, C, A, Line(D, E), omega we get angle(D, C, A) == line_angle(Line(D, A)) - line_angle(Line(D, E)) mod 180
We have proved angle(E, P, A) == angle(E, D, A) mod 180
It is almost always true that triangle(E, P, A)
By four_points_concyclic_sufficient_conditions_v0 on E, P, A, D we get concyclic(E, P, A, D)
Let alpha := Circle(E, P, A)
#_
# show that F, Q, C, D concyclic
By Line_definition on C, Q, Line(A, C) we get Line(A, C) == Line(C, Q)
By Line_definition on F, Q, Line(F, T) we get Line(F, T) == Line(F, Q)
We have proved angle(F, Q, C) == angle(D, A, C) mod 180
By tangent_angle_180_v0 on D, A, C, Line(D, F), omega we get angle(D, A, C) == line_angle(Line(D, C)) - line_angle(Line(D, F)) mod 180
We have proved angle(F, Q, C) == angle(F, D, C) mod 180
It is almost always true that triangle(F, Q, C)
By four_points_concyclic_sufficient_conditions_v0 on F, Q, C, D we get concyclic(F, Q, C, D)
Let gamma := Circle(F, Q, C)
#_
By complementary_angles_180_v0 on D, E, A, B we get angle(E, A, D) + angle(D, A, B) == 0 mod 180
By angles_on_chord on B, D, A, C, omega  we get angle(B, A, D) == angle(B, C, D) mod 180
By complementary_angles_180_v0 on D, F, C, B we get angle(F, C, D) + angle(D, C, B) == 0 mod 180
We have proved collinear(E, D, F)
It is almost always true that alpha != gamma
By two_tangent_circles_angles_on_chord_v0 E, A, D, C, F, alpha, gamma we get tangent(alpha, gamma)
# prove that T in radical_axis(alpha, omega)
## prove the wanted betweens
By Circle_definition on A, B, C, omega we get omega == Circle(A, B, C)
By triangle_circle_in_out_transitivity_v0 on T, A, B, C we get inside_circle(T, omega)
By inscribed_convex_quadrilateral_and_tangent_v0 on A, B, C, D, T, l, omega we get between(B, A, E)
By inscribed_convex_quadrilateral_and_tangent_v1 on A, B, C, D, T, l, omega we get between(B, C, F)
By triangle_and_point_iside_imply_between A, B, C, T, E we get between(T, P, E)
By triangle_and_point_iside_imply_between C, B, A, T, F we get between(T, Q, F)
##_
## prove concyclic(E, P, Q, F)
We have proved angle(Q, F, E) == angle(A, D, E) mod 180
We have proved angle(Q, F, E) == angle(A, P, E) mod 180
By complementary_angles_180_v0 E, A, P, Q we get angle(A, P, E) + angle(E, P, Q) == 0 mod 180
It is almost always true that triangle(E, P, Q)
By four_points_concyclic_sufficient_conditions_v0 on E, P, Q, F we get concyclic(E, P, Q, F)
##_
By between_imply_not_between on T, P, E we get collinear_and_not_between(E, T, P)
By between_imply_not_between on T, Q, F we get collinear_and_not_between(F, T, Q)
By power_of_a_point_concyclic_condition_v1_r on T, P, E, Q, F we get log(distance(T, P)) + log(distance(T, E)) == log(distance(T, Q)) + log(distance(T, F))
It is almost always true that center(alpha) != center(gamma)
By between_imply_not_between on T, P, E we get collinear_and_not_between(P, T, E)
By between_imply_not_between on T, Q, F we get collinear_and_not_between(Q, T, F)
By equal_power_on_radical_v0 on T, P, E, Q, F, alpha, gamma we get T in radical_axis(alpha, gamma)
By intersection_on_radical on D, alpha, gamma we get D in radical_axis(alpha, gamma)
By Line_definition on D, T, radical_axis(alpha, gamma) we get radical_axis(alpha, gamma) == Line(T, D)
By different_centers_imply_different_circles on alpha, gamma we get alpha != gamma
By radical_axis_of_tangent_circles_v1 on D, Line(T, D), alpha, gamma we get tangent(Line(T, D), alpha), tangent(Line(T, D), gamma)
#_
It is almost always true that triangle(T, D, K)
By isosceles_angles_segments_v0 on T, D, K we get angle(T, D, K) == angle(D, K, T)
By tangent_angle_180_v0 on D, A, E, Line(T, D), alpha we get angle(D, A, E) == line_angle(Line(D, E)) - line_angle(Line(T, D)) mod 180
We have proved angle(D, A, E) == angle(T, D, K) mod 180
We introduce Line(B, D)
By tangent_angle_180_v0 on D, A, B, Line(K, D), omega we get angle(D, A, B) == line_angle(Line(B, D)) - line_angle(Line(K, D)) mod 180
We have proved angle(B, D, E) == angle(E, A, D) mod 180
We have proved parallel(Line(T, K), Line(B, D))
# show that P, T, Q, K, D are concyclic
## concyclic(T, K, D, P)
By tangent_angle_180_v0 on D, P, E, Line(T, D), alpha we get angle(D, P, E) == line_angle(Line(E, D)) - line_angle(Line(T, D)) mod 180
We have proved angle(E, P, D) == angle(F, D, T) mod 180
We have proved angle(E, P, D) == angle(K, D, T) mod 180
By complementary_angles_180_v0 D, T, P, E we get angle(T, P, D) + angle(D, P, E) == 0 mod 180
We have proved angle(T, K, D) + angle(D, P, T) == 0 mod 180
By four_points_concyclic_sufficient_conditions_v0 T, K, D, P we get concyclic(T, K, D, P)
##_
## concyclic(T, K, D, Q)
By tangent_angle_180_v0 on D, Q, F, Line(T, D), gamma we get angle(D, Q, F) == line_angle(Line(F, D)) - line_angle(Line(T, D)) mod 180
We have proved angle(F, Q, D) == angle(F, D, T) mod 180
We have proved angle(F, Q, D) == angle(K, D, T) mod 180
By complementary_angles_180_v0 D, T, Q, F we get angle(T, Q, D) + angle(D, Q, F) == 0 mod 180
We have proved angle(T, K, D) + angle(D, Q, T) == 0 mod 180
By four_points_concyclic_sufficient_conditions_v0 T, K, D, Q we get concyclic(T, K, D, Q)
##_
Let tau := Circle(T, D, K)
#_
# prove that PK and BC are parallel
By angles_on_chord on P, D, K, Q, tau we get angle(P, K, D) == angle(P, Q, D) mod 180
By angles_on_chord on D, C, F, Q, gamma we get angle(D, F, C) == angle(D, Q, C) mod 180
By Line_definition on P, Q, Line(A, C) we get Line(A, C) == Line(P, Q) 
By complementary_angles_180_v0 on D, P, Q, C we get angle(P, Q, D) + angle(D, Q, C) == 0 mod 180
We have proved angle(P, Q, D) == angle(C, F, D) mod 180
We have proved parallel(Line(P, K), Line(B, C))
#_
# make sure that homothety_six_points theorem will imply concurrent and not parallel
We have proved orientation(C, B, D) == orientation(D, B, A)
It is almost always true that not_collinear(B, D, E)
By between_imply_same_orientation on D, E, A, B we get orientation(D, A, B) == orientation(D, E, B)
It is almost always true that not_collinear(B, D, F)
By between_imply_same_orientation on D, F, C, B we get orientation(D, C, B) == orientation(D, F, B)
We have proved orientation(F, B, D) == orientation(D, B, E)
It is almost always true that triangle(E, B, F)
By inside_infinite_hourglass_imply_between on E, B, F, D we get between(E, D, F)
It is almost always true that triangle(E, F, T)
By three_betweens_on_triangle_imply_non_parallel on T, E, F, P, D, Q we get line_angle(Line(T, D)) != line_angle(Line(P, Q)) mod 180
#_
By Line_definition on P, C, Line(A, C) we get Line(A, C) == Line(P, C)
By Line_definition on P, Q, Line(P, C) we get Line(P, C) == Line(P, Q)

It is almost always true that distinct(Line(P, Q), Line(D, T), Line(B, K))

By homothety_six_points_v1 on T, P, K, D, C, B we get concurrent(Line(P, Q), Line(D, T), Line(B, K))
