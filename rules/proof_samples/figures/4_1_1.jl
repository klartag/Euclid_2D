Assumptions:
A, B, C, H, Ha: Point
distinct(A, B, C, H, Ha)
not_collinear(A, B, C)

H == orthocenter(A, B, C)

perpendicular_bisector(H, Ha) == Line(B, C)

Need to prove:
concyclic(A, B, C, Ha)

Proof:
By point_on_perpendicular_bisector on Ha, H, C, Line(B,C) we get distance(C,H) == distance(C,Ha)
By point_on_perpendicular_bisector on H, Ha, B, Line(B,C) we get distance(B,H) == distance(B,Ha)
By orthocenter_definition on A, C, B we get H in altitude(A,B,C), H in altitude(C,A,B), H in altitude(B,A,C)
By line_definition on B, H, altitude(B,A,C) we get Line(B,H) == altitude(B,A,C)
By line_definition on H, C, altitude(C,A,B) we get Line(C,H) == altitude(C,A,B)
By isosceles_triangle_properties on C, Ha, H we get distance(C,H) == distance(C,Ha), angle(C,Ha,H) == angle(Ha,H,C) mod 360, orientation(C,Ha,H) == angle(C,Ha,H) + halfangle(H,C,Ha) mod 360
By isosceles_triangle_properties on B, H, Ha we get distance(B,H) == distance(B,Ha), angle(B,H,Ha) == angle(H,Ha,B) mod 360, orientation(B,H,Ha) == angle(B,H,Ha) + halfangle(Ha,B,H) mod 360
By perpendicular_direction_conditions_v0_r on A, C, H, B we get 180 == 2 * direction(A,C) - 2 * direction(H,B) mod 360
By perpendicular_direction_conditions_v0_r on H, C, A, B we get 180 == 2 * direction(H,C) - 2 * direction(A,B) mod 360
By divide_by_2_two_angles on B, A, C, B, Ha, C we get coangle(B,A,C) == coangle(B,Ha,C) mod 360
By concyclic_sufficient_conditions on B, A, C, Ha we get concyclic(A, B, C, Ha)
