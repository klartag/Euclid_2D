Assumptions:
A, B, C, D: Point
distinct(A, B, C, D)
not_collinear(A, B, C)
between(A, D, C)
angle(B, A, C) == 80 mod 360
angle(A, C, B) == 45 mod 360
angle(B, D, C) == 115 mod 360

Need to prove: 
angle(D, B, A) == 35 mod 360

Proof:
By between_implies_orientation on B, A, D, C we get orientation(B,A,D) == orientation(B,D,C) mod 360, orientation(B,A,C) == orientation(B,A,D) mod 360
By same_angle on C, A, D, B we get coangle(A,C,B) == coangle(D,C,B) mod 360
By triangle_halfangle_sum on A, C, B we get orientation(A,C,B) == halfangle(A,C,B) + halfangle(C,B,A) + halfangle(B,A,C) mod 360
By triangle_halfangle_sum on B, A, C we get orientation(B,A,C) == halfangle(B,A,C) + halfangle(A,C,B) + halfangle(C,B,A) mod 360
By triangle_halfangle_sum on B, D, C we get orientation(B,D,C) == halfangle(B,D,C) + halfangle(D,C,B) + halfangle(C,B,D) mod 360
By triangle_halfangle_sum on D, C, B we get orientation(D,C,B) == halfangle(D,C,B) + halfangle(C,B,D) + halfangle(B,D,C) mod 360
By angle_equality_conversions_v0_r on D, C, B, A, C, B we get angle(A,C,B) == angle(D,C,B) mod 360
