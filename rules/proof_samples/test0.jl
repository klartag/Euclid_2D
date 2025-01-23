Assumptions:
A, B, C, D, E, F, G, H: Point
f, g: Line
c, d: Circle
distinct(A, B, C, D, E, F, G, H)
distinct(f, g)
distinct(c, d)
A in c
B in c
C in c
D in c
f == Line(A, B)
E == center(c)
g == internal_angle_bisector(B, E, C)
F == projection(B, g)
G == line_intersection(f, g)
d == Circle(C, D, F)
H in g, d

Need to prove:
concyclic(A, D, G, H)

Proof:
By line_definition on G, F, g we get g == Line(F, G)
By circle_definition on B, C, D, c we get c == Circle(B, C, D)
By circle_definition on A, B, D, c we get c == Circle(A, B, D)
By circle_definition on F, D, H, d we get d == Circle(D, F, H)
By circle_radius_v0_r on B, c we get radius(c) == distance(B, center(c))
By circle_radius_v0_r on C, c we get radius(c) == distance(C, center(c))
By angles_on_chord on F, D, H, C, d we get coangle(F, C, D) == coangle(F, H, D) mod 360
By angles_on_chord on B, D, C, A, c we get coangle(B, A, D) == coangle(B, C, D) mod 360
By in_imply_collinear on G, B, A we get collinear(A, B, G)
By in_imply_collinear on H, G, F we get collinear(F, G, H)
By isosceles_triangle_altitude_v2 on E, B, C we get identical(perpendicular_bisector(B, C), internal_angle_bisector(B, E, C), perpendicular_line(E, Line(B, C)))
By perpendicular_line_definition on B, Line(B, C), g we get Line(B, C) == perpendicular_line(B, g)
By same_angle on A, B, G, D we get coangle(B, A, D) == coangle(G, A, D) mod 360
By same_angle on H, F, G, D we get coangle(F, H, D) == coangle(G, H, D) mod 360
By same_angle on C, B, midpoint(B, C), D we get coangle(B, C, D) == coangle(midpoint(B, C), C, D) mod 360
By perpendicular_bisector_properties on C, B we get perpendicular(Line(B, C), perpendicular_bisector(B, C)), midpoint(B, C) == line_intersection(Line(B, C), perpendicular_bisector(B, C))
By concyclic_sufficient_conditions on G, H, D, A we get concyclic(A, D, G, H)
