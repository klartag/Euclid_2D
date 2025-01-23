Assumptions:
A, B, C, D, E, F, M, N, P, Q: Point
w_B, w_C: Circle
distinct(A, B, C, D, E, F, M, N, P, Q)
distinct(w_B, w_C)
triangle(A, B, C)
D == projection(A, Line(B, C))
E == projection(B, Line(A, C))
F == projection(C, Line(B, A))
w_B == incircle(B, D, F)
w_C == incircle(C, D, E)
tangent(Line(D, F), w_B)
M in Line(D, F), w_B
tangent(Line(D, E), w_C)
N in Line(D, E), w_C
P == line_circle_other_intersection(M, Line(M, N), w_B)
Q == line_circle_other_intersection(N, Line(M, N), w_C)

Need to prove:
distance(M, P) == distance(N, Q)

Proof:
Let O_B := center(w_B)
Let O_C := center(w_C)
Let r_B := radius(w_B)
Let r_C := radius(w_C)
Let T := intersection_of_tangent_line_and_circle(Line(B, C), w_B)
Let U := intersection_of_tangent_line_and_circle(Line(B, C), w_C)
It is almost always true that distinct(A, B, C, D, E, F, M, N, P, Q, O_B, O_C, T, U)
It is almost always true that triangle(A, C, F)
It is almost always true that triangle(A, B, E)
We have proved perpendicular(Line(A, D), Line(B, C))
We have proved perpendicular(Line(C, F), Line(B, A))
By four_points_concyclic_sufficient_conditions_v0 on C, F, A, D we get concyclic(C, F, A, D)
By four_points_concyclic_sufficient_conditions_v0 on B, E, A, D we get concyclic(B, E, A, D)

#



