Assumptions:
A, B, C, A_1, B_1, P, Q, P_1, Q_1: Point
distinct(A, B, C, A_1, B_1, P, Q, P_1, Q_1)
triangle(A, B, C)
between(B, A_1, C)
between(A, B_1, C)
between(A, P, A_1)
between(B, Q, B_1)
parallel(Line(P, Q), Line(A, B))
between(P, B_1, P_1)
between(Q, A_1, Q_1)
angle(P, P_1, C) == angle(B, A, C)
angle(C, Q_1, Q) == angle(C, B, A)

Need to prove:
concyclic(P, Q, P_1, Q_1)

Proof:
Let A_2 := line_circle_other_intersection(A, Line(A, A_1), Circle(A, B, C))
Let B_2 := line_circle_other_intersection(B, Line(B, B_1), Circle(A, B, C))
It is almost always true that distinct(A, B, C, A_1, B_1, P, Q, P_1, Q_1, A_2, B_2)
We have proved angle(Q, P, A_2) == angle(B, A, A_2) mod 180
We have proved concyclic(A, B, A_2, B_2)
We have proved angle(B, A, A_2) == angle(B, B_2, A_2) mod 180
We have proved angle(Q, P, A_2) == angle(Q, B_2, A_2) mod 180
It is almost always true that not_collinear(P, Q, A_2)
By four_points_concyclic_sufficient_conditions_v0 on Q, P, A_2, B_2 we get concyclic(Q, P, A_2, B_2)
Let w := Circle(Q, P, A_2)

We have proved angle(C, A_2, A_1) == angle(C, Q_1, A_1) mod 180
It is almost always true that not_collinear(C, A_2, A_1)
By four_points_concyclic_sufficient_conditions_v0 on C, A_2, A_1, Q_1 we get concyclic(C, A_2, A_1, Q_1)
We have proved angle(Q, Q_1, A_2) == angle(Q, P, A_2) mod 180
It is almost always true that not_collinear(Q, Q_1, A_2)
By four_points_concyclic_sufficient_conditions_v0 on Q, Q_1, A_2, P we get concyclic(Q, Q_1, A_2, P)

We have proved angle(C, B_2, B_1) == angle(C, P_1, B_1) mod 180
It is almost always true that not_collinear(C, B_2, B_1)
By four_points_concyclic_sufficient_conditions_v0 on C, B_2, B_1, P_1 we get concyclic(C, B_2, B_1, P_1)
We have proved angle(P, P_1, B_2) == angle(P, Q, B_2) mod 180
It is almost always true that not_collinear(P, P_1, B_2)
By four_points_concyclic_sufficient_conditions_v0 on P, P_1, B_2, Q we get concyclic(P, P_1, B_2, Q)

