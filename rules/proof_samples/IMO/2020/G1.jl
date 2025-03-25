Assumptions:
# free objects
A, B, C, D, P, Q, E, F: Point
l: Line
omega: Circle
distinct(A,B,C,D,P,Q,E,F)
isosceles_triangle(C, A, B)
between(A,D,midpoint(A,B))
between(B,P,C)
perpendicular(Line(D,P), Line(P,B))
between(A,Q,C)
perpendicular(Line(D,Q), Line(Q,C))
l == perpendicular_bisector(P,Q)
E in l 
between(C, E, Q)
omega == Circle(C, P, Q)
F in omega
F in Circle(A,B,C)
collinear(F,E,P)
Need to prove:
perpendicular(Line(A,C), Line(B,C))


Proof:
