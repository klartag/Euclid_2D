Assumptions:
A, B, C, D, E, F, P, X, Y: Point

distinct(A, B, C, D, E, F, P, X, Y)

# Acute triangle data.
triangle(A, B, C)
# exists(Line(A, B), Line(B, C), Line(C, A)) should automatically be concluded as part of `triangle`,
# but it isn't, even when adding it to the definition of triangle.
exists(Line(A, B), Line(B, C), Line(C, A))

triangle(A, B, F)
triangle(A, C, F)
# exists(Line(A, F)) should automatically be concluded as part of `triangle`,
# but it isn't, even when adding it to the definition of triangle.
exists(Line(A, F))

angle(A, F, B) == 90
between(B, F, C)

P not in Line(B, C)  # P is not degenerate.
between(A, P, F)
between(F, D, C)  # Can probably be proved and removed from here.
between(B, E, F)
angle(A, C, F) == angle(P, D, F)
angle(A, B, F) == angle(P, E, F)

cb: Circle
cc: Circle
cb != cc
A, B, D, X in cb
distance(D, X) == distance(D, A)

A, C, E, Y in cc
distance(E, Y) == distance(E, A)

exists(Line(B, X))
exists(Line(C, Y))

Need to prove:
concyclic(B, C, X, Y)

Proof:
# Proving the left reflection. This could be packaged into fewer theorems, but it isn't neccessary.
By angles_on_chord on A, D, B, X, cb we get angle(A, B, D) == angle(A, X, D) mod 180
By angles_on_chord on D, X, A, B, cb we get angle(D, B, X) == angle(D, A, X) mod 180
# This is neccessary because we introduce both the angle and its negative at the same time.
By concyclic_to_triangle on A, D, X, cb we get triangle(A, D, X)
By congruent_triangles_v4 on A, D, X, X, D, A we get angle(A, X, D) + angle(X, A, D) == 0 

# Proving the right reflection.
By angles_on_chord on A, E, C, Y, cc we get angle(A, C, E) == angle(A, Y, E) mod 180
By angles_on_chord on E, Y, A, C, cc we get angle(E, C, Y) == angle(E, A, Y) mod 180
# This is neccessary because we introduce both the angle and its negative at the same time.
By concyclic_to_triangle on A, E, Y, cc we get triangle(A, E, Y)
By congruent_triangles_v4 on A, E, Y, Y, E, A we get angle(A, Y, E) + angle(Y, A, E) == 0

# Intersecting and getting A'
Let A' := line_intersection(Line(B, X), Line(C, Y))

By triangle_angles_360 on B, A, C we get angle(B, A, C) + angle(A, C, B) + angle(C, B, A) == 180 mod 360
By same_angle_v0 on A, B, D, C we get angle(A, B, D) == angle(A, B, C) mod 180
By same_angle_v0 on X, B, D, C we get angle(X, B, D) == angle(X, B, C) mod 180
By same_angle_v0 on A, C, E, B we get angle(A, C, E) == angle(A, C, B) mod 180
By same_angle_v0 on Y, C, E, B we get angle(Y, C, E) == angle(Y, C, B) mod 180

It is almost always true that distinct(A, B, C, D, E, F, P, X, Y, A')

# Showing that A, F, A' are collinear.

We have shown line_angle(Line(C, Y)) - line_angle(Line(B, C)) != 0 mod 180
By different_lines on Line(C, Y), Line(B, C) we get Line(C, Y) != Line(B, C)
By different_lines on Line(B, X), Line(B, C) we get Line(B, X) != Line(B, C)

If A' == B:
    By line_unique_points on A', C, Line(B, C), Line(C, Y) we get Line(B, C) == Line(C, Y)
    By line_equality_contradiction on Line(B, C) we get false()

If A' == C:
    By line_unique_points on A', B, Line(B, C), Line(B, X) we get Line(B, C) == Line(B, X)
    By line_equality_contradiction on Line(B, C) we get false()


# We have proved A' in Line(B, X)
# We have proved collinear(A', X, B)
# By line_equality_v3 on B, X, A' we get Line(A', B) == Line(B, X)
# By line_equality_v3 on C, Y, A' we get Line(A', C) == Line(C, Y)

# We have to state that the angles exist before we can use line-angle equations.
Let a1 := angle(A', B, C)
Let a2 := angle(B, C, A')
Let d1 := distance(B, C)
By congruent_triangles_v3 on B, C, A, B, C, A' we get distance(B, A) == distance(B, A')
By congruent_triangles_v3 on B, C, A, B, C, A' we get triangle(B, C, A')
By triangle_non_trivial on B, C, A' we get A' != B, A' != C, A' not in Line(B, C)
By point_not_in_line on Line(B, C), F, A' we get A' != F
By same_angle_v2 on A, B, F, C we get angle(A, B, F) == angle(A, B, C) mod 360
By same_angle_v2 on A', B, F, C we get angle(A', B, F) == angle(A', B, C) mod 360

Let d2 := distance(F, B)
It is almost always true that triangle(F, B, A')
It is almost always true that orientation(F, B, A) != orientation(F, B, A')
By congruent_triangles_v5 on F, B, A, F, B, A' we get angle(A', F, B) + angle(A, F, B) == 0, triangle(F, B, A')

By complementary_angles_180_v1 on B, A, F, A' we get collinear(A, A', F) #A' in Line(A, F)


By triangle_def on F, D, P we get triangle(F, D, P)
By triangle_def on F, E, P we get triangle(F, E, P)

By same_angle_v0 on D, F, P, A we get angle(D, F, P) == angle(D, F, A) mod 180
By same_angle_v0 on A, F, D, C we get angle(A, F, D) == angle(A, F, C) mod 180
By similar_triangles_v0 on A, F, C, P, F, D we get distance(A, F) / distance(P, F) == distance(F, C) / distance(F, D)

By same_angle_v0 on B, F, P, A we get angle(B, F, P) == angle(B, F, A) mod 180  # Here the signature matcher fails.
By same_angle_v0 on P, F, E, B we get angle(P, F, E) == angle(P, F, B) mod 180
By similar_triangles_v0 on A, F, B, P, F, E we get distance(A, F) / distance(P, F) == distance(F, B) / distance(F, E)

It is almost always true that center(cb) != center(cc)
We introduce radical_axis(cb, cc)
By intersection_on_radical on A, cb, cc we get A in radical_axis(cb, cc)

By inner_transitivity_of_between on B, F, D, C we get between(B, F, D)
By inner_transitivity_of_between on C, F, E, B we get between(C, F, E)
By equal_power_on_radical_v4 on F, D, B, E, C, cb, cc we get F in radical_axis(cb, cc)
By line_unique_points on A, F, Line(A, F), radical_axis(cb, cc) we get Line(A, F) == radical_axis(cb, cc)
It is almost always true that distinct(B, C, X, Y, A')
By radical_axis_weak on A', Y, C, X, B, cc, cb we get concyclic(B, C, X, Y) #c, Y in c, C in c, X in c, B in c