Assumptions:
A, B, C, D, E, F, G, T: Point
l_F, l_G: Line
Gamma: Circle
distinct(A, B, C, D, E, F, G, T)
A in Gamma
F in Gamma
D == line_circle_other_intersection(A, Line(A, B), Gamma)
E == line_circle_other_intersection(A, Line(A, C), Gamma)
G == line_circle_other_intersection(F, Line(B, C), Gamma)
between(B, F, G)
l_F == point_circle_tangent_line(F, Circle(B, D, F))
l_G == point_circle_tangent_line(G, Circle(C, E, G))
T == line_intersection(l_F, l_G)

Need to prove:
parallel(Line(A, T), Line(B, C))

Proof:
By Line_definition on T, F, l_F we get l_F == Line(T, F)
By tangent_angle_180_v0 on F, D, B, l_F, Circle(B, D, F) we get angle(F, D, B) == line_angle(Line(B, F)) - line_angle(l_F) mod 180
We have proved angle(F, D, B) == angle(T, F, B) mod 180
We have proved angle(T, F, B) == angle(F, D, A) mod 180
By Circle_definition on A, D, F, Gamma we get Gamma == Circle(A, D, F)
By four_points_concyclic_sufficient_conditions_v1 on A, D, F, G we get concyclic(A, D, F, G)
We have proved angle(A, D, F) + angle(F, G, A) == 0 mod 180
By complementary_angles_180_v0 on A, F, G, C we get angle(F, G, A) + angle(A, G, C) == 0 mod 180
We have proved angle(F, D, A) == angle(C, G, A) mod 180

By Line_definition on T, G, l_G we get l_G == Line(T, G)
By tangent_angle_180_v0 on G, E, C, l_G, Circle(C, E, G) we get angle(G, E, C) == line_angle(Line(C, G)) - line_angle(l_G) mod 180
We have proved angle(T, G, B) == angle(G, E, C) mod 180
By Circle_definition on A, E, F, Gamma we get Gamma == Circle(A, E, F)
It is almost always true that triangle(A, E, F)
By four_points_concyclic_sufficient_conditions_v1 on A, E, F, G we get concyclic(A, E, F, G)
We have proved angle(G, F, A) + angle(A, E, G) == 0 mod 180
By complementary_angles_180_v0 on G, A, E, C we get angle(A, E, G) + angle(G, E, C) == 0 mod 180
We have proved angle(G, E, C) == angle(C, F, A) mod 180

We have proved angle(T, F, B) == angle(C, G, A) mod 180
We have proved angle(T, G, B) == angle(C, F, A) mod 180
It is almost always true that triangle(G, F, A)
It is almost always true that triangle(G, F, T)
By congruent_triangles_v3 on F, G, T, G, F, A we get congruence_triangles(F, G, T, G, F, A)

By congruence_triangles_heights on F, G, T, G, F, A we get distance_from_line(T, Line(F, G)) == distance_from_line(A, Line(F, G))

By same_ditance_imply_parallel A, T, Line(F, G) we get parallel(Line(A, T), Line(F, G))

