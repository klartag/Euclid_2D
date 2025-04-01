Assumptions:
A, B, C, D, E, F, G: Point
w: Circle
distinct(A, B, C, D, E, F, G)

angle(A, B, C) < 90 mod 360
angle(B, C, A) < 90 mod 360
angle(C, A, B) < 90 mod 360

w == Circle(A, B, C)

between(A, D, B)
between(A, E, C)
distance(A, D) == distance(A, E)

F in perpendicular_bisector(B, D), w
G in perpendicular_bisector(C, E), w

orientation(A, F, B) == orientation(A, B, C)
orientation(A, G, C) == orientation(A, C, B)

Need to prove:
parallel(Line(D, E), Line(F, G))

Proof:
