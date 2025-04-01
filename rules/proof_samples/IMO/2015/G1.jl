Assumptions:
A, B, C, G, H, I, J: Point
distinct(A, B, C, G, H, I, J)

angle(A, B, C) < 90 mod 360
angle(B, C, A) < 90 mod 360
angle(C, A, B) < 90 mod 360

H == orthocenter(A, B, C)
parallelogram(A, B, G, H)
I in Line(G, H)
collinear(A, C, midpoint(H, I))

J in Line(A, C), Circle(G, C, I)

Need to prove:
distance(I, J) == distance(A, H)

Proof:
