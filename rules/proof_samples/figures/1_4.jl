Assumptions:
A, B, C, O: Point
distinct(A, B, C, O)
O == center(Circle(A, B, C))

Need to prove:
2 * angle(A, B, C) == angle(A, O, C) mod 360

Proof:
By angle_to_center on A, B, C, Circle(A,B,C) we get coangle(A,B,C) == halfangle(A,O,C) - orientation(A,O,C) mod 360
By coangle_definition_v0 on A, B, C we get angle(A,B,C) == coangle(A,B,C) + orientation(A,B,C) mod 360
