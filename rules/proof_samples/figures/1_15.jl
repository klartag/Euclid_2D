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
between(C, line_circle_tangent_point(Line(C, D), c), D)
between(D, line_circle_tangent_point(Line(D, A), c), A)


Need to prove:
distance(A, B) + distance(C, D) == distance(B, C) + distance(D, A)

Proof:
By tangent_lengths_equal on A, Line(A,B), Line(A,D), c we get distance(A,line_circle_tangent_point(Line(A,B),c)) == distance(A,line_circle_tangent_point(Line(A,D),c))
By tangent_lengths_equal on B, Line(A,B), Line(B,C), c we get distance(B,line_circle_tangent_point(Line(A,B),c)) == distance(B,line_circle_tangent_point(Line(B,C),c))
By tangent_lengths_equal on C, Line(B,C), Line(C,D), c we get distance(C,line_circle_tangent_point(Line(B,C),c)) == distance(C,line_circle_tangent_point(Line(C,D),c))
By tangent_lengths_equal on D, Line(C,D), Line(A,D), c we get distance(D,line_circle_tangent_point(Line(A,D),c)) == distance(D,line_circle_tangent_point(Line(C,D),c))
By between_imply_segment_sum on C, line_circle_tangent_point(Line(B,C),c), B we get distance(B,C) == distance(C,line_circle_tangent_point(Line(B,C),c)) + distance(B,line_circle_tangent_point(Line(B,C),c))
By between_imply_segment_sum on B, line_circle_tangent_point(Line(A,B),c), A we get distance(A,B) == distance(B,line_circle_tangent_point(Line(A,B),c)) + distance(A,line_circle_tangent_point(Line(A,B),c))
By between_imply_segment_sum on D, line_circle_tangent_point(Line(C,D),c), C we get distance(C,D) == distance(D,line_circle_tangent_point(Line(C,D),c)) + distance(C,line_circle_tangent_point(Line(C,D),c))
By between_imply_segment_sum on A, line_circle_tangent_point(Line(A,D),c), D we get distance(A,D) == distance(A,line_circle_tangent_point(Line(A,D),c)) + distance(D,line_circle_tangent_point(Line(A,D),c))
