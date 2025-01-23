Assumptions:
A, B, C, D, E: Point

distinct(A, B, C, D, E)

Need to prove:
angle(A, C, E) + angle(B, D, A) + angle(C, E, B) + angle(D, A, C) + angle(E, B, D) == 180 mod 360

Proof:
By reverse_direction on A, C we get 180 == direction(A,C) - direction(C,A) mod 360
By reverse_direction on D, B we get 180 == direction(D,B) - direction(B,D) mod 360
By reverse_direction on C, E we get 180 == direction(C,E) - direction(E,C) mod 360
By reverse_direction on A, D we get 180 == direction(A,D) - direction(D,A) mod 360
By reverse_direction on B, E we get 180 == direction(B,E) - direction(E,B) mod 360