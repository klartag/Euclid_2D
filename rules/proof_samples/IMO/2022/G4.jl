Assumptions:

# objects
A, B, C, O, D, W, X, Y, Z: Point
l_D : Line

# constructed objects
O == circumcenter(A, B, C)
l_D == perpendicular_line(D, Line(B, C))
W == line_intersection(l_D, Line(A, O)) 
X == line_intersection(l_D, Line(A, C))
Y == line_intersection(l_D, Line(A, B))
Z == circle_circle_other_intersection(A, Circle(A, X, Y), Circle(A, B, C))

# assumptions
acute_triangle(A, B, C)
distance(A, C) != distance(A, B) #instead of distance(A, C) > distance(A, B) # we do not define '>' between objects.
distinct(B, D, C)
between(B, D, C)
Z != A
distance(O, W) == distance(O, D)

#distinct objects
distinct(A, B, C, O, D, W, X, Y, Z)

exists(Line(Z, X))
exists(Line(Z, A))
exists(Line(Y, Z))

Need to prove:
tangent(Line(D, Z), Circle(A, X, Y))

Proof:
By acute_triangle_properties_v0 on A, B, C we get inside_triangle(O, A, B, C)
Let E := line_intersection(Line(A, O), Line(B, C))
It is almost always true that D != E
By Line_definition on D, E, Line(B, C) we get Line(B, C) == Line(D, E)
By Line_definition on D, W, l_D we get l_D == Line(D, W)
By triangle_sufficient_conditions_v1 on D, W, E we get triangle(D, W, E)
By right_triangle_sufficient_conditions on W, D, E we get right_triangle(W, D, E)
By Line_definition on W, E, Line(A, O) we get Line(A, O) == Line(W, E)
By circumcenter_and_right_triangle_2 on W, D, E, O we get O == circumcenter(W, D, E)
By two_points_on_circle on E, D, Circle(W, D, E) we get distance(O, D) == distance(O, E)
# We have proved distance(O, D) == distance(O, E)
It is almost always true that triangle(D, O, E)
Let l := altitude(O, D, E)
We have proved l == altitude(O, B, C)
By isosceles_internal_angle_bisector_v2 on O, D, E we get l == perpendicular_bisector(D, E)
By isosceles_internal_angle_bisector_v2 on O, B, C we get l == perpendicular_bisector(B, C)
We have proved D == line_reflection(E, l)
# angle computation
By Line_definition on D, X, l_D we get l_D == Line(D, X)
By complementary_angles_180_v0 on Z, D, X, Y we get angle(D, X, Z) + angle(Z, X, Y) == 0 mod 180
By angles_on_chord on Z, Y, A, X, Circle(A, X, Y) we get angle(Z, X, Y) == angle(Z, A, Y) mod 180
By angles_on_chord on Z, B, A, C, Circle(A, B, C) we get angle(Z, C, B) == angle(Z, A, B) mod 180
By complementary_angles_180_v0 on Z, B, A, Y we get angle(B, A, Z) + angle(Z, A, Y) == 0 mod 180
We have proved angle(D, X, Z) + angle(Z, C, D) == 0 mod 180
It is almost always true that triangle(C, D, X)
By four_points_concyclic_sufficient_conditions_v0 on C, D, X, Z we get concyclic(C, D, X, Z)
# show AZ || BC
Let Z' := line_circle_other_intersection(A, parallel_line(A, Line(B, C)), Circle(A, B, C))
It is almost always true that Z' != A # we don't have in line_circle_other_intersection somthing that tell that Z' != A
We have proved B == line_reflection(C, l)
By Line_definition on Z', A, parallel_line(A, Line(B, C)) we get parallel_line(A, Line(B, C)) == Line(A, Z') 
We have proved perpendicular(l, Line(A, Z'))
By perpendicular_to_chord_bisect_it on A, Z', l, Circle(A, B, C) we get l == perpendicular_bisector(A, Z')
We have proved A == line_reflection(Z', l)
# angle computation
It is almost always true that A != E
By reflection_of_three_points_through_line on B, A, E, C, Z', D, l we get angle(C, Z', D) + angle(B, A, E) == 0
We have proved angle(D, Z', C) == angle(B, A, E)
By Line_definition on A, E, Line(A, O) we get Line(A, O) == Line(A, E)
We have proved angle(B, A, E) == angle(B, A, O) mod 180
By circle_radius_v0_r on A, Circle(A, B, C) we get distance(A, O) == radius(Circle(A, B, C))
By circle_radius_v0_r on B, Circle(A, B, C) we get distance(B, O) == radius(Circle(A, B, C))
By isosceles_angles_segments_v0 on O, A, B we get angle(O, A, B) == angle(A, B, O)
It is almost always true that triangle(A, B, O)
We have proved angle(B, A, O) + angle(A, O, B) + angle(O, B, A) == 180 mod 360
We have proved angle(A, O, B) + 2 * angle(B, A, O) == 180 mod 360
By angle_to_center_theorem_360 on A, B, C, Circle(A, B, C) we get angle(A, O, B) == 2 * angle(A, C, B) mod 360
By divide_by_2_mod_360 on angle(A, C, B) + angle(B, A, O), 90 we get angle(A, C, B) + angle(B, A, O) == 90 mod 180

We have proved angle(C, D, X) == 90 mod 180
We have proved angle(D, X, C) == 90 - angle(X, C, D) mod 180
We have proved angle(B, A, O) == 90 - angle(A, C, B) mod 180
We have proved 90 - angle(A, C, B) == 90 - angle(A, C, B) mod 180
By Line_definition on X, C, Line(A, C) we get Line(A, C) == Line(X, C)
By Line_definition on D, C, Line(B, C) we get Line(B, C) == Line(D, C)
We have proved angle(D, Z', C) == angle(D, X ,C) mod 180
# show Z == Z'
It is almost always true that triangle(D, Z', C)
It is almost always true that distinct(D, Z', C, X)

By four_points_concyclic_sufficient_conditions_v0 on D, Z', C, X we get concyclic(D, Z', C, X)
We introduce Circle(C, D, X)
If Circle(A, B, C) == Circle(C, D, X):
    By circle_line_at_most_two_intersections on A, C, X, Line(A, C), Circle(A, B, C) we get A == C
    By point_equality_contradiction on A we get false()
We have proved Circle(A, B, C) != Circle(C, D, X)
By two_circles_have_at_most_2_points_in_common on Z, Z', C, Circle(A, B, C), Circle(C, D, X) we get Z == Z'
# angle computation
By Line_definition on C, D, Line(B, C) we get Line(B, C) == Line(D, C)
We have proved parallel(Line(C, D), Line(A, Z))
#We have proved angle(A, Z, D) == line_angle(Line(D, Z)) - line_angle(Line(Z, A))
We have proved angle(A, Z, D) == angle(C, D, Z) mod 180
By angles_on_chord on C, Z, X, D, Circle(C, D, X) we get angle(C, X, Z) == angle(C, D, Z) mod 180
By angles_on_chord on A, Z, X, Y, Circle(A, Y, X) we get angle(A, X, Z) == angle(A, Y, Z) mod 180
By Line_definition on A, X, Line(A, C) we get Line(A, C) == Line(A, X)
By complementary_angles_180_v0 Z, A, X, C we get angle(A, X, Z) + angle(Z, X, C) == 0 mod 180
We have proved angle(C, X, Z) == angle(A, Y, Z) mod 180
# finish
By tangent_angle_180_v1 on Z, A, Y, Line(D, Z), Circle(A, X, Y) we get tangent(Line(D, Z), Circle(A, X, Y))