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
c == Circle(B, D, A)
d == Circle(H, G, E)
I in d, c
J in k, d

Need to prove:
concyclic(A, F, I, J)

Proof:
By line_definition on A, D, perpendicular_line(A, g) we get Line(A, D) == perpendicular_line(A, g)
By line_definition on F, J, k we get k == Line(F, J)
By line_definition on F, C, perpendicular_line(C, f) we get Line(C, F) == perpendicular_line(C, f)
By line_definition on A, E, h we get h == Line(A, E)
By line_definition on E, B, perpendicular_line(B, h) we get Line(B, E) == perpendicular_line(B, h)
By line_definition on D, B, g we get g == Line(B, D)
By circle_definition on A, B, I, c we get c == Circle(A, B, I)
By circle_definition on E, G, I, d we get d == Circle(E, G, I)
By circle_definition on G, I, J, d we get d == Circle(G, I, J)
By line_unique_intersection_v1 on h, f, A, B we get B not in h
By angles_on_chord on G, I, J, E, d we get coangle(G, E, I) == coangle(G, J, I) mod 360
By angles_on_chord on B, I, D, A, c we get coangle(B, A, I) == coangle(B, D, I) mod 360
By in_imply_collinear on G, B, E we get collinear(B, E, G)
By in_imply_collinear on F, B, A we get collinear(A, B, F)
By not_in_line_equivalent_to_not_collinear_v0 on B, A, C we get not_collinear(A, B, C), exists(Line(A, C))
By perpendicular_angle_conditions_v0 on A, D, B we get 0 == coangle(A, D, B) mod 360
By perpendicular_angle_conditions_v0 on A, E, B we get 0 == coangle(A, E, B) mod 360
By concyclic_sufficient_conditions on A, D, B, E we get concyclic(A, B, D, E)
By same_angle on E, G, B, I we get coangle(B, E, I) == coangle(G, E, I) mod 360
By same_angle on A, B, F, I we get coangle(B, A, I) == coangle(F, A, I) mod 360
By orthocenter_concurrency on C, A, B we get orthocenter(A, B, C) in altitude(C, A, B), orthocenter(A, B, C) in altitude(A, B, C), orthocenter(A, B, C) in altitude(B, A, C)
By concyclic_definition_0 on D, A, B, E we get E in Circle(A, B, D)
By line_intersection_definition on orthocenter(A, B, C), i, j we get orthocenter(A, B, C) == line_intersection(i, j)
By angles_on_chord on B, I, D, E, c we get coangle(B, D, I) == coangle(B, E, I) mod 360
By in_imply_collinear on orthocenter(A, B, C), F, J we get collinear(F, J, orthocenter(A, B, C))
By same_angle on J, G, F, I we get coangle(F, J, I) == coangle(G, J, I) mod 360
By concyclic_sufficient_conditions on F, A, I, J we get concyclic(A, F, I, J)
