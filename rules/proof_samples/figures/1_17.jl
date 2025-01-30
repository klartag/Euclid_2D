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
