Assumptions:
# free objects
A, B, C, D, P, Q, R: Point
distinct(A, B, C, D, P, Q, R)


# constructed objects
Q == line_circle_other_intersection(D, Line(P, D), Circle(A, C, D))
R == line_circle_other_intersection(P, Line(P, C), Circle(A, P, Q))


#assumptions
parallelogram(A, B, C, D)
distance(A, C) == distance(B, C)
between(A, B, P)
collinear(A, B, P) # it stupid that between not imply collinear


#distinct

#collinear
collinear(A, B, P)
collinear(D, Q, P)
collinear(C, R, P)


exists(Line(A, R))
exists(Line(C, Q))
exists(Line(R, Q))
#exists(Line(A, Q))
#exists(Line(C, R))
Need to prove:
concurrent(Line(C, D), Line(A, Q), Line(B, R))

Proof:
We have proved Line(C, R) == Line(C, P)

We have proved distance(A, C) == distance(B, C)
We have proved distance(B, C) == distance(A, D)
By isosceles_angles_segments_v0 on C, B, A we get angle(C, B, A) == angle(B, A, C)
By isosceles_angles_segments_v0 on A, C, D we get angle(A, C, D) == angle(C, D, A)
We have proved parallel(Line(D, C), Line(A, B))
We have proved angle(B, A, C) == angle(D, C, A) mod 180 # maybe mod 180 won't be enough
We introduce Line(A, R)
By complementary_angles_180_v0 on A, C, R, P we get angle(C, R, A) + angle(A, R, P) == 0 mod 180
By angles_on_chord on  A, P, R, Q, Circle(A, P, Q) we get angle(A, R, P) == angle(A, Q, P) mod 180
By complementary_angles_180_v0 on A, P, Q, D we get angle(P, Q, A) + angle(A, Q, D) == 0 mod 180
By angles_on_chord on  D, A, C, Q, Circle(A, D, C) we get angle(D, C, A) == angle(D, Q, A) mod 180
We have proved angle(C, R, A) == angle(C, B, A) mod 180
It is almost always true that triangle(A, C, R)
By four_points_concyclic_sufficient_conditions_v0 C, R, A, B we get concyclic(C, R, A, B)
Let gamma := Circle(C, R, A)
# solution 1
It is almost always true that line_angle(Line(A, Q)) != line_angle(Line(C, D)) mod 180
Let X := line_intersection(Line(A, Q), Line(C, D))
It is almost always true that X != C
It is almost always true that X != D
It is almost always true that X != Q
It is almost always true that X != R
It is almost always true that X != B
It is almost always true that X != A
# By collinear_sufficient_conditions_v0 on X, C, D we get collinear(X, C, D)
# By collinear_sufficient_conditions_v0 on X, A, Q we get collinear(X, A, Q)
# prove that B, R, X are collinear
We introduce Line(Q, R)
By complementary_angles_180_v0 on R, A, Q, X we get angle(A, Q, R) + angle(R, Q, X) == 0 mod 180
By angles_on_chord on  A, R, P, Q, Circle(A, P, Q) we get angle(A, P, R) == angle(A, Q, R) mod 180
We have proved angle(R, Q, X) == angle(R, P, A) mod 180
We have proved angle(R, C, X) == angle(R, P, A) mod 180

We have proved angle(R, P, A) == angle(R, C, X) mod 180
It is almost always true that triangle(Q, R, X)
By four_points_concyclic_sufficient_conditions_v0 R, Q, X, C we get concyclic(R, Q, X, C)
Let delta := Circle(R, Q, X)
# final angle chasing
By angles_on_chord on  X, C, R, Q, delta we get angle(X, R, C) == angle(X, Q, C) mod 180
We introduce Line(C, Q)
By complementary_angles_180_v0 on C, X, Q, A we get angle(X, Q, C) + angle(C, Q, A) == 0 mod 180
By angles_on_chord on  C, A, Q, D, Circle(A, D, C) we get angle(C, Q, A) == angle(C, D, A) mod 180
We have proved angle(A, D, C) == angle(B, A, C) mod 180
By angles_on_chord on  C, B, R, A, gamma we get angle(C, R, B) == angle(C, A, B) mod 180
We have proved angle(X, R, C) + angle(C, R, B) == 0 mod 180
# collinear implication
By complementary_angles_180_v1 on C, X, R, B we get collinear(X, R, B)
# from collinear to concurrent
By line_intersection_definition on X, Line(R, B), Line(A, Q) we get X == line_intersection(Line(R, B), Line(A, Q))
It is almost always true that distinct(Line(R, B), Line(A, Q), Line(D, C))
By concurrent_sufficient_conditions_v0 on Line(R, B), Line(A, Q), Line(D, C) we get concurrent(Line(R, B), Line(A, Q), Line(D, C))