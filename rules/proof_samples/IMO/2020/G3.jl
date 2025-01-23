Assumptions:
A, B, C, D, E, F, L, K: Point
distinct(A, B, C, D, E, F, L, K)
convex(A, B, C, D)
angle(D, A, B) == angle(B, C, D)
E == line_reflection(A, Line(B, C))
F == line_reflection(A, Line(C, D))
K == line_intersection(Line(A, E), Line(B, D))
between(A, K, E)
L == line_intersection(Line(A, F), Line(B, D))
between(A, L, F)

Need to prove:
tangent(Circle(B, E, K), Circle(D, F, L))

Proof:

By line_reflection_is_involution on A, E, Line(B, C) we get A == line_reflection(E, Line(B, C))
By line_reflection_is_involution on A, F, Line(D, C) we get A == line_reflection(F, Line(C, D))

Let A' := line_reflection(A, Line(B, D))
It is almost always true that distinct(A, B, C, D, E, F, L, K, A')

# show that concyclic(A', B, E, K)
Let K' := line_reflection(K, Line(B, C))
It is almost always true that distinct(A, B, C, D, E, F, L, K, K', A')
By reflection_of_three_points_through_line_v0 on A, K, E, E, K', A, Line(B, C) we get collinear(A, K', E)
By reflection_of_three_points_through_line on B, E, K, B, A, K', Line(B, C) we get angle(B, E, K) + angle(B, A, K') == 0
We have proved angle(B, E, K) + angle(B, A, K) == 0 mod 180
By reflection_of_three_points_through_line on B, A, K, B, A', K, Line(B, D) we get angle(B, A, K) + angle(B, A', K) == 0
We have proved angle(B, E, K) == angle(B, A', K) mod 180
It is almost always true that triangle(A', K, B)
By four_points_concyclic_sufficient_conditions_v0 on B, A', K, E we get concyclic(A', B, E, K)
#_

# show that concyclic(A', D, F, L)
Let L' := line_reflection(L, Line(D, C))
It is almost always true that distinct(A, B, C, D, E, F, L, K, L', A')

By reflection_of_three_points_through_line_v0 on A, L, F, F, L', A, Line(D, C) we get collinear(A, L', F)       
By reflection_of_three_points_through_line on D, F, L, D, A, L', Line(D, C) we get angle(D, F, L) + angle(D, A, L') == 0
We have proved angle(D, F, L) + angle(D, A, L) == 0 mod 180
By reflection_of_three_points_through_line on D, A, L, D, A', L, Line(B, D) we get angle(D, A, L) + angle(D, A', L) == 0
We have proved angle(D, F, L) == angle(D, A', L) mod 180
It is almost always true that triangle(A', L, D)
By four_points_concyclic_sufficient_conditions_v0 on D, A', L, F we get concyclic(A', D, F, L)
#_
#We have proved triangle(A', K, L)
#It is almost always true that triangle(A', K, L)
We have proved angle(A', K, L) + angle(K, L, A') + angle(L, A', K) == 0 mod 180
By reflection_of_three_points_through_line on K, A, L, K, A', L, Line(B, D) we get angle(K, A, L) + angle(K, A', L) == 0
We have proved angle(A', K, L) + angle(K, L, A') + angle(K, A, L) == 0 mod 180
Let C_AL := projection(C, Line(A, L))
Let C_AK := projection(C, Line(A, K))
It is almost always true that distinct(C, C_AL, A, C_AK, K, L)
By four_points_angles on C,  C_AL,  A, C_AK we get angle(C, C_AL, A) + angle(C_AL, A, C_AK) + angle(A, C_AK, C) + angle(C_AK, C, C_AL) == 0 mod 360
We have proved angle(C_AL, A, C_AK) == angle(L, A, K) mod 180
We have proved angle(B, C ,D) == angle(C_AK, A, C_AL) mod 180
We have proved angle(B, C ,D) + angle(L, A, K) == 0 mod 180
By reflection_of_three_points_through_line on B, A, D, B, A', D, Line(B, D) we get angle(B, A, D) + angle(B, A', D) == 0
We have proved angle(A', K, B) + angle(D, L, A') == angle(D, A', B) mod 180
It is almost always true that center(Circle(B, E, K)) != center(Circle(D, F, L))
By two_tangent_circles_angles_on_chord_v0 on B, K, A', L, D, Circle(B, E, K), Circle(D, F, L) we get tangent(Circle(B, E, K), Circle(D, F, L))


#We have proved angle(A, B, C) + angle(B, C, D) + angle(C, D, A) + angle(D, A, B) == 0 mod 360

