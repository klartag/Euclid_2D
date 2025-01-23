Assumptions:
A, B, C, I, D: Point
triangle(A, B, C)
I == incenter(A, B, C)
D == center(Circle(B, I, C))

Need to prove:
concyclic(A, B, C, D)

Proof:
By incenter_isogonal_conjugate on C, B, A we get I == isogonal_conjugate(I,A,B,C)
By triangle_halfangle_sum on C, A, B we get orientation(C,A,B) == halfangle(C,A,B) + halfangle(A,B,C) + halfangle(B,C,A) mod 360
By isogonal_conjugate_definition on C, B, A, I, I we get coangle(B,C,I) == coangle(I,C,A) mod 360, coangle(A,B,I) == coangle(I,B,C) mod 360, coangle(C,A,I) == coangle(I,A,B) mod 360
By angle_to_center on I, B, C, Circle(B,C,I) we get coangle(I,B,C) == halfangle(I,D,C) - orientation(I,D,C) mod 360
By angle_to_center on B, C, I, Circle(B,C,I) we get coangle(B,C,I) == halfangle(B,D,I) - orientation(B,D,I) mod 360
By coangle_definition_v1 on B, C, I we get angle(B,C,I) == coangle(B,C,I) + orientation(B,C,I) mod 360
By coangle_definition_v1 on I, C, A we get angle(I,C,A) == coangle(I,C,A) + orientation(I,C,A) mod 360
By coangle_definition_v1 on A, B, I we get angle(A,B,I) == coangle(A,B,I) + orientation(A,B,I) mod 360
By coangle_definition_v1 on I, B, C we get angle(I,B,C) == coangle(I,B,C) + orientation(I,B,C) mod 360
By divide_by_2_two_angles on C, A, B, C, D, B we get coangle(C,A,B) == coangle(C,D,B) mod 360
By concyclic_sufficient_conditions on C, A, B, D we get concyclic(A, B, C, D)
