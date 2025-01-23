Assumptions:
A, B, C, D: Point
c: Circle

distinct(A, B, C, D)
distinct(Line(A, B), Line(B, C), Line(C, D), Line(D, A))

tangent(Line(A, B), c)
tangent(Line(B, C), c)
tangent(Line(C, D), c)
tangent(Line(D, A), c)

between(A, line_circle_tangent_point(Line(A, B), c), B)
between(B, line_circle_tangent_point(Line(B, C), c), C)
between(C, D, line_circle_tangent_point(Line(C, D), c))
between(line_circle_tangent_point(Line(D, A), c), D, A)

Need to prove:
distance(A, B) + distance(C, D) == distance(B, C) + distance(D, A)

Proof:
By tangent_lengths_equal on C, Line(B,C), Line(C,D), c we get distance(C,line_circle_tangent_point(Line(B,C),c)) == distance(C,line_circle_tangent_point(Line(C,D),c))
By tangent_lengths_equal on B, Line(A,B), Line(B,C), c we get distance(B,line_circle_tangent_point(Line(A,B),c)) == distance(B,line_circle_tangent_point(Line(B,C),c))
By tangent_lengths_equal on D, Line(A,D), Line(C,D), c we get distance(D,line_circle_tangent_point(Line(A,D),c)) == distance(D,line_circle_tangent_point(Line(C,D),c))
By tangent_lengths_equal on A, Line(A,D), Line(A,B), c we get distance(A,line_circle_tangent_point(Line(A,B),c)) == distance(A,line_circle_tangent_point(Line(A,D),c))
By between_imply_segment_sum on B, line_circle_tangent_point(Line(B,C),c), C we get distance(B,C) == distance(B,line_circle_tangent_point(Line(B,C),c)) + distance(C,line_circle_tangent_point(Line(B,C),c))
By between_imply_segment_sum on B, line_circle_tangent_point(Line(A,B),c), A we get distance(A,B) == distance(B,line_circle_tangent_point(Line(A,B),c)) + distance(A,line_circle_tangent_point(Line(A,B),c))
By between_imply_segment_sum on line_circle_tangent_point(Line(A,D),c), D, A we get distance(A,line_circle_tangent_point(Line(A,D),c)) == distance(D,line_circle_tangent_point(Line(A,D),c)) + distance(A,D)
By between_imply_segment_sum on line_circle_tangent_point(Line(C,D),c), D, C we get distance(C,line_circle_tangent_point(Line(C,D),c)) == distance(D,line_circle_tangent_point(Line(C,D),c)) + distance(C,D)
