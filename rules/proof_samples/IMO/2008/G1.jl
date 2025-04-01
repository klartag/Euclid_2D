Assumptions:
A, B, C, H, A0, B0, C0, A1, B1, C1, A2, B2, C2: Point
wa, wb, wc: Circle
distinct(A, B, C, H, A0, B0, C0, A1, B1, C1, A2, B2, C2)

acute_triangle(A, B, C)

H == orthocenter(A, B, C)
A0 == midpoint(B, C)
B0 == midpoint(A, C)
C0 == midpoint(A, B)

center(wa) == A0
center(wb) == B0
center(wc) == C0
H in wa, wb, wc

A1, A2 in wa, Line(B, C)
B1, B2 in wa, Line(A, C)
C1, C2 in wa, Line(A, B)

Need to prove:
concyclic(A1, A2, B1, B2)
concyclic(A2, B1, B2, C1)
concyclic(B1, B2, C1, C2)

Proof:
