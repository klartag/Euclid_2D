Assumptions:
A, B, C, D, P, Q, M, N: Point
c_abcd, c_adq, c_bcp: Circle
convex(A, B, C, D)
# TODO: Writing `convex` should automatically draw these lines.
exists(Line(A, B), Line(B, C), Line(C, D), Line(D, A))
distinct(A, B, C, D, P, Q, M, N)
between(Q, A, B, P)
A in c_abcd
B in c_abcd
C in c_abcd
D in c_abcd
A in c_adq
D in c_adq
Q in c_adq
B in c_bcp
C in c_bcp
P in c_bcp
tangent(Line(A, C), c_adq)
tangent(Line(B, D), c_bcp)
distance(B, M) == distance(M, C)
between(B, M, C)
distance(A, N) == distance(N, D)
between(A, N, D)

c_bpm: Circle
B in c_bpm
P in c_bpm
M in c_bpm

c_anq: Circle
A in c_anq
N in c_anq
Q in c_anq

ta: Line
ta == tangent_from_point_in_circle(A, c_anq)

tb: Line
tb == tangent_from_point_in_circle(B, c_bpm)

Need to prove:
concurrent(ta, tb, Line(C, D))

Proof:
# By convex_quad on A, B, C, D we get X, triangle(A, B, C), triangle(A, B, D), triangle(A, C, D), triangle(B, C, D)
By triangle_non_trivial on A, B, D we get D not in Line(A, B)
By triangle_non_trivial on A, B, C we get C not in Line(A, B)
By triangle_non_trivial on A, C, D we get A not in Line(C, D)
By triangle_non_trivial on B, C, D we get B not in Line(C, D)
By line_point_inequality on Line(A, C), Line(A, B), C we get Line(A, B) != Line(A, C)
By line_point_inequality on Line(A, D), Line(C, D), A we get Line(A, D) != Line(C, D)
By line_point_inequality on Line(B, D), Line(C, D), B we get Line(B, D) != Line(C, D)

By angles_on_chord on D, B, C, A, c_abcd we get angle(D, C, B) == angle(D, A, B) mod 180
By angles_on_chord on C, A, B, D, c_abcd we get angle(C, D, A) == angle(C, B, A) mod 180
By angles_on_chord on C, D, A, B, c_abcd we get angle(C, A, D) == angle(C, B, D) mod 180
By complementary_angles_360 on D, Q, A, B we get angle(Q, A, D) + angle(D, A, B) == 180 mod 360
By complementary_angles_360 on C, P, B, A we get angle(P, B, C) + angle(C, B, A) == 180 mod 360
By tangent_angle_180_v0 on A, Q, D, Line(A, C), c_adq we get angle(A, Q, D) == line_angle(Line(A, D)) - line_angle(Line(A, C)) mod 180
By tangent_angle_180_v0 on B, P, C, Line(B, D), c_bcp we get angle(B, P, C) == line_angle(Line(B, C)) - line_angle(Line(B, D)) mod 180
By same_angle_v2 on Q, A, N, D we get angle(Q, A, N) == angle(Q, A, D) mod 360
By same_angle_v2 on P, B, M, C we get angle(P, B, M) == angle(P, B, C) mod 360
By concyclic_to_triangle on D, A, Q, c_adq we get triangle(D, A, Q)
By concyclic_to_triangle on B, C, P, c_bcp we get triangle(B, C, P)
By similar_triangles_v0 on D, C, B, D, A, Q we get distance(D, C) / distance(D, A) == distance(C, B) / distance(A, Q), angle(A, Q, D) == angle(C, B, D) mod 360, angle(D, A, Q) == angle(D, C, B) mod 360
By similar_triangles_v0 on C, D, A, C, B, P we get distance(C, D) / distance(C, B) == distance(D, A) / distance(B, P), angle(B, P, C) == angle(D, A, C) mod 360, angle(C, B, P) == angle(C, D, A) mod 360
By length_sum_v0 on A, N, D we get distance(A, N) + distance(N, D) == distance(A, D)
By length_sum_v0 on B, M, C we get distance(B, M) + distance(M, C) == distance(B, C)

By distance_nonzero_v1 on A, D we get distance(A, D) != 0
By distance_nonzero_v1 on B, C we get distance(B, C) != 0
By distance_nonzero_v1 on C, D we get distance(C, D) != 0

By scalar_log on 2*distance(A, N), distance(A, D) we get log(2 * distance(A, N)) == log(distance(A, D))
By scalar_log on 2*distance(B, M), distance(B, C) we get log(2 * distance(B, M)) == log(distance(B, C))
Let R := midpoint(C, D)

By scalar_log on 2*distance(C, R), distance(C, D) we get log(2 * distance(C, R)) == log(distance(C, D))
By scalar_log on distance(C, R), distance(D, R) we get log(distance(C, R)) == log(distance(R, D))

# TODO: We shouldn't really need these "We introduce" lines for the conclusions immediately following them.
# Maybe we should separate `triangle_non_trivial` into some smaller theorems?
We introduce Line(D, Q)
We introduce Line(C, P)
By triangle_non_trivial on A, D, Q we get Q not in Line(A, D), Line(A, D) != Line(A, Q)
By triangle_non_trivial on B, C, P we get P not in Line(B, C), Line(B, C) != Line(B, P)

# By line_containment on R, B, Line(C, D) we get R != B
# By line_containment on R, A, Line(C, D) we get R != A
It is almost always true that distinct(R, A, B)
We have proved collinear(C, R, D)
By line_equality_v0 on A, N, D we get Line(A, D) == Line(A, N)
By line_equality_v0 on B, M, C we get Line(B, C) == Line(B, M)
By line_unique_intersection_v1 on Line(A, Q), Line(A, D), A, N we get N not in Line(A, Q)
By line_unique_intersection_v1 on Line(B, P), Line(B, C), B, M we get M not in Line(B, P)
By triangle_def on A, Q, N we get triangle(A, Q, N)
By triangle_def on B, P, M we get triangle(B, P, M)
By same_angle_v2 on Q, A, N, D we get angle(Q, A, N) == angle(Q, A, D) mod 360
By same_angle_v2 on P, B, M, C we get angle(P, B, M) == angle(P, B, C) mod 360
By same_angle_v2 on B, C, R, D we get angle(B, C, R) == angle(B, C, D) mod 360
By same_angle_v2 on A, D, R, C we get angle(A, D, R) == angle(A, D, C) mod 360
By similar_triangles_v1 on Q, A, N, B, C, R we get angle(A, N, Q) == angle(C, R, B) mod 360
By similar_triangles_v1 on P, B, M, A, D, R we get angle(B, M, P) == angle(D, R, A) mod 360

# Building K.

By on_convex on C, D, A, B, R we get R not in Line(A, B)
By triangle_def on A, B, R we get triangle(A, B, R)

Let c_abr := Circle(A, B, R)
It is almost always true that center(c_abr) not in Line(C, D)
Let K := line_circle_other_intersection(R, Line(C, D), c_abr)
It is almost always true that distinct(K, center(c_abr), R)
We introduce Line(K,center(c_abr))
Let Alt := midpoint(R, K)
It is almost always true that distinct(K, center(c_abr), R, Alt)
By two_points_on_circle on K, R, c_abr we get distance(K,center(c_abr)) == distance(R,center(c_abr))
By perpendicular_bisector_definition_2 on R, K, Alt, center(c_abr) we get Line(Alt,center(c_abr)) == perpendicular_bisector(K,R)
By Line_definition on K, R, Line(C, D) we get Line(C, D) == Line(K, R)
# By second_line_circle_intersection on Line(C, D), c_abr, R we get K, Alt, K in Line(C, D), K in c_abr, between(K, Alt, R), line_angle(Line(C, D)) - line_angle(Line(center(c_abr), Alt)) == 90 mod 180
If K == A:
    By line_unique_intersection_v0 on Line(A, D), Line(C, D), K, D we get K == D
    By point_equality_contradiction on K we get false()
We have proved K != A
If K == B:
    By line_unique_intersection_v0 on Line(B, D), Line(C, D), K, D we get K == D
    By point_equality_contradiction on K we get false()
We have proved K != B

# There are two cases: Either K==R and the line is tangent, or K != R and we use the angle on chord.
If K == R:
    By equal_is_between_r on K, Alt we get K == Alt
    By tangent_def_v0_r on K, Line(C, D), c_abr we get tangent(Line(C, D), c_abr)
    We introduce Line(B, K)
    We introduce Line(A, K)
    By tangent_angle_180_v0 on K, A, B, Line(C, D), c_abr we get angle(K, A, B) == line_angle(Line(K, B)) - line_angle(Line(C, D)) mod 180
    By tangent_angle_180_v0 on K, B, A, Line(C, D), c_abr we get angle(K, B, A) == line_angle(Line(K, A)) - line_angle(Line(C, D)) mod 180
    We have proved angle(K, A, B) == angle(C, R, B) mod 180
    We have proved angle(K, B, A) == angle(D, R, A) mod 180
Else if K != R:
    By angles_on_chord on K, B, A, R, c_abr we get angle(K, A, B) == angle(K, R, B) mod 180
    By angles_on_chord on K, A, B, R, c_abr we get angle(K, B, A) == angle(K, R, A) mod 180
    By line_equality_v0 on C, R, D we get Line(C, R) == Line(C, D), Line(D, R) == Line(C, R)
    By Line_definition on K, R, Line(C, D) we get Line(C, D) == Line(K, R)
    We have proved angle(K, A, B) == angle(C, R, B) mod 180
    We have proved angle(K, B, A) == angle(D, R, A) mod 180

We have proved angle(K, A, B) == angle(C, R, B) mod 180
We have proved angle(K, B, A) == angle(D, R, A) mod 180

By line_equality_v0 on Q, A, B we get Line(A, Q) == Line(A, B)
By line_equality_v0 on P, B, A we get Line(P, B) == Line(A, B)
By line_equality_v0 on A, N, D we get Line(A, N) == Line(A, D)
By line_equality_v0 on B, M, C we get Line(B, M) == Line(B, C)
We introduce Line(A, K)
We introduce Line(B, K)
By tangent_angle_180_v1 on A, N, Q, Line(A, K), c_anq we get tangent(Line(A, K), c_anq)
By tangent_angle_180_v1 on B, M, P, Line(B, K), c_bpm we get tangent(Line(B, K), c_bpm)
By tangent_unique on A, c_anq, ta, Line(A, K) we get ta == Line(A, K)
By tangent_unique on B, c_bpm, tb, Line(B, K) we get tb == Line(B, K)
By concyclic_to_triangle on A, C, D, c_abcd we get triangle(A, C, D)
By concyclic_to_triangle on B, C, D, c_abcd we get triangle(B, C, D)
By concyclic_to_triangle on A, B, K, c_abr we get triangle(A, B, K)
By line_point_inequality on ta, Line(C, D), A we get ta != Line(C, D)
By line_point_inequality on tb, Line(C, D), B we get tb != Line(C, D)
By line_point_inequality on ta, tb, A we get ta != tb
By line_intersection_definition on K, ta, tb we get K == line_intersection(ta, tb)
By line_intersection_definition on K, tb, Line(C, D) we get K == line_intersection(tb, Line(C, D))
By concurrent_sufficient_conditions_v0 on ta, tb, Line(C, D) we get concurrent(ta, tb, Line(C, D))
