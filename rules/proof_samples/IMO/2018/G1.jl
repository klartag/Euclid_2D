Assumptions:
A, B, C, D, E, F, G: Point
Gamma: Circle
distinct(A, B, C, D, E, F, G)
triangle(A, B, C)
Gamma == Circle(A, B, C)
between(A, D, B)
between(A, E, C)
distance(A, E) == distance(A, D)
F in perpendicular_bisector(B, D), Gamma
G in perpendicular_bisector(C, E), Gamma

Need to prove:
parallel(Line(F, G), Line(D, E))

Proof:
It is almost always true that line_angle(Line(A, B)) != line_angle(Line(F, G)) mod 180
It is almost always true that line_angle(Line(A, C)) != line_angle(Line(F, G)) mod 180
Let Z := line_intersection(Line(A, B), Line(F, G))
Let T := line_intersection(Line(A, C), Line(F, G))
It is almost always true that not_collinear(A, D, F)
Let X := parallelogram_point(A, D, F)
It is almost always true that distinct(A, B, C, D, E, F, G, Z, T, X)
We have proved angle(F, X, A) == angle(A, D, F) #mod 180
By complementary_angles_180_v0 on F, A, D, B we get angle(A, D, F) + angle(F, D, B) == 0 mod 180
By perpendicular_bisector_equi_distance_v0_r on B, D, F we get distance(F, B) == distance(F, D)
It is almost always true that not_collinear(F, D, B)
By isosceles_angles_segments_v0 on F, D, B we get angle(F, D, B) == angle(D, B, F)
By four_points_concyclic_sufficient_conditions_v0 on F, X, A, B we get concyclic(F, X, A, B)
We have proved X in Gamma

It is almost always true that not_collinear(A, E, G)
Let Y := parallelogram_point(A, E, G)
It is almost always true that distinct(A, B, C, D, E, F, G, Z, T, X, Y)
We have proved angle(G, Y, A) == angle(A, E, G) #mod 180
By complementary_angles_180_v0 on G, A, E, C we get angle(A, E, G) + angle(G, E, C) == 0 mod 180
By perpendicular_bisector_equi_distance_v0_r on C, E, G we get distance(G, C) == distance(G, E)
It is almost always true that not_collinear(G, E, C)
By isosceles_angles_segments_v0 on G, E, C we get angle(G, E, C) == angle(E, C, G)
By four_points_concyclic_sufficient_conditions_v0 on G, Y, A, C we get concyclic(G, Y, A, C)
We have proved Y in Gamma
We have proved distance(X, F) == distance(Y, G)
By isosceles_trapezoid_sufficient_conditions on X, Y, G, F we get isosceles_trapezoid(X, Y, G, F)
We have proved angle(A, T, Z) == angle(T, Z, A) mod 180
#We have proved angle(A, T, Z) == angle(G, F, X) mod 180
It is almost always true that not_collinear(A, D, E)
By isosceles_angles_segments_v0 on A, E, D we get angle(A, E, D) == angle(E, D, A)


It is almost always true that triangle(A, E, D)
It is almost always true that triangle(A, T, Z)
We have proved angle(A, D, E) + angle(D, E, A) + angle(E, A, D) == 180 mod 360
We have proved angle(A, T, Z) + angle(T, Z, A) + angle(Z, A, T) == 180 mod 360
We have proved angle(E, A, D) == angle(T, A, Z) mod 180
We have proved angle(A, E, D) == angle(A, T, Z) mod 180
