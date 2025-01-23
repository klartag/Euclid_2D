Assumptions:
A, B, C, O: Point
perpendicular(Line(A, B), Line(A, C))
O == midpoint(B, C)

Need to prove:
distance(A, O) == distance(B, O)

Proof:
# Found by the proof generator
By right_triangle_circumcenter_v1 on B, A, C we get O == circumcenter(A,B,C)
By circle_radius_v0_r on C, Circle(A,B,C) we get distance(C,O) == radius(Circle(A,B,C))
By circle_radius_v0_r on A, Circle(A,B,C) we get distance(A,O) == radius(Circle(A,B,C))
