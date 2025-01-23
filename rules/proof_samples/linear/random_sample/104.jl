Assumptions:
A, B, C, D, E, F, G, H, I, J: Point
f, g, h, i, j, k: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H, I, J)
distinct(f, g, h, i, j, k)
distinct(c, d)
f == Line(B, A)
g == Line(B, C)
h == Line(C, A)
D == projection(A, g)
E == projection(B, h)
F == projection(C, f)
i == Line(D, A)
j == Line(B, E)
k == Line(C, F)
G == line_intersection(i, j)
H in k
c == Circle(G, A, H)
I in c
d == Circle(D, A, I)
J in g, d

Need to prove:
concyclic(C, H, I, J)

Proof:
By line_definition on H, C, k we get k == Line(C, H)
By line_definition on J, D, g we get g == Line(D, J)
By line_definition on E, B, perpendicular_line(B, h) we get Line(B, E) == perpendicular_line(B, h)
By line_definition on C, F, perpendicular_line(C, f) we get Line(C, F) == perpendicular_line(C, f)
By line_definition on A, D, perpendicular_line(A, g) we get Line(A, D) == perpendicular_line(A, g)
By circle_definition on J, D, I, d we get d == Circle(D, I, J)
By circle_definition on I, H, G, c we get c == Circle(G, H, I)
By circle_definition on G, A, I, c we get c == Circle(A, G, I)
By line_unique_intersection_v1 on h, g, C, B we get B not in h
By angles_on_chord on D, I, A, J, d we get coangle(D, A, I) == coangle(D, J, I) mod 360
By angles_on_chord on G, I, H, A, c we get coangle(G, A, I) == coangle(G, H, I) mod 360
By in_imply_collinear on G, D, A we get collinear(A, D, G)
By in_imply_collinear on C, J, D we get collinear(C, D, J)
By not_in_line_equivalent_to_not_collinear_v0 on B, C, A we get not_collinear(A, B, C), exists(Line(A, C))
By same_angle on A, G, D, I we get coangle(D, A, I) == coangle(G, A, I) mod 360
By same_angle on J, D, C, I we get coangle(C, J, I) == coangle(D, J, I) mod 360
By orthocenter_concurrency on A, C, B we get orthocenter(A, B, C) in altitude(A, B, C), orthocenter(A, B, C) in altitude(C, A, B), orthocenter(A, B, C) in altitude(B, A, C)
By line_intersection_definition on orthocenter(A, B, C), j, i we get orthocenter(A, B, C) == line_intersection(i, j)
By in_imply_collinear on orthocenter(A, B, C), C, H we get collinear(C, H, orthocenter(A, B, C))
By same_angle on H, G, C, I we get coangle(C, H, I) == coangle(G, H, I) mod 360
By concyclic_sufficient_conditions on C, H, I, J we get concyclic(C, H, I, J)
