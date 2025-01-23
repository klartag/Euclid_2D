Assumptions:
A, B, C, D, E: Point
c1, c2: Circle

distinct(A, B, C, D, E)

c1 == incircle(A, B, C)
c2 == excircle(A, B, C)

D == line_circle_tangent_point(Line(B, C), c1)
E == line_circle_tangent_point(Line(B, C), c2)

Need to prove:
distance(B, D) == distance(E, C)

Proof:
# Found by the proof generator
By tangent_lengths_equal on C, Line(A,C), Line(B,C), c2 we get distance(C,line_circle_tangent_point(Line(A,C),c2)) == distance(C,line_circle_tangent_point(Line(B,C),c2))
By tangent_lengths_equal on C, Line(B,C), Line(A,C), c1 we get distance(C,line_circle_tangent_point(Line(A,C),c1)) == distance(C,line_circle_tangent_point(Line(B,C),c1))
By tangent_lengths_equal on B, Line(A,B), Line(B,C), c1 we get distance(B,line_circle_tangent_point(Line(A,B),c1)) == distance(B,line_circle_tangent_point(Line(B,C),c1))
By tangent_lengths_equal on B, Line(B,C), Line(A,B), c2 we get distance(B,line_circle_tangent_point(Line(A,B),c2)) == distance(B,line_circle_tangent_point(Line(B,C),c2))
By tangent_lengths_equal on A, Line(A,B), Line(A,C), c2 we get distance(A,line_circle_tangent_point(Line(A,B),c2)) == distance(A,line_circle_tangent_point(Line(A,C),c2))
By tangent_lengths_equal on A, Line(A,B), Line(A,C), c1 we get distance(A,line_circle_tangent_point(Line(A,B),c1)) == distance(A,line_circle_tangent_point(Line(A,C),c1))
By excircle_tangency_order on A, C, B we get between(A, C, line_circle_tangent_point(Line(A,C),c2)), between(B, line_circle_tangent_point(Line(B,C),c2), C), between(A, B, line_circle_tangent_point(Line(A,B),c2))
By incircle_tangency_order on B, C, A we get between(B, line_circle_tangent_point(Line(B,C),c1), C), between(A, line_circle_tangent_point(Line(A,C),c1), C), between(A, line_circle_tangent_point(Line(A,B),c1), B)
By between_imply_segment_sum on line_circle_tangent_point(Line(A,C),c2), C, A we get distance(A,line_circle_tangent_point(Line(A,C),c2)) == distance(C,line_circle_tangent_point(Line(A,C),c2)) + distance(A,C)
By between_imply_segment_sum on A, B, line_circle_tangent_point(Line(A,B),c2) we get distance(A,line_circle_tangent_point(Line(A,B),c2)) == distance(A,B) + distance(B,line_circle_tangent_point(Line(A,B),c2))
By between_imply_segment_sum on C, D, B we get distance(B,C) == distance(C,D) + distance(B,D)
By between_imply_segment_sum on B, line_circle_tangent_point(Line(A,B),c1), A we get distance(A,B) == distance(B,line_circle_tangent_point(Line(A,B),c1)) + distance(A,line_circle_tangent_point(Line(A,B),c1))
By between_imply_segment_sum on A, line_circle_tangent_point(Line(A,C),c1), C we get distance(A,C) == distance(A,line_circle_tangent_point(Line(A,C),c1)) + distance(C,line_circle_tangent_point(Line(A,C),c1))
By between_imply_segment_sum on C, E, B we get distance(B,C) == distance(C,E) + distance(B,E)
