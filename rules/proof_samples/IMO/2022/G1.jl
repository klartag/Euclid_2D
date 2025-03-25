Assumptions:
A, B, C, D, E, T, P, Q, R, S: Point

distinct(A, B, C, D, E, T, P, Q, R, S)  # I might have gone overboard.

# All of these should be replaced with the appropriate convexity theorems.
T not in Line(A, B)
T not in Line(B, C)
T not in Line(C, D)
T not in Line(D, E)
T not in Line(E, A)

orientation(A, B, T) == orientation(B, C, T)
orientation(A, B, T) == orientation(C, D, T)
orientation(A, B, T) == orientation(D, E, T)
orientation(A, B, T) == orientation(E, A, T)

distance(B, C) == distance(D, E)
distance(T, B) == distance(T, D)
distance(T, C) == distance(T, E)
angle(A, B, T) == angle(T, E, A) mod 360

P == line_intersection(Line(A, B), Line(C, D))
Q == line_intersection(Line(A, B), Line(C, T))

R == line_intersection(Line(A, E), Line(C, D))
S == line_intersection(Line(A, E), Line(D, T))

between(P, B, A, Q)
between(R, E, A, S)

Need to prove:
concyclic(R, Q, S, P)

Proof:
We have proved collinear(D, C, P)
By segment_segment_segment_congruence on C, T, B, E, T, D we get angle(C, T, B) == angle(E, T, D)
By same_angle_v2 on T, E, A, S we get angle(T, E, A) == angle(T, E, S) mod 360
By same_angle_v2 on T, B, A, Q we get angle(T, B, A) == angle(T, B, Q) mod 360
By complementary_angles_180_v0 on E, D, T, S we get angle(D, T, E) + angle(E, T, S) == 0 mod 180
By complementary_angles_180_v0 on B, C, T, Q we get angle(C, T, B) + angle(B, T, Q) == 0 mod 180
We have proved Line(A, B) == Line(B, Q)
By triangle_def on B, Q, T we get triangle(B, Q, T)
By triangle_def on S, E, T we get triangle(S, E, T)
By similar_triangles_v3 on Q, B, T, S, E, T we get distance(Q, B) / distance(S, E) == distance(B, T) / distance(E, T), distance(Q, B) / distance(S, E) == distance(T, Q) / distance(T, S), angle(T, Q, B) + angle(T, S, E) == 0 mod 360
By distance_nonzero_v1 on T, B we get distance(T, B) != 0
By distance_nonzero_v1 on T, C we get distance(T, C) != 0
By distance_nonzero_v1 on T, D we get distance(T, D) != 0
By distance_nonzero_v1 on T, E we get distance(T, E) != 0
By scalar_log on distance(C, T), distance(E, T) we get log(distance(C, T)) == log(distance(E, T))
By scalar_log on distance(B, T), distance(D, T) we get log(distance(B, T)) == log(distance(D, T))
It is almost always true that triangle(C, D, Q)

By power_of_a_point_concyclic_condition_v0 on T, C, Q, D, S we get concyclic(C, D, Q, S)
Let c1 := Circle(C, D, Q)

By angles_on_chord on C, D, Q, S, c1 we get angle(C, Q, D) == angle(C, S, D) mod 180
By angles_on_chord on Q, D, C, S, c1 we get angle(Q, C, D) == angle(Q, S, D) mod 180
By triangle_angles_360 on C, P, Q we get angle(C, P, Q) + angle(P, Q, C) + angle(Q, C, P) == 180 mod 360
By complementary_angles_180_v0 on Q, D, C, P we get angle(D, C, Q) + angle(Q, C, P) == 0 mod 180
By same_angle_v0 on Q, P, C, R we get angle(Q, P, C) == angle(Q, P, R) mod 180
By same_angle_v0 on T, Q, B, P we get angle(T, Q, B) == angle(T, Q, P) mod 180
By same_angle_v0 on P, Q, T, C we get angle(P, Q, T) == angle(P, Q, C) mod 180
By triangle_angles_360 on T, Q, B we get angle(T, Q, B) + angle(Q, B, T) + angle(B, T, Q) == 180 mod 360
By triangle_angles_360 on P, Q, C we get angle(P, Q, C) + angle(Q, C, P) + angle(C, P, Q) == 180 mod 360
We introduce Line(D, Q)
By angle_sum on Q, D, C, P we get angle(D, Q, C) + angle(C, Q, P) == angle(D, Q, P) mod 360
By same_angle_v0 on T, S, E, R we get angle(T, S, E) == angle(T, S, R) mod 180
By same_angle_v0 on R, S, T, D we get angle(R, S, T) == angle(R, S, D) mod 180
We introduce Line(S, Q)
By angle_sum on S, D, R, Q we get angle(D, S, R) + angle(R, S, Q) == angle(D, S, Q) mod 360
It is almost always true that angle(R, S, Q) != 0 mod 180
It is almost always true that triangle(R, S, Q)
By four_points_concyclic_sufficient_conditions_v0 on R, S, Q, P we get concyclic(R, Q, S, P)