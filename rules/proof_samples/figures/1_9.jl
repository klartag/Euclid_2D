Assumptions:
A, B, C, D, O: Point
distinct(A, B, C, D, O)
not_collinear(A, O, C)
D == projection(A, Line(B, C))
O == center(Circle(A, B, C))

Need to prove:
angle(D, A, B) == angle(C, A, O) mod 360

Proof:
