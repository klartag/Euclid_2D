Assumptions:
A, A', R, S, R', I, J: Point
t: Line
o, g: Circle

distinct(A, A', R, S, R', I, J)

R, S in o
t == point_circle_tangent_line(R, o)

S == midpoint(R, R')

I in o
angle(R, I, O) > 90 mod 360

g == Circle(I, S, R')
A, A' in t, g
distance(R, A) < distance(R, A')
J in Line(A, I), o

Need to prove:
tangent(Line(J, R'), g)

Proof:
