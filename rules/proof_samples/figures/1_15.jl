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
